
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import pickle, os

os.makedirs("outputs/charts", exist_ok=True)
df = pd.read_csv("outputs/clean_data.csv")
with open("outputs/sql_results.pkl", "rb") as f:
    res = pickle.load(f)

sns.set_theme(style="whitegrid", font_scale=1.05)
BLUE   = "#185FA5"
GREEN  = "#3B6D11"
ORANGE = "#BA7517"
COLORS = [BLUE, GREEN, ORANGE, "#993556", "#534AB7",
          "#0F6E56", "#A32D2D", "#5F5E5A", "#639922", "#2E86C1"]


fig, ax = plt.subplots(figsize=(10, 6))
data = res["avg_discount_by_cat"].head(10)
bars = ax.barh(data["main_category"], data["avg_discount_pct"],
               color=BLUE, edgecolor="none", height=0.6)
ax.bar_label(bars, fmt="%.1f%%", padding=4, fontsize=10, color="#333")
ax.set_xlabel("Average Discount %", fontsize=11)
ax.set_title("Which categories have the highest average discounts?",
             fontsize=13, fontweight="bold", pad=14)
ax.invert_yaxis()
ax.xaxis.set_major_formatter(mtick.PercentFormatter())
plt.tight_layout()
plt.savefig("outputs/charts/01_discount_by_category.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 1 saved")


fig, ax = plt.subplots(figsize=(12, 6))
top_cats = df["main_category"].value_counts().head(6).index
plot_df  = df[df["main_category"].isin(top_cats)]
sns.boxplot(
    data=plot_df, x="main_category", y="discounted_price",
    palette=COLORS[:6], flierprops=dict(marker=".", alpha=0.4), ax=ax
)
ax.set_yscale("log")
ax.set_xlabel("")
ax.set_ylabel("Discounted Price (log scale)", fontsize=11)
ax.set_title("Price spread by product category", fontsize=13, fontweight="bold", pad=14)
ax.tick_params(axis="x", rotation=20)
plt.tight_layout()
plt.savefig("outputs/charts/02_price_distribution.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 2 saved")


fig, ax = plt.subplots(figsize=(9, 6))
sample = df.sample(min(500, len(df)), random_state=42)
scatter = ax.scatter(
    sample["discount_pct"], sample["rating"],
    c=sample["discounted_price"], cmap="YlOrRd_r",
    alpha=0.65, s=40, edgecolors="none"
)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("Price (₹)", fontsize=10)
ax.set_xlabel("Discount %", fontsize=11)
ax.set_ylabel("Rating (out of 5)", fontsize=11)
ax.set_title("Does higher discount mean lower quality?",
             fontsize=13, fontweight="bold", pad=14)
ax.axhline(4.0, color=GREEN, linestyle="--", linewidth=1.2, label="Rating = 4.0")
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig("outputs/charts/03_rating_vs_discount.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 3 saved")

fig, ax = plt.subplots(figsize=(8, 5))
data = res["price_buckets"]
bars = ax.bar(data["price_bucket"], data["products"],
              color=COLORS[:len(data)], edgecolor="none", width=0.6)
ax.bar_label(bars, padding=4, fontsize=10)
ax.set_xlabel("Price Range", fontsize=11)
ax.set_ylabel("Number of Products", fontsize=11)
ax.set_title("How are products distributed across price ranges?",
             fontsize=13, fontweight="bold", pad=14)
ax.tick_params(axis="x", rotation=10)
plt.tight_layout()
plt.savefig("outputs/charts/04_price_buckets.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 4 saved")


fig, ax = plt.subplots(figsize=(10, 6))
data = res["top_savings"].head(10)
bars = ax.barh(
    data["product_short"].str[:45] + "...",
    data["savings_inr"],
    color=GREEN, edgecolor="none", height=0.6
)
ax.bar_label(bars, fmt="₹%.0f", padding=4, fontsize=9)
ax.set_xlabel("Money Saved (₹)", fontsize=11)
ax.set_title("Top 10 products with highest absolute savings",
             fontsize=13, fontweight="bold", pad=14)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/charts/05_top_savings.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 5 saved")
print("\nAll 5 charts saved to outputs/charts/")