# KharidLo 2.0 - E-commerce Shopping Application

**Developer:** Yoshobanta Bisoi  
**Live Demo:** [kharidlocart.streamlit.app](https://kharidlocart.streamlit.app/)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success)](https://kharidlocart.streamlit.app/)

## 🚀 About This Project

KharidLo 2.0 is a full-featured e-commerce web application developed by **Yoshobanta Bisoi** as a demonstration of Python programming, Streamlit framework expertise, and modern web development practices. This project showcases real-world shopping cart functionality, inventory management, and user authentication systems.

**Created by Yoshobanta Bisoi** to demonstrate:
- Object-oriented programming in Python
- Web application development with Streamlit
- Real-time inventory management
- Multi-user session handling
- Business logic implementation

## 👨‍💻 About the Developer

Built by **Yoshobanta Bisoi** - Python Developer

This project demonstrates expertise in:
- Python programming and data structures
- Web application development with Streamlit
- E-commerce system architecture
- Object-oriented programming
- Session state management
- User experience design

## ✨ Features

### Customer Features
- **User Registration/Login**: Simple signup process with name, address, and phone number
- **Product Browsing**: View available smartphones with real-time stock levels and pricing
- **Shopping Cart Management**: Add/remove items with automatic discount calculations
- **Checkout System**: Complete purchase process with order confirmation
- **Discount System**: Automatic price reductions on all products

### Admin Features (Developed by Yoshobanta Bisoi)
- **Stock Management**: Real-time inventory monitoring and control
- **Sales Analytics**: Comprehensive transaction history and revenue tracking
- **Business Insights**: Total earnings and discount savings analysis
- **User Activity Tracking**: Monitor all customer purchases

## 🛍️ Available Products

KharidLo 2.0 features a curated selection of smartphones:
- **iPhone 15 Series**: iPhone 15, 15 Pro, 15 Pro Max (up to 15% discount)
- **Samsung S24 Ultra**: Flagship Android device (7.5% discount)
- **Google Pixel 9**: Latest Google smartphone (12% discount)
- **OnePlus 12**: High-performance device (8% discount)

## 🔧 Technical Stack

**Built by Yoshobanta Bisoi using:**
- **Language**: Python 3.11+
- **Framework**: Streamlit
- **Architecture**: Object-Oriented Programming
- **State Management**: Streamlit Session State
- **Data Structures**: Dictionaries, defaultdict for efficient operations

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yoshobanta/KharidLo-2.0.git

# Navigate to project directory
cd KharidLo-2.0

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will launch at `http://localhost:8501`

## 🎯 How to Use

### For Customers:
1. **Sign Up**: Enter your name, address, and phone number
2. **Browse Products**: View available smartphones with prices and stock
3. **Add to Cart**: Select items and quantities
4. **Checkout**: Complete your purchase and receive confirmation

### For Admin:
- **Username**: `admin`
- **Password**: `yosho123`
- Access comprehensive dashboard for inventory and sales management

**Note**: Admin credentials are for demonstration purposes only in this project by Yoshobanta Bisoi.
## 🎓 Learning Outcomes

This project by **Yoshobanta Bisoi** demonstrates:
- ✅ Python class-based programming and OOP concepts
- ✅ Streamlit framework for rapid web app development
- ✅ Data structure optimization (dictionaries, defaultdict)
- ✅ Session state management for multi-user applications
- ✅ Business logic implementation for e-commerce
- ✅ User interface design and user experience

---

## 🔧 Technical Challenges Solved

### Problem: Sales Data Not Persisting Between User and Admin Sessions

**Challenge Faced by Yoshobanta Bisoi:**

When initially developing KharidLo 2.0, a critical issue emerged where sales transactions made by customers were not appearing in the Admin Dashboard. The problem occurred because:
- User purchases were being recorded successfully
- Stock quantities were updating correctly
- But the Admin panel always showed an empty sales history

**Root Cause:**
The `sales_history` was implemented as a class variable in the `Kharidlo` class, which was being reset when switching between user and admin views due to Streamlit's app reload behavior.

**Solution Implemented by Yoshobanta Bisoi:**

1. **Removed** the `sales_history` class variable from the `Kharidlo` class
2. **Added** `st.session_state.sales_history` initialization in the Streamlit app setup
3. **Modified** the `checkout()` method to append transactions to `st.session_state.sales_history`
4. **Updated** the Admin Dashboard to read from `st.session_state.sales_history`

**Result:**
✅ Sales data now persists across all user sessions  
✅ Admin can view real-time transaction history  
✅ No data loss when switching between customer and admin views  
✅ Proper state management using Streamlit's session state

**Key Learning:**
This challenge taught the importance of understanding framework-specific state management and choosing the right data persistence strategy for web applications.

---

## 🎓 Skills Demonstrated

This project showcases:
- **Python Programming:** OOP, data structures, algorithms
- **Streamlit Framework:** Web development, UI/UX design
- **State Management:** Session handling, data persistence
- **Problem Solving:** Debugging, optimization, troubleshooting
- **Software Architecture:** E-commerce system design
- **Version Control:** Git & GitHub workflow

---

## 💡 Key Features Implemented by Yoshobanta Bisoi

### 1. **Shared Inventory System**
All users interact with a single, synchronized stock database ensuring real-time updates across sessions.

### 2. **Dynamic Pricing Engine**
Automatic discount calculations with variable discount rates per product.
### 3. **Session Management**
Persistent shopping carts using Streamlit's session state technology.

### 4. **Sales Tracking**
Complete transaction history with detailed analytics for business insights.

### 5. **User Authentication**
Separate customer and admin access levels with secure login system.

## 🎓 Learning Outcomes

This project by **Yoshobanta Bisoi** demonstrates:
- ✅ Python class-based programming and OOP concepts
- ✅ Streamlit framework for rapid web app development
- ✅ Data structure optimization (dictionaries, defaultdict)
- ✅ Session state management for multi-user applications
- ✅ Business logic implementation for e-commerce
- ✅ User interface design and user experience

## 📊 Project Structure

```
KharidLo-2.0/
├── app.py              # Main application file (Yoshobanta Bisoi)
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── problems.txt       # Development notes
└── readme.txt         # Additional documentation
```

## 🔄 Future Enhancements

Yoshobanta Bisoi plans to add:
- Database integration (SQLite/PostgreSQL)
- Payment gateway integration
- User profile management
- Product reviews and ratings
- Advanced search and filtering
- Order history and tracking
- Email notifications

## 🐛 Known Issues

- Sales data persistence relies on Streamlit session state
- Refer to `problems.txt` for development notes and fixes

## 📝 License
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yoshobanta/KharidLo-2.0/issues).

---

**Built with ❤️ by Yoshobanta Bisoi**

**Repository:** [github.com/yoshobanta/KharidLo-2.0](https://github.com/yoshobanta/KharidLo-2.0) | **Live Demo:** [kharidlocart.streamlit.app](https://kharidlocart.streamlit.app/)

---

### 🔍 Keywords

Yoshobanta Bisoi, KharidLo 2.0, E-commerce Application, Python Streamlit Project, Shopping Cart System, Inventory Management System, Python E-commerce, Streamlit Web App, Multi-user Shopping System, Python OOP Project, Real-time Stock Management, Session State Management, Python Project Portfolio

---

© 2025 Yoshobanta Bisoi. All Rights Reserved.
---

**Created with ❤️ by Yoshobanta Bisoi**

**Portfolio**: [GitHub - Yoshobanta Bisoi](https://github.com/yoshobanta)

**Keywords**: Yoshobanta Bisoi, Python Developer, Streamlit Projects, E-commerce Application, Shopping Cart System, Python Projects, KharidLo 2.0, Web Development, Portfolio Project, Yoshobanta Bisoi GitHub, Yoshobanta Bisoi Projects

---

© 2025 Yoshobanta Bisoi. All Rights Reserved.
