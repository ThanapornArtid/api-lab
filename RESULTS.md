# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: {"tools":["Knife","Pizza cutter","Scissors"]}
- Step 0.4, the name of your pizza: A Scary Hawaii
- Step 0.12, results of the three runs without a session (optional): failed, failed, failed.
- Step 0.16, blocks of "how many of the three tools are excluded": 0 tools, 1 tool, 2 tools, 3 tools

# Defect report

- Title: Excluding all three tools makes POST /api/pizza answer 500 with an empty body
- Request: POST https://quickpizza.grafana.com/api/pizza with header "Authorization: token abcdef0123456789" and body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}. Reproduce with: curl -i -H "@auth.txt" -d "@all-tools.json" https://quickpizza.grafana.com/api/pizza. The same happens with the token of a newly logged-in user.
- Expected result: status 400 with a JSON error message, because no pizza can satisfy the request
- Actual result: status 500 with an empty body
- Severity: Medium. A normal customer input crashes the request and the app gets no message to show, but other requests still work.

## Part A

- Step A4, status codes when the other user reads, changes and deletes:

## Part B

1.
2.
3.
4.
5.
6.
7.
8.