from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    symbol = data.get("symbol")
    timeframe = data.get("timeframe", "15m")
    o = data.get("open")
    h = data.get("high")
    l = data.get("low")
    c = data.get("close")
    v = data.get("volume")

    resumen = f"""
Analyze this setup:
Symbol: {symbol}
Timeframe: {timeframe}
Open: {o}
High: {h}
Low: {l}
Close: {c}
Volume: {v}
"""
    print(resumen)
    return {"message": resumen}
