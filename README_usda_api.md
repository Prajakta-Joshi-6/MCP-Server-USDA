# USDA API Nutrition Tool

A Python tool for fetching nutrition profiles for ingredients from the USDA FoodData Central API. Features intelligent ingredient mapping logic to find the best generic (non-branded) nutrition data.

## Features

- **Smart Ingredient Matching**: Advanced relevance scoring algorithm that prioritizes generic ingredients over branded products
- **Generic Foods Only**: Automatically filters out branded products and prioritizes Foundation, SR Legacy, and Survey data types
- **Standardized Output**: Returns nutrition data per 100 grams (standard USDA reference serving size)
- **Intelligent Filtering**: Avoids processed/compound foods when searching for base ingredients (e.g., finds "whole milk" not "cheese crackers")

## Requirements

- Python 3.7+
- `requests` library
- `python-dotenv` (optional, only needed if using `.env` file for API key)

## Installation

```bash
pip install requests python-dotenv
```

## USDA API Key

You can provide the API key in two ways:
1. **Environment variable**: Set `USDA_API_KEY` in your environment or `.env` file
2. **Function parameter**: Pass `api_key` directly to functions

## Usage

### As a Python Module

```python
from usda_api import get_ingredient_nutrition_profile

# Get nutrition profile for an ingredient
profile = get_ingredient_nutrition_profile("whole milk")

# With explicit API key
profile = get_ingredient_nutrition_profile("apple", api_key="your_api_key_here")

if profile:
    print(f"Ingredient: {profile['ingredientName']}")
    print(f"Serving Size: {profile['servingSize']} {profile['servingSizeUnit']}")
    print(f"Nutrients: {len(profile['nutrients'])}")
    
    # Access nutrients
    for nutrient in profile['nutrients']:
        print(f"{nutrient['nutrientName']}: {nutrient['value']} {nutrient['unitName']}")
```

### As a Standalone Script

```bash
python usda_api.py
```

The script will prompt you for an ingredient name and display the nutrition profile. Results are automatically saved to a JSON file.

## Available Functions

### `get_ingredient_nutrition_profile(query, api_key=None)`

Get generic nutrition profile for an ingredient. Returns a dictionary with:
- `ingredientName`: Name of the ingredient
- `description`: Full description
- `fdcId`: Food Data Central ID
- `dataType`: Data source type (Foundation, SR Legacy, or Survey)
- `foodCategory`: Food category
- `servingSize`: 100 (standard serving size)
- `servingSizeUnit`: "g" (grams)
- `nutrients`: List of all nutrients with values, units, and daily values

Returns `None` if no matching ingredient is found.

### `search_foods(query, api_key=None, data_type=None)`

Search foods in the USDA FoodData Central API. Returns raw API response.

### `extract_ingredient_info(api_response)`

Extract essential ingredient information from USDA API response.

### `get_ingredient_info(query, api_key=None)`

Search for foods and extract essential ingredient information.

## Example Output

```json
{
  "ingredientName": "Milk, whole, 3.25% milkfat",
  "description": "Milk, whole, 3.25% milkfat",
  "fdcId": 171265,
  "dataType": "Foundation",
  "foodCategory": {"description": "Dairy and Egg Products"},
  "servingSize": 100,
  "servingSizeUnit": "g",
  "nutrients": [
    {
      "nutrientId": 1008,
      "nutrientName": "Energy",
      "value": 61,
      "unitName": "KCAL",
      "percentDailyValue": null,
      "rank": 100
    },
    ...
  ]
}
```

## How the Ingredient Mapping Works

The script uses an intelligent relevance scoring system that:

1. **Prioritizes Generic Foods**: Filters for Foundation, SR Legacy, and Survey data types (excludes Branded products)
2. **Exact Match Bonus**: Gives highest scores to exact matches
3. **Position Weighting**: Earlier results from the API (which are already ranked by relevance) get higher scores
4. **Compound Food Filtering**: Penalizes processed/compound foods when searching for base ingredients
5. **Data Type Priority**: Foundation > SR Legacy > Survey > others

This ensures you get the most relevant generic ingredient data, not branded products or processed foods.

## License

This script is provided as-is for fetching nutrition data from the USDA FoodData Central API.

