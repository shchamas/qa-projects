# Test Cases - SauceDemo

## Test 1: Login valid
- **Steps:**
1. Go to saucedemo.com
2. Login: standard_user / secret_sauce
- **Expected:** Products page shows
- **Actual:** Products page displayed with 6 products, Sauce Labs Backpack, Bike Light, Bolt T-Shirt, etc. URL changed to inventory.html
- **Result:** PASS
- **Screenshot:** ![Test 1 - Login Pass](test1-login-pass-saucedemo.png)

## Test 2: Login wrong password
- **Steps:**
1. Go to saucedemo.com
2. Login: standard_user / wrong
3. Click Login
- **Expected:** Error message shows, stay on login page
- **Actual:** Red error shows "Epic sadface: Username and password do not match any user in this service"
- **Result:** PASS
- **Screenshot:** ![Test 2 - Wrong Password](test2-wrong-password-saucedemo.png)

## Test 3: Login enpty
- **Steps:**
1. Go to saucedemo.com
2. Leave username and password empty
3. Click Login
- **Expected:** Error "Username is required"
- **Actual:** Red error shows "Epic sadface: Username is required"
- **Result:** PASS
- **Screenshot:** ![Test 2 - Wrong Password](test2-wrong-password-saucedemo.png)

