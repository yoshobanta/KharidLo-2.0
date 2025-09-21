import streamlit as st
from collections import defaultdict

# -------------------------------
# Kharidlo Shop Class
# -------------------------------
class Kharidlo:
    shop_name = "Kharidlo_2.0"
    owner = "Yosho"
    mbl = "RKL"
    contact = 9876543210

    # Shared stock among all users
    stock = {
        'iphone 15': 15,
        'iphone 15 pro': 10,
        'iphone 15 pro max': 5,
        'samsung s24 ultra': 8,
        'pixel 9': 12,
        'oneplus 12': 20,
    }

    price = {
        'iphone 15': 52458,
        'iphone 15 pro': 61523,
        'iphone 15 pro max': 70114,
        'samsung s24 ultra': 89999,
        'pixel 9': 69999,
        'oneplus 12': 55999,
    }

    discount = {
        'iphone 15': 15.0,
        'iphone 15 pro': 10.0,
        'iphone 15 pro max': 5.0,
        'samsung s24 ultra': 7.5,
        'pixel 9': 12.0,
        'oneplus 12': 8.0,
    }

    def __init__(self, name, add, pno):
        self.name = name
        self.add = add
        self.pno = pno
        self.cart = defaultdict(int)

    # Add item to cart
    def add_item(self, item, q=1):
        if item in Kharidlo.stock:
            if Kharidlo.stock[item] >= q:
                self.cart[item] += q
                Kharidlo.stock[item] -= q
                return f"✅ {q} x {item} added to cart."
            else:
                return f"⚠️ Only {Kharidlo.stock[item]} unit(s) available."
        else:
            return f"❌ {item} is not sold here."

    # Remove item from cart
    def remove_item(self, item, q=1):
        if item in self.cart:
            if self.cart[item] >= q:
                self.cart[item] -= q
                Kharidlo.stock[item] += q
                if self.cart[item] == 0:
                    self.cart.pop(item)
                return f"🗑️ {q} x {item} removed from cart."
            else:
                return f"⚠️ You only have {self.cart[item]} of {item} in cart."
        else:
            return f"❌ {item} not in your cart."

    # Clear cart
    def clear_cart(self):
        for item, q in self.cart.items():
            Kharidlo.stock[item] += q
        self.cart.clear()
        return "🛒 Cart cleared."

    # Display cart
    def display_cart(self):
        if not self.cart:
            return None, "Cart is empty"
        cart_items = []
        total = 0
        discount_total = 0
        for item, q in self.cart.items():
            price = Kharidlo.price[item] * q
            disc = (price * Kharidlo.discount[item]) / 100
            final_price = price - disc
            cart_items.append([item, q, Kharidlo.price[item], Kharidlo.discount[item], final_price])
            total += price
            discount_total += disc
        return cart_items, f"💰 Total: ₹{total - discount_total} (Saved ₹{discount_total})"

    # Checkout
    def checkout(self):
        if not self.cart:
            return "❌ Cart is empty."
        # Make a copy of cart before clearing
        purchased_cart = dict(self.cart)

        # Append to session state sales_history
        if "sales_history" not in st.session_state:
            st.session_state.sales_history = []
        st.session_state.sales_history.append({
            "customer": self.name,
            "cart": purchased_cart
        })

        # Clear cart
        self.cart.clear()

        # Return summary
        cart_items, summary = self.display_cart_after_purchase(purchased_cart)
        return f"✅ Checkout successful!\n{summary}"

    # Helper to display purchased cart summary
    def display_cart_after_purchase(self, purchased_cart):
        cart_items = []
        total = 0
        discount_total = 0
        for item, q in purchased_cart.items():
            price = Kharidlo.price[item] * q
            disc = (price * Kharidlo.discount[item]) / 100
            final_price = price - disc
            cart_items.append([item, q, Kharidlo.price[item], Kharidlo.discount[item], final_price])
            total += price
            discount_total += disc
        return cart_items, f"💰 Total: ₹{total - discount_total} (Saved ₹{discount_total})"

# -------------------------------
# Streamlit App Setup
# -------------------------------
st.title("🛒 Welcome to Kharidlo 2.0")

# Session state initialization
if "customers" not in st.session_state:
    st.session_state.customers = {}

