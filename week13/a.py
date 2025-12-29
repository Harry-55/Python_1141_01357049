import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("NVDA", start="2025-01-01", end="2025-12-01", auto_adjust=True)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
date = df.index

ax1.plot(date, df['Close'].squeeze(), color='blue')
ax1.set_title('NVIDIA (NVDA) Close Price in 2025')
ax1.set_ylabel('Close Price (USD)')
ax1.grid(True)

ax2.bar(date, df['Volume'].squeeze(), color='orange')
ax2.set_title('NVIDIA (NVDA) Volume in 2025')
ax2.set_ylabel('Volume')
ax2.grid(True)

plt.xlabel('Date')
plt.show()
