# -*- coding: utf-8 -*-
"""Client gọi model qua giao diện kiểu OpenAI (/chat/completions). Chỉ dùng thư viện chuẩn.
GLM, DeepSeek, Qwen đều có điểm cuối kiểu này ở các bản trước; bạn phải tự điền base_url và model đúng theo nhà cung cấp đang dùng (xem models.example.json)."""
import json, os, re, time, urllib.request, urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load_config(path=None):
    p = Path(path or os.environ.get("VNUIS_MODELS", HERE / "models.json"))
    if not p.exists(): p = HERE / "models.example.json"
    return json.loads(p.read_text(encoding="utf-8"))

def extract_json(text):
    """Lấy khối JSON đầu tiên trong câu trả lời (model hay bọc trong ```json hoặc thêm lời dẫn)."""
    t = re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", t, re.S)
    if m: t = m.group(1).strip()
    for opener, closer in (("{", "}"), ("[", "]")):
        i = t.find(opener)
        if i < 0: continue
        depth = 0; ins = False; esc = False
        for j in range(i, len(t)):
            ch = t[j]
            if ins:
                if esc: esc = False
                elif ch == "\\": esc = True
                elif ch == '"': ins = False
            elif ch == '"': ins = True
            elif ch == opener: depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0: return json.loads(t[i:j + 1])
    raise ValueError("không thấy JSON trong câu trả lời: " + text[:200])

class LLM:
    def __init__(self, cfg, name=None):
        self.name = name or cfg.get("default")
        m = cfg["models"][self.name]
        self.base_url = m["base_url"].rstrip("/"); self.model = m["model"]
        self.key = os.environ.get(m.get("api_key_env", ""), "")
        self.json_mode = m.get("supports_json_mode", True)
        self.extra = m.get("extra_body", {})
        self.extra_think = m.get("extra_body_thinking", {}); self.extra_nothink = m.get("extra_body_no_thinking", {})
        self.timeout = m.get("timeout_s", 120); self.retries = m.get("max_retries", 3)
        self.max_tokens = m.get("max_tokens", 4096)
        self.usage = dict(prompt=0, completion=0, calls=0)

    def chat(self, messages, json_out=False, temperature=0.2, max_tokens=None, thinking=None):
        body = {"model": self.model, "messages": messages, "temperature": temperature, "max_tokens": max_tokens or self.max_tokens}
        body.update(self.extra)
        if thinking is True: body.update(self.extra_think)
        if thinking is False: body.update(self.extra_nothink)
        if json_out and self.json_mode: body["response_format"] = {"type": "json_object"}
        req = urllib.request.Request(self.base_url + "/chat/completions", data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json", "Authorization": "Bearer " + self.key})
        last = None
        for a in range(self.retries):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r: d = json.loads(r.read())
                u = d.get("usage") or {}
                self.usage["prompt"] += u.get("prompt_tokens", 0); self.usage["completion"] += u.get("completion_tokens", 0); self.usage["calls"] += 1
                return d["choices"][0]["message"]["content"] or ""
            except urllib.error.HTTPError as e:
                last = e
                if e.code in (429, 500, 502, 503, 504): time.sleep(2 ** a); continue
                raise RuntimeError(f"{e.code}: {e.read()[:300]!r}")
            except (urllib.error.URLError, TimeoutError) as e:
                last = e; time.sleep(2 ** a)
        raise RuntimeError(f"gọi model thất bại sau {self.retries} lần: {last}")

    def chat_json(self, messages, **kw):
        txt = self.chat(messages, json_out=True, **kw)
        try: return extract_json(txt)
        except ValueError:
            txt = self.chat(messages + [{"role": "assistant", "content": txt}, {"role": "user", "content": "Chỉ trả đúng một khối JSON hợp lệ, không thêm chữ nào khác."}], json_out=True, **kw)
            return extract_json(txt)
