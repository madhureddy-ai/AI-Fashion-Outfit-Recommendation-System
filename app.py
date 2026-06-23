import streamlit as st
import pandas as pd

# Load datasets
products_df = pd.read_csv("products.csv")
outfits_df = pd.read_csv("outfits.csv")

# Title
st.title("AI Fashion Outfit Recommendation System")
st.write(
    "AI-powered Fashion Assistant that recommends complete outfits based on user profile and occasion."
)

st.divider()

# Inputs
gender = st.selectbox(
    "Gender",
    ["men", "women"]
)

occasion = st.selectbox(
    "Occasion",
    outfits_df["occasion"].dropna().unique()
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=24
)

style = st.selectbox(
    "Style Preference",
    ["Formal", "Casual", "Party", "Sports"]
)

user_query = st.text_input(
    "Ask Naturally",
    placeholder="I need an outfit for business meeting"
)

# Button
if st.button("Recommend Outfit"):

    # Natural language understanding
    if user_query:

        query = user_query.lower()

        if "meeting" in query or "office" in query or "interview" in query:
            occasion = "office"

        elif "party" in query:
            occasion = "party"

        elif "wedding" in query:
            occasion = "wedding"

        elif "casual" in query:
            occasion = "casual"

        elif "sports" in query or "gym" in query:
            occasion = "sports"

    result = outfits_df[
        (outfits_df["gender"] == gender)
        &
        (outfits_df["occasion"] == occasion)
    ]

    if len(result) > 0:

        outfit = result.sample(1).iloc[0]

        # Topwear
        st.subheader("👕 Topwear")
        st.write(outfit["hero"])

        hero_product = products_df[
            products_df["id"] == outfit["hero_id"]
        ]

        if not hero_product.empty:
            st.image(hero_product.iloc[0]["image"], width=250)

        # Bottomwear
        st.subheader("👖 Bottomwear")
        st.write(outfit["second"])

        second_product = products_df[
            products_df["id"] == outfit["second_id"]
        ]

        if not second_product.empty:
            st.image(second_product.iloc[0]["image"], width=250)

        # Footwear
        st.subheader("👟 Footwear")
        st.write(outfit["footwear"])

        footwear_product = products_df[
            products_df["id"] == outfit["footwear_id"]
        ]

        if not footwear_product.empty:
            st.image(footwear_product.iloc[0]["image"], width=250)

        # Accessory
        st.subheader("⌚ Accessory")
        st.write(outfit["accessory_1"])

        if pd.notna(outfit["accessory_1_id"]):

            accessory_product = products_df[
                products_df["id"] == outfit["accessory_1_id"]
            ]

            if not accessory_product.empty:
                st.image(accessory_product.iloc[0]["image"], width=250)

        # Reason
        st.subheader("💡 Reason")
        st.success(outfit["stylist_rationale"])

    else:
        st.error("No outfit found.")