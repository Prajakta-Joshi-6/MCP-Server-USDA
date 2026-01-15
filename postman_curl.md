# MCP Server cURL Commands for Postman

## Server Information
- **Base URL**: `http://localhost:8000`
- **Endpoint**: `/mcp`
- **Protocol**: JSON-RPC 2.0
- **Content-Type**: `application/json`
- **Accept**: `application/json, text/event-stream` (REQUIRED - both must be included)

---

## 1. List Available Tools

**Method**: POST  
**URL**: `http://localhost:8000/mcp`

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list"
  }'
```

**For Postman:**
- Method: POST
- URL: `http://localhost:8000/mcp`
- Headers:
  - `Content-Type: application/json`
  - `Accept: application/json, text/event-stream`
- Body (raw JSON):
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}
```

---

## 2. Call Tool: Get Nutrition Profile for "whole milk"

**Method**: POST  
**URL**: `http://localhost:8000/mcp`

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "get_ingredient_nutrition_profile_tool",
      "arguments": {
        "query": "whole milk"
      }
    }
  }'
```

**For Postman:**
- Method: POST
- URL: `http://localhost:8000/mcp`
- Headers:
  - `Content-Type: application/json`
  - `Accept: application/json, text/event-stream`
- Body (raw JSON):
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_ingredient_nutrition_profile_tool",
    "arguments": {
      "query": "whole milk"
    }
  }
}
```

---

## 3. Call Tool: Get Nutrition Profile for "apple"

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
      "name": "get_ingredient_nutrition_profile_tool",
      "arguments": {
        "query": "apple"
      }
    }
  }'
```

**For Postman:** Same as above, but change `"query": "apple"` in the body.

---

## 4. Call Tool: Get Nutrition Profile for "bread"

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
      "name": "get_ingredient_nutrition_profile_tool",
      "arguments": {
        "query": "bread"
      }
    }
  }'
```

---

## Quick Test Command (Copy-Paste Ready)

Test with "whole milk":

```bash
curl -X POST http://localhost:8000/mcp -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_ingredient_nutrition_profile_tool","arguments":{"query":"whole milk"}}}'
```

**IMPORTANT:** Make sure your Accept header includes both `application/json` and `text/event-stream` for FastMCP to work properly.

---

## Expected Response Format

**Success Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": {
          "ingredientName": "Milk, whole, 3.25% milkfat, with added vitamin D",
          "description": "Milk, whole, 3.25% milkfat, with added vitamin D",
          "fdcId": 171265,
          "dataType": "Foundation",
          "foodCategory": "Dairy and Egg Products",
          "servingSize": 100,
          "servingSizeUnit": "g",
          "nutrients": [...]
        }
      }
    ]
  }
}
```

**Error Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "error": {
    "code": -32602,
    "message": "Invalid params"
  }
}
```

