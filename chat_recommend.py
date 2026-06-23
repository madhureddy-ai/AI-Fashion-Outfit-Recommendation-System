import pandas as pd

products_df = pd.read_csv("products.csv")
outfits_df = pd.read_csv("outfits.csv")

gender = input("Gender (men/women): ").lower()
occasion = input("Occasion (office/party/casual): ").lower()

result = outfits_df[
    (outfits_df["gender"] == gender)
    &
    (outfits_df["occasion"] == occasion)
]

if len(result) > 0:

    outfit = result.sample(1).iloc[0]

    print("\n===== RECOMMENDED OUTFIT =====")

    print("\nTopwear:")
    print(outfit["hero"])

    print("\nBottomwear:")
    print(outfit["second"])

    print("\nFootwear:")
    print(outfit["footwear"])

    print("\nAccessory:")
    print(outfit["accessory_1"])

    print("\nReason:")
    print(outfit["stylist_rationale"])

else:
    print("No outfit found.")