# API_autocomplete_system
Working of the API:
The API provides autocomplete results based on a query string (`query=a`, `query=aa`, etc.).  
Each version has different **result limits per request

API Versions with Max results per request:
v1: 10 names
v2: 12 names
v3: 15 names

To extract all names:
1. Send multiple queries ie., 'a', 'aa', 'ab', .. 'b', 'ba', etc.
2. Pagination can be used to fetch more names.
