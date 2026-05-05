
import pandas as pd
import numpy as np

# ── 1. Load raw data ──────────────────────────────────────
df = pd.read_csv("amazon.csv")
print(f"Raw data: {df.shape[0]} rows, {df.shape[1]} columns")
print(df.dtypes)

# ── 2. Keep only useful columns ───────────────────────────
cols = [
    "product_id", "product_name", "category",
    "discounted_price", "actual_price",
    "discount_percentage", "rating", "rating_count"
]
df = df[cols].copy()

# ── 3. Clean price columns (remove ₹ and commas) ─────────
def clean_price(col):
    return (
        col.astype(str)
           .str.replace("₹", "", regex=False)
           .str.replace(",", "", regex=False)
           .str.strip()
    )

df["discounted_price"] = pd.to_numeric(
    clean_price(df["discounted_price"]), errors="coerce"
)
df["actual_price"] = pd.to_numeric(
    clean_price(df["actual_price"]), errors="coerce"
)

# ── 4. Clean discount % ───────────────────────────────────
df["discount_pct"] = (
    df["discount_percentage"]
      .astype(str)
      .str.replace("%", "", regex=False)
      .str.strip()
)
df["discount_pct"] = pd.to_numeric(df["discount_pct"], errors="coerce")

# ── 5. Clean rating & rating count ───────────────────────
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["rating_count"] = (
    df["rating_count"]
      .astype(str)
      .str.replace(",", "", regex=False)
)
df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")

# ── 6. Extract main category (before first |) ─────────────
df["main_category"] = df["category"].str.split("|").str[0].str.strip()

# ── 7. Calculate savings amount ───────────────────────────
df["savings"] = df["actual_price"] - df["discounted_price"]

# ── 8. Drop rows with missing prices ─────────────────────
df = df.dropna(subset=["discounted_price", "actual_price"])

# ── 9. Remove obvious bad data ────────────────────────────
df = df[df["actual_price"] > 0]
df = df[df["discounted_price"] > 0]
df = df[df["discounted_price"] <= df["actual_price"]]

# ── 10. Shorten product name for display ─────────────────
df["product_short"] = df["product_name"].str[:60]

print(f"\nClean data: {df.shape[0]} rows")
print(df.head())
print("\nNull counts:\n", df.isnull().sum())

# ── 11. Save clean data ───────────────────────────────────
import os
os.makedirs("outputs", exist_ok=True)

df.to_csv("outputs/clean_data.csv", index=False)
print("\nSaved: outputs/clean_data.csv")