if "current_customer" not in st.session_state:
    st.session_state.current_customer = None

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

if "sales_history" not in st.session_state:
    st.session_state.sales_history = []

# -------------------------------
# Sidebar Menu
# -------------------------------
if st.session_state.is_admin:
    menu = st.sidebar.radio("Menu", ["Admin Dashboard", "Logout Admin"])
else:
    menu = st.sidebar.radio("Menu", ["Login / Signup", "Shop", "Cart", "Checkout", "Admin Login"])

# -------------------------------
# Customer Login / Signup
# -------------------------------
if menu == "Login / Signup":
    st.header("👤 Customer Login / Signup")
    name = st.text_input("Enter your name")
    add = st.text_input("Enter your address")
    pno = st.text_input("Enter your phone number")
    if st.button("Login / Signup"):
        if name not in st.session_state.customers:
            st.session_state.customers[name] = Kharidlo(name, add, pno)
            st.success(f"✅ New account created for {name}")
        else:
            st.info(f"🔑 Welcome back, {name}")
        st.session_state.current_customer = st.session_state.customers[name]

# -------------------------------
# Shop
# -------------------------------
elif menu == "Shop":
    if not st.session_state.current_customer:
        st.warning("⚠️ Please login first")
    else:
        st.header("🛍️ Shop Products")
        product = st.selectbox("Select a product", list(Kharidlo.stock.keys()))
        qty = st.number_input("Quantity", 1, 10, 1)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Add to Cart"):
                msg = st.session_state.current_customer.add_item(product, qty)
                st.info(msg)
        with col2:
            if st.button("Remove from Cart"):
                msg = st.session_state.current_customer.remove_item(product, qty)
                st.warning(msg)

# -------------------------------
# Cart
# -------------------------------
elif menu == "Cart":
    if not st.session_state.current_customer:
        st.warning("⚠️ Please login first")
    else:
        st.header("🛒 Your Cart")
        cart_items, summary = st.session_state.current_customer.display_cart()
        if cart_items:
            st.table(cart_items)
            st.success(summary)
            if st.button("Clear Cart"):
                st.warning(st.session_state.current_customer.clear_cart())
        else:
            st.info(summary)

# -------------------------------
# Checkout
# -------------------------------
elif menu == "Checkout":
    if not st.session_state.current_customer:
        st.warning("⚠️ Please login first")
    else:
        st.header("💳 Checkout")
        msg = st.session_state.current_customer.checkout()
        st.success(msg)

# -------------------------------
# Admin Login
# -------------------------------
elif menu == "Admin Login":
    st.header("🔒 Admin Login")
    admin_user = st.text_input("Username")
    admin_pass = st.text_input("Password", type="password")
    if st.button("Login as Admin"):
        if admin_user == "admin" and admin_pass == "yosho123":
            st.session_state.is_admin = True
            st.success("✅ Admin login successful!")
        else:
            st.error("❌ Invalid admin credentials")

# -------------------------------
# Admin Dashboard
# -------------------------------
elif menu == "Admin Dashboard":
    st.header("🛠️ Admin Dashboard")

    # Stock Table
    st.subheader("📦 Current Stock")
    stock_table = [[item, qty, Kharidlo.price[item]] for item, qty in Kharidlo.stock.items()]
    st.table(stock_table)

    # Sales History Table
    st.subheader("📊 Sales History")
    if not st.session_state.sales_history:
        st.info("No sales yet.")
    else:
        sales_data = []
        for sale in st.session_state.sales_history:
            customer = sale["customer"]
            for item, qty in sale["cart"].items():
                price = Kharidlo.price[item] * qty
                discount = (price * Kharidlo.discount[item]) / 100
                final_price = price - discount
                sales_data.append([customer, item, qty, price, discount, final_price])
        st.table(sales_data)

    # Total Revenue
    total_revenue = sum(
        (Kharidlo.price[item]*qty - (Kharidlo.price[item]*qty*Kharidlo.discount[item]/100))
        for sale in st.session_state.sales_history for item, qty in sale["cart"].items()
    )
    st.success(f"💰 Total Revenue: ₹{total_revenue:.2f}")

    # Logout button
    if st.button("Logout Admin"):
        st.session_state.is_admin = False
        st.success("Logged out from admin.")