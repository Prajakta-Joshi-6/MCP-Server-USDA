"""
MCP Server for USDA Nutrition Profile using FastMCP.
Exposes get_ingredient_nutrition_profile as an MCP tool.

Requirements:
- Python 3.10 or higher
- MCP SDK installed: pip install git+https://github.com/modelcontextprotocol/python-sdk.git
"""
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
from usda_api import get_ingredient_nutrition_profile

# Initialize FastMCP server
mcp = FastMCP("USDA Nutrition Profile Server")


@mcp.tool()
def get_ingredient_nutrition_profile_tool(query: str) -> Dict[str, Any]:
    """
    Get generic nutrition profile for an ingredient.
    
    Fetches nutrition information for a given ingredient from the USDA FoodData Central API.
    Returns generic (non-branded) nutrition data standardized per 100 grams.
    
    Args:
        query: The name of the ingredient to search for (e.g., 'whole milk', 'apple', 'bread')
        
    Returns:
        Dictionary containing:
        - ingredientName: Name of the ingredient
        - description: Full description
        - fdcId: Food Data Central ID
        - dataType: Data source type (Foundation, SR Legacy, or Survey)
        - foodCategory: Food category
        - servingSize: 100 (standard serving size)
        - servingSizeUnit: "g" (grams)
        - nutrients: List of all nutrients with values, units, and daily values
        
        If ingredient not found, returns error dictionary with error and message fields.
    """
    try:
        # Validate input
        if not query or not query.strip():
            return {
                "error": "Invalid input",
                "message": "Ingredient name cannot be empty."
            }
        
        # Call the existing function from usda_api
        nutrition_profile = get_ingredient_nutrition_profile(query.strip())
        
        # Handle case where ingredient not found
        if nutrition_profile is None:
            return {
                "error": "Ingredient not found",
                "message": f"No generic nutrition data found for '{query}'. Try a different ingredient name.",
                "query": query
            }
        
        # Ensure all values are JSON-serializable (convert None to null-equivalent)
        # The nutrition profile should already be JSON-serializable, but we'll ensure it
        return nutrition_profile
        
    except Exception as e:
        # Handle any errors that occur during API call
        return {
            "error": "API request failed",
            "message": str(e),
            "query": query if 'query' in locals() else "unknown"
        }


if __name__ == "__main__":
    # Run the MCP server with HTTP transport
    mcp.run(transport="streamable-http")

