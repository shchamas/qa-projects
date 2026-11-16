# QA Testing Projects
Manual and API and Automation QA Testing Projects

Hi, I'm Sam Chamas. I'm learning Manual, API and Automation QA.

Currently practicing on SauceDemo and building test cases, bug reports, and automation.

## Skills
- Manual Testing, Test Cases, Bug Reports
- API Testing with Postman
- Automation with Playwright
- Chrome DevTools

## Projects
1. SauceDemo - Login, Cart and Checkout
2. The Internet - Broken Images and Login
3. JSONPlaceholder - API Testing with Postman
4. SauceDemo - Automation with Playwright + Python

## Project 1: SauceDemo - Manual Testing

**Tested App:** https://www.saucedemo.com
**Date:** Nov 13, 2026
**Environment:** Chrome on Desktop + Safari on iPhone

### Results
- **Total Tests:** 11
- **PASS:** 7 (Test 1, 2, 3, 6, 9, 10, 11)
- **FAIL:** 3 (Test 4, 7, 8)
- **N/A:** 1 (Test 5 - Blocked by Test 4)

### Bugs Found: 3
1. **Bug 1 - No Search Functionality** - Medium
2. **Bug 2 - No Quantity Selection** - Low
3. **Bug 3 - Checkout Allowed With Empty Cart** - HIGH

### Files
- `manual-testing/test-cases.md` - All 11 test cases with steps + results
- `manual-testing/bug-reports.md` - All 3 bugs with steps + screenshots
- `manual-testing/*.png` - Screenshots as proof of concept

## Project 2: The Internet - Manual Testing

**Tested App:** https://the-internet.herokuapp.com
**Date:** Nov 14, 2026
**Environment:** Chrome on Desktop + Safari on iPhone

### Results
- **Total Tests:** 5
- **PASS:** 4 (Test 2, 3, 4, 5)
- **FAIL:** 1 (Test 1 - Broken Images)

### Bugs Found: 1
1. **Bug 1 - 2 Broken Images on Broken Images Page** - Medium

### Files
- `manual-testing-project2/test-cases.md` - All 5 test cases with steps + results
- `manual-testing-project2/bug-reports.md` - Bug with steps + screenshot
- `manual-testing-project2/*.png` - Screenshots as proof of concept

## Project 3: JSONPlaceholder - API Testing with Postman

**Tested API:** https://jsonplaceholder.typicode.com
**Date:** Nov 14, 2026
**Environment:** Postman on Desktop

### Results
- **Total Tests:** 6
- **PASS:** 6 (Test 1, 2, 3, 4, 5, 6)
- **FAIL:** 0

### What Was Tested
- GET All Posts - 200 OK
- GET Single Post - 200 OK
- GET Invalid Post - 404 Not Found (Negative Test)
- POST Create Post - 201 Created, id: 101
- PUT Update Post - 200 OK
- DELETE Post - 200 OK

### Files
- `api-testing/postman-tests.md` - All 6 test cases with steps + results
- `api-testing/api-testing-project1/*.png` - Screenshots as proof of concept

## Project 4: SauceDemo - Automation with Playwright + Python

**Tested App:** https://www.saucedemo.com
**Date:** Nov 16, 2026
**Environment:** Playwright + Python + Pytest on Chrome

### Results
- **Total Tests:** 6
- **PASS:** 6 (Test 1, 2, 3, 4, 5, 6)
- **FAIL:** 0

### What Was Tested
- Test 1 - Valid Login - Goes to Products page
- Test 2 - Invalid Password - Shows error message
- Test 3 - Locked Out User - Shows locked out error
- Test 4 - Empty Login - Shows username required error
- Test 5 - Add to Cart - Cart badge shows 1, item in cart
- Test 6 - Complete Checkout - Full flow to Thank you for your order

### How To Run
- python -m pytest automation/test_login.py -v

### Files
- `automation/test_login.py` - All 6 automated tests
