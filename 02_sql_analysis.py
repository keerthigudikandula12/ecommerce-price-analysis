
import pandas as pd
import sqlite3

# Load the clean CSV we saved in Step 1
df = pd.read_csv("outputs/clean_data.csv")

# Create a SQLite database file
conn = sqlite3.connect("outputs/price_tracker.db")

# Load the dataframe INTO the database as a table called "products"
df.to_sql("products", conn, if_exists="replace", index=False)
print("Loaded into SQLite!")

# Helper function — runs any SQL query and prints the result
def run(label, sql):
    result = pd.read_sql_query(sql, conn)
    print(f"\n{'='*45}")
    print(f"  {label}")
    print('='*45)
    print(result.to_string(index=False))
    return result


q1 = run("Avg discount % by category", """
    SELECT
        main_category,
        ROUND(AVG(discount_pct), 1) AS avg_discount_pct,
        COUNT(*) AS product_count
    FROM products
    GROUP BY main_category
    ORDER BY avg_discount_pct DESC
    LIMIT 10
""")


q2 = run("Top 10 products by savings", """
    SELECT
        product_short,
        main_category,
        actual_price,
        discounted_price,
        ROUND(savings, 0) AS savings_inr,
        discount_pct
    FROM products
    ORDER BY savings DESC
    LIMIT 10
""")

q3 = run("Product count by price range", """
    SELECT
        CASE
            WHEN discounted_price < 500   THEN 'Under 500'
            WHEN discounted_price < 1000  THEN '500-1000'
            WHEN discounted_price < 5000  THEN '1000-5000'
            WHEN discounted_price < 10000 THEN '5000-10000'
            ELSE 'Above 10000'
        END AS price_bucket,
        COUNT(*) AS products,
        ROUND(AVG(discount_pct), 1) AS avg_discount
    FROM products
    GROUP BY price_bucket
    ORDER BY MIN(discounted_price)
""")

q4 = run("Value traps — high discount, low rating", """
    SELECT
        product_short,
        main_category,
        ROUND(discount_pct, 0) AS discount_pct,
        rating,
        rating_count
    FROM products
    WHERE discount_pct >= 50
      AND rating < 3.5
      AND rating_count > 100
    ORDER BY discount_pct DESC
    LIMIT 10
""")

q5 = run("Best value products", """
    SELECT
        product_short,
        main_category,
        discounted_price,
        ROUND(discount_pct, 0) AS discount_pct,
        rating,
        rating_count
    FROM products
    WHERE discount_pct >= 40
      AND rating >= 4.0
      AND rating_count >= 500
    ORDER BY rating DESC, discount_pct DESC
    LIMIT 10
""")

# Save all query results so Step 4 (Excel) can use them
import pickle

results = {
    "avg_discount_by_cat": q1,
    "top_savings":         q2,
    "price_buckets":       q3,
    "value_traps":         q4,
    "best_value":          q5,
}

with open("outputs/sql_results.pkl", "wb") as f:
    pickle.dump(results, f)

conn.close()
print("All queries done. Results saved.")