# ✅ Predicting next day's regime (multi-regime setup)
predicted_next = []

for t in range(len(hidden_states) - 1):
    current_state = hidden_states[t]
    next_probs = model.transmat_[current_state]
    next_state_pred = np.argmax(next_probs)
    # Re-map according to sorted volatility order
    next_state_remapped = remap[next_state_pred]
    predicted_next.append(next_state_remapped)

predicted_next = [np.nan] + predicted_next  # Time alignment
data['Predicted_Regime'] = predicted_next

# ✅ Position signal: +1 = long (regime 0), 0 = cash (regime 1), -1 = short (regime 2)
position = data['Predicted_Regime'].map({0: 1, 1: 0, 2: -1})
data['Position'] = position

# ✅ Compute strategy returns
data['Strategy_Multi'] = data['Log_Returns'] * data['Position']
data['Cumulative_Multi'] = (1 + data['Strategy_Multi']).cumprod()
data['Cumulative_BH'] = (1 + data['Log_Returns']).cumprod()

# ✅ Performance visualization
plt.figure(figsize=(14, 6))
plt.plot(data.index, data['Cumulative_BH'], label='Buy & Hold (S&P 500)', linestyle='--', color='gray')
plt.plot(data.index, data['Cumulative_Multi'], label='HMM Multi-Regime Strategy', color='purple')
plt.title("Cumulative Performance: Multi-Regime HMM Strategy vs Buy & Hold")
plt.ylabel("Capital (base 1)")
plt.xlabel("Date")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ Annualized performance summary
perf = data[['Strategy_Multi', 'Log_Returns']].dropna()

mean_multi = perf['Strategy_Multi'].mean() * 252
vol_multi = perf['Strategy_Multi'].std() * np.sqrt(252)
sharpe_multi = mean_multi / vol_multi

mean_bh = perf['Log_Returns'].mean() * 252
vol_bh = perf['Log_Returns'].std() * np.sqrt(252)
sharpe_bh = mean_bh / vol_bh

print("\n📊 Annualized Performance:")
print(f"Multi-Regime Strategy : Return = {mean_multi:.2%}, Volatility = {vol_multi:.2f}, Sharpe = {sharpe_multi:.2f}")
print(f"Buy & Hold            : Return = {mean_bh:.2%}, Volatility = {vol_bh:.2f}, Sharpe = {sharpe_bh:.2f}")
