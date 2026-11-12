# Test Cases - SauceDemo

## Test 1: Login valid
- **Steps:**
1. Go to saucedemo.com
2. Login: standard_user / secret_sauce
- **Expected:** Products page shows
- **Actual:** Products page displayed with 6 products, Sauce Labs Backpack, Bike Light, Bolt T-Shirt, etc. URL changed to inventory.html
- **Result:** PASS
- **Screenshot:** ![Test 1 - Login Pass](test1-login-pass-saucedemo.png)


## Test 2: Add to Cart
- **Steps:**
1. Go to saucedemo.com
2. Login: standard_user / secret_sauce
3. Click Add to Cart on 1 product
- **Expected:** Cart icon shows 1
- **Actual:** Cart icon shows 1
- **Result:** PASS

## Test 3: Login Wrong Password
- **Steps:**
1. Go to saucedemo.com
2. Login: standard_user / wrong
3. Click Login
- **Expected:** Show error message
- **Actual:** the_error
- **Result:** PASS_or_FAIL
