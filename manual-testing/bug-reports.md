# Bug Reports

## Bug 1: No Search Functionality
- **Steps:**
1. Login with standard_user / secret_sauce
2. Go to Products page
3. Look for search bar
- **Expected:** User can search for products by name
- **Actual:** No search bar or search function exists
- **Screenshot:** ![Test 4 - Search Bar Uavailable](test4-search-bar-unavailable-saucedemo.png)
- **Environment:** Chrome, SauceDemo
- **Severity:** Medium

## Bug 2: No Quantity Selection
- **Steps:** 1. Login 2. On Products page, try to change quantity
- **Expected:** User can set quantity 0, 2, etc.
- **Actual:** No quantity field, only Add / Remove for 1 item
- **Screenshot:** ![Test 6 - No Quantity](test7-add-0-quantity-saucedemo.png)
- **Severity:** Low

## Bug 3: Checkout Allowed With Empty Cart
- **Steps:** 1. Login 2. Empty cart 3. Click Cart 4. Click Checkout
- **Expected:** System should block checkout and show "Cart is empty"
- **Actual:** System allows user to go to Checkout: Your Information page with 0 items
- **Screenshot:** ![Test 8 - Checkout - Empty](test8-checkout-empty-saucedemo.png)
- **Severity:** High - User can checkout with no products
