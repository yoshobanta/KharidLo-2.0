# Kharidlo 2.0 - E-commerce Shopping Application

## Overview
Kharidlo 2.0 is a comprehensive e-commerce web application built using Python's Streamlit framework that simulates a smartphone retail store. The application features a multi-user shopping system with both customer and administrator functionalities.

## Prerequisites
- Python 3.7 or higher
- Streamlit library (`pip install streamlit`)

## Features

### Customer Features
- **User Registration/Login**: Simple signup process with name, address, and phone number
- **Product Browsing**: View available smartphones with stock levels and pricing
- **Shopping Cart**: Add/remove items, view cart contents with automatic discount calculations
- **Checkout System**: Complete purchase process with order confirmation

### Admin Features
- **Stock Management**: Real-time inventory monitoring
- **Sales Analytics**: Complete transaction history and revenue tracking
- **Business Insights**: Total earnings and discount savings analysis

## Available Products
- iPhone 15 series (iPhone 15, 15 Pro, 15 Pro Max)
- Samsung S24 Ultra
- Google Pixel 9
- OnePlus 12

## How to Run
1. Clone the repository: `git clone https://github.com/yoshobanta/KharidLo-2.0.git`
2. Navigate to the project directory: `cd KharidLo-2.0`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `streamlit run app.py`
5. Access the web interface at http://localhost:8501

## Admin Access
- Username: `admin`
- Password: `yosho123`

**Note**: Only admin can access the Admin panel for managing inventory and viewing sales data. This is for demonstration purposes only.

## Technical Details
- Built with Python and Streamlit
- Uses Streamlit session state for data persistence across page refreshes
- Object-oriented design with shared inventory system
- Real-time stock updates across all user sessions
- Data structures: Dictionaries and defaultdict for efficient cart management

## Known Issues and Limitations
- Sales data persistence relies on Streamlit session state (refer to `problems.txt` for details on previous fixes)
- No persistent database - data resets on application restart
- Admin credentials are hardcoded for demo purposes

## Author
- **Name**: Yoshobanta Bisoi
- **Repository**: [KharidLo-2.0](https://github.com/yoshobanta/KharidLo-2.0)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is open source and available under the [MIT License](LICENSE).