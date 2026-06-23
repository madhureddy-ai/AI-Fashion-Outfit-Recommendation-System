import pandas as pd

products_df = pd.read_csv("products.csv")
outfits_df = pd.read_csv("outfits.csv")

print("\nProducts columns:")
print(products_df.columns)

print("\nOutfits columns:")
print(outfits_df.columns)

print("\nGender values:")
print(products_df["gender"].unique())

print("\nOccasions:")
print(products_df["occasion"].unique())

print("\nCategories:")
print(products_df["category_label"].unique())

print("\nWear types:")
print(products_df["wear_type"].unique())