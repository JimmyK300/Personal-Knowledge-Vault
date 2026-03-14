# Offline local AI model (Mac Pro Intel, 16GB) — best pick + test plan

## Goal

One offline model that is _as competent as possible_ for math + coding + general Q&A, while staying cheap (no API spend) and runnable on this machine.

## Best pick (open-source license)

### Chat / math / coding

**Qwen2.5-14B-Instruct (Apache-2.0)** in **GGUF** quant **`Q4_K_M`**.

Why this is the default:

- Strong instruction-following for its size.
- Apache-2.0 (actual open-source license).
- 14B is a noticeable step up from 7B for reasoning/coding _if you can tolerate speed_.

Reality check for this hardware:

- On CPU-only, 14B may be slow (often a few tok/s). It’s still the best _quality-per-dollar offline_ option within 16GB.
- If it’s too slow, drop to the fallback model below.

### Fallback (if 14B feels too slow)

**Qwen2.5-7B-Instruct (Apache-2.0)** GGUF **`Q5_K_M`** or **`Q6_K`**.

This is usually the best “fast enough, still smart” choice on 16GB.

## If you want to try 3 models (your shortlist)

You said you want to try:

1. **Qwen2.5-7B-Instruct** (Apache-2.0)

- Start with: **GGUF `Q5_K_M`** (best balance)
- If it’s stable + you want a bit more accuracy: **`Q6_K`**

2. **Phi-4-mini-instruct** (MIT, ~3.8B)

- Start with: **GGUF `Q6_K`** (you already ran a 3.8B model at `Q6_K` / 4096 ctx, so this is a good default)
- If you need more speed: **`Q4_K_M`**

3. **Qwen3.5**

- If you mean the official release: **Qwen3.5-9B (Apache-2.0)**
  - Start with: **GGUF `Q4_K_M`**
  - Run it as **text-only** if your runner supports it (the base checkpoint includes a vision encoder; text-only saves memory)
  - Note: some “Instruct” pages for Qwen3.5 can be access-gated on Hugging Face; if you hit that, stick to **Qwen3.5-9B** or use whatever GGUF your runner can actually download.

Common settings for fair comparison:

- Context length: **4096**
- Temperature: **0.2–0.7**
- Max output: start around **512–2048** (avoid huge outputs during speed tests)

### What to record (so the comparison is real)

For each model/quant, capture:

- **tok/s** (generation speed)
- **time-to-first-token** (subjective is fine)
- **RAM + swap** (does macOS start swapping / UI lag?)
- **math correctness** on prompts (1)–(3)

### How to export `llmfit` results (copy/paste friendly)

`llmfit` cares about **available RAM**, not just total. If it says you only have ~3–4GB available, 7B/9B models may show as “Too Tight” even though you have 16GB installed.

1. Check available RAM:

- `llmfit system`

2. Important: `--max-context` is a **global flag**, so it goes _before_ the subcommand:

- ✅ `llmfit --max-context 4096 fit --cli`
- ✅ `llmfit --max-context 4096 fit --json > /tmp/llmfit_fit.json`
- ❌ `llmfit fit --max-context 4096 ...`

3. If you saved JSON, you can grep it or parse it (macOS usually has `python3`):

- `python3 -c 'import json; d=json.load(open("/tmp/llmfit_fit.json")); print([m for m in d["models"] if m["name"] in {"Qwen/Qwen2.5-7B-Instruct","Qwen/Qwen3.5-9B"}])'`

Template (paste into your daily note):

- Model:
- Quant:
- Ctx:
- tok/s:
- Swap? (Y/N):
- Notes: (math mistakes? good debugging? etc)

## What about a “3.5” model (smaller ~3–4B models)?

If by “3.5” you mean something like **Phi-4-mini-instruct (~3.8B, MIT)** / **Phi-3.5-mini-instruct (~3.8B, MIT)** (or any ~3–4B instruct model):

- **Yes, it’s faster and more lightweight** than 7B/14B (often _much_ faster on CPU).
- **No, it’s usually not the same caliber** on hard math/coding/reasoning. Smaller models tend to:
  - make more subtle algebra/shape mistakes,
  - get lost in multi-step proofs,
  - be less reliable at debugging or writing longer code correctly.

Two important points:

- **“Latest” doesn’t mean “best for your tasks.”** Newer small models can beat older small models, but size still matters a lot for difficult reasoning.
- **Quantization doesn’t make a model more intelligent.** Quantization mostly trades accuracy for speed/RAM. A higher-quality base model (7B/14B) quantized to Q4 often still beats a smaller model at similar speed.

When a ~3–4B model _is_ the best choice:

- You care more about **responsiveness** than peak correctness (e.g., quick Q&A, drafting, light code).
- You don’t want to wait for 14B.

If you want a speed-first baseline to compare against, add one more candidate to the A/B test:

- **Phi-4-mini-instruct** (MIT) GGUF **`Q4_K_M`** (best lightweight pick)
- If you can’t find a good GGUF for Phi-4 on your runner yet: **Phi-3.5-mini-instruct** GGUF **`Q4_K_M`** (fallback lightweight baseline)

## Runner (how to run locally)

### Option A — LM Studio (fastest to start)

- Install LM Studio.
- Download the GGUF for the model (start with `Q4_K_M` for 14B, or `Q6_K` for 7B).
- In settings:
  - Context length: start at **4096**
  - Temperature: **0.2–0.7**
  - Top-p: **0.9** (if exposed)

## How to decide if it’s ‘the best’ for you (test plan)

Run the same prompts for each candidate (14B Q4 vs 7B Q6) and score:

- **Correctness** (does it make math mistakes?)
- **Usefulness** (does it structure the answer well?)
- **Honesty** (does it admit uncertainty vs inventing?)
- **Speed** (tok/s + does your Mac start swapping memory?)

### Prompt set (copy/paste)

**Math (concept + derivation)**

1. “Derive the gradient of logistic regression binary cross-entropy loss w.r.t. weights. Keep shapes explicit.”
2. “Explain eigenvalues/eigenvectors with one geometric example and one computation example.”
3. “Show a clean proof that the sum of two independent Gaussians is Gaussian.”

**Coding (write + debug)** 4. “Write Python code: implement a numerically-stable softmax and cross-entropy (vectorized). Add a quick test.” 5. “Here is a bug: [paste a short snippet from one of your scripts]. Find the bug and fix it. Explain briefly.”

**Reasoning (planning + questions)** 6. “Before answering, ask me 5 clarifying questions: I want a 2-week plan to learn CNNs and backprop deeply.”

**Your vault (realistic)** 7. Paste ~150–400 lines from a note (e.g., a CNN/backprop note) and ask:

- “Summarize into 7 bullets.”
- “Extract a study checklist.”
- “Generate 10 Anki Q/A cards.”

### Pass/fail thresholds (simple)

- If the 14B model is **< ~1–2 tok/s** and feels painful: switch to **7B Q6**.
- If the 7B model makes repeated math errors on prompts (1)–(3): tolerate 14B, or increase quant (Q5) if RAM allows.

## Notes on ‘best’ models that are _not_ open-source

Some very strong models are “open weights” but not OSI open-source (license restrictions). If you’re OK with that, the best single-model experience often comes from Llama-family instruct models.

If you want, decide first: do you require OSI open-source licensing, or is “free-ish open weights” OK?
