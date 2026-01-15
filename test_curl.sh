#!/bin/bash

# MCP Server Test Curl Commands for Postman
# Server running on http://localhost:8000

# Test 1: Initialize the MCP session (if required)
echo "=== Test 1: Initialize Session ==="
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": {
        "name": "postman-test",
        "version": "1.0.0"
      }
    }
  }'

echo -e "\n\n=== Test 2: List Available Tools ==="
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list"
  }'

echo -e "\n\n=== Test 3: Call get_ingredient_nutrition_profile_tool with 'whole milk' ==="
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
        "query": "whole milk"
      }
    }
  }'

echo -e "\n\n=== Test 4: Call get_ingredient_nutrition_profile_tool with 'apple' ==="
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
        "query": "apple"
      }
    }
  }'

