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

- Step A4, status codes when the other user reads, changes and deletes: read 404, change 400, delete 400.

## Part B

1. API tests can find problems between parts, like the load balancer sending a login to the wrong server, or the server crashing with 500. Unit tests with stubs are still useful because they are faster, do not need the network, and show exactly which function is wrong.

2. Ratings made with the public token are shared, so other students could change them during my test. In Project 2, each test will create its own data and only change or delete that data.

3. QuickPizza has several servers, and each one keeps its own users, so the session keeps the AWSALB cookie to stay on the same server. Without a session, all three of my runs failed with 401 at login.

4. The "all 3 tools excluded" block. A 500 with an empty body gives the app nothing to show, while a 400 with a message says what was wrong. The test stays as xfail so the defect stays visible, and strict=True tells me when it is fixed.

5. Base choice needs 1 + 2 + 3 + 1 + 2 = 9 tests.
All combinations need 3 x 4 x 2 x 3 = 72 tests.

6. Read gave 404, change gave 400, and delete gave 400. I expected 403 or 404 for all three. It is not a security defect because the rating did not change, but 400 is misleading because the request was valid.

7. It returned 200 with 50 ratings of the shared default user instead of 401. This is a defect, because on a real system a stranger could use another user's data without logging in.

8. An API test checks status codes, error messages and data rules faster than a web page test. Only a web page test can check what the user actually sees on the screen.