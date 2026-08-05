# Streaming & Structured Outputs

## 1. Streaming Tokens (Raw SDK → FastAPI SSE)
Normally an API call waits for the ENTIRE response before returning anything. **Streaming** sends each token back as it's generated — text appears progressively, like watching ChatGPT "type."

```python
for chunk in llm_stream(messages):
    print(chunk, end="", flush=True)
```
Each chunk prints immediately, no waiting for the full response.

**SSE (Server-Sent Events):** same streaming pattern, one more hop — pushes incremental updates from backend (FastAPI) to browser over a kept-open HTTP connection. LLM streams tokens to backend → backend re-streams to browser via SSE.

**Forward link:** Phase 4 (LangGraph) streams agent STEPS ("Searching... → Reading... → Drafting..."), not just tokens — same foundation.

**Simple words:** streaming = answer appears piece by piece as generated, not all at once after waiting. SSE = same "piece by piece" idea, pushed from server to browser.

**Interview answer:** "Streaming sends model output token-by-token as generated rather than waiting for the full response, improving perceived latency. SSE extends this to the browser by keeping an HTTP connection open and pushing incremental events. The same pattern extends to agent frameworks like LangGraph, which stream intermediate agent steps, not just tokens."

## 2. Structured Outputs — Pydantic Schema → Guaranteed JSON
Define a Pydantic model instead of a raw JSON schema:
```python
from pydantic import BaseModel

class WeatherAnswer(BaseModel):
    city: str
    temperature_celsius: float
    condition: str
```
Pass it to the API's structured-output feature → get back validated, typed data (`response.city`, etc.) instead of a raw string to parse manually.

**Why Pydantic specifically:** same validation tool already used at other system boundaries (Phase 1) — one consistent way to define/validate data shapes across the whole app.

**Validation failure + retry:** same pattern as tool-call error handling (Phase 2.3) — catch the validation error, feed it back to the model as context, retry. Don't crash.

**Simple words:** describe the shape you want as a Pydantic class, API enforces the response matches it — ready-to-use typed data instead of a raw string you hope is valid JSON. If it fails, tell the model what went wrong and let it retry.

**Interview answer:** "Structured outputs with Pydantic define the expected response shape as a typed class, which the API uses to constrain generation, returning validated typed data instead of a raw string. When validation fails, the recovery pattern mirrors tool-call error handling: catch the error, feed it back to the model, retry rather than crashing."
