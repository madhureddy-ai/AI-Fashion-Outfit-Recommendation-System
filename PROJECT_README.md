# AI Fashion Outfit Recommendation System

## Overview

An AI-powered Fashion Assistant that recommends complete outfits based on user profile and occasion.

## Features

* User-aware outfit recommendations
* Natural language query support
* Topwear, Bottomwear, Footwear and Accessory suggestions
* Explainable recommendations
* Streamlit-based interactive UI
* Image-based outfit display

## Inputs

* Gender
* Occasion
* Age
* Style Preference
* Natural language query

## Tech Stack

* Python
* Pandas
* Streamlit

## Architecture

User → Streamlit UI → Natural Language Parser → Recommendation Engine → Outfit Dataset → Image Retrieval → Explainability → Final Recommendation

## Run

```bash
streamlit run app.py
```

## Future Improvements

* Gemini API Integration
* CLIP/FashionCLIP embeddings
* Vector Search (FAISS/Qdrant)
* Multi-modal Retrieval
* Personalized recommendations
