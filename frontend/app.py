import streamlit as st
import requests

# -----------------------------
# 🎯 FastAPI Backend URL
# -----------------------------
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Ngam Je Coffee",
    page_icon="☕",
    layout="centered",
)

# -----------------------------
# 🌿 Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
        body {
            background-color: #f4efe9;
        }
        .block-container {
            max-width: 700px;
            padding-top: 2rem;
        }
        h1, h2, h3, h4 {
            color: #4b2e05 !important;
            font-family: 'Georgia', serif;
        }
        .coffee-card {
            border-radius: 15px;
            background: linear-gradient(145deg, #fffaf4, #f8f2eb);
            padding: 16px 20px;
            margin-bottom: 12px;
            box-shadow: 0 2px 5px rgba(100, 65, 35, 0.1);
        }
        .coffee-price {
            color: #8b4513;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #6f4e37;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.6rem 1.2rem;
        }
        .stButton>button:hover {
            background-color: #5a3c28;
            color: #fffbe6;
        }
        .sidebar .sidebar-content {
            background-color: #eae2d7;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# ☕ App Header
# -----------------------------
st.title("Ngam Je Coffee")
st.caption("Freshly brewed with love ❤️")

# -----------------------------
# 🔧 Helper Functions
# -----------------------------
def fetch_coffees():
    try:
        res = requests.get(f"{BASE_URL}/coffees")
        if res.status_code == 200:
            return sorted(res.json(), key=lambda x: x["price"])
        else:
            st.error("❌ Failed to fetch coffee menu.")
            return []
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        return []

def add_coffee(name, description, price):
    return requests.post(f"{BASE_URL}/coffees", json={
        "name": name, "description": description, "price": price
    })

def update_coffee(coffee_id, name, description, price):
    return requests.put(f"{BASE_URL}/coffees/{coffee_id}", json={
        "name": name, "description": description, "price": price
    })

def delete_coffee(coffee_id):
    return requests.delete(f"{BASE_URL}/coffees/{coffee_id}")

# -----------------------------
# 🎛️ Sidebar Navigation
# -----------------------------
st.sidebar.title("☕ Actions")
action = st.sidebar.radio(
    "Select an action:",
    ["View Menu", "Add Coffee", "Update Coffee", "Delete Coffee"],
)

# -----------------------------
# 📜 VIEW MENU
# -----------------------------
if action == "View Menu":
    st.subheader("Today's Menu")
    coffees = fetch_coffees()

    if not coffees:
        st.info("☕ No coffee available yet. Please add one!")
    else:
        for coffee in coffees:
            st.markdown(
                f"""
                <div class="coffee-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="margin:0;">{coffee['name']}</h4>
                        <h4 style="margin:0; color:#8b4513;">RM {coffee['price']:.2f}</h4>
                    </div>
                    <p style="color:#5c3d1e; margin-top:4px;">{coffee['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# -----------------------------
# ➕ ADD COFFEE
# -----------------------------
elif action == "Add Coffee":
    st.subheader("➕ Add New Coffee")
    name = st.text_input("Coffee Name")
    description = st.text_area("Description")
    price = st.number_input("Price (RM)", min_value=0.0, step=0.5)

    if st.button("Add Coffee ☕"):
        if name and description:
            res = add_coffee(name, description, price)
            if res.status_code == 200:
                st.success(f"✅ '{name}' added successfully!")
            else:
                st.error("❌ Failed to add coffee.")
        else:
            st.warning("Please fill in all fields.")

# -----------------------------
# ✏️ UPDATE COFFEE
# -----------------------------
elif action == "Update Coffee":
    st.subheader("✏️ Update Coffee")
    coffees = fetch_coffees()

    if coffees:
        coffee_map = {c["name"]: c for c in coffees}
        selected = st.selectbox("Select coffee to edit", list(coffee_map.keys()))
        c = coffee_map[selected]

        new_name = st.text_input("Name", c["name"])
        new_description = st.text_area("Description", c["description"])
        new_price = st.number_input("Price (RM)", value=float(c["price"]), step=0.5)

        if st.button("💾 Save Changes"):
            res = update_coffee(c["id"], new_name, new_description, new_price)
            if res.status_code == 200:
                st.success(f"✅ '{new_name}' updated successfully!")
            else:
                st.error("❌ Failed to update coffee.")
    else:
        st.info("No coffees to edit yet.")

# -----------------------------
# 🗑️ DELETE COFFEE
# -----------------------------
elif action == "Delete Coffee":
    st.subheader("🗑️ Delete Coffee")
    coffees = fetch_coffees()

    if coffees:
        coffee_map = {c["name"]: c for c in coffees}
        selected = st.selectbox("Select coffee to delete", list(coffee_map.keys()))
        c = coffee_map[selected]

        if st.button("Delete 🚫"):
            res = delete_coffee(c["id"])
            if res.status_code == 200:
                st.success(f"'{selected}' has been deleted.")
            else:
                st.error("❌ Failed to delete coffee.")
    else:
        st.info("No coffees to delete yet.")