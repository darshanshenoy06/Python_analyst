authentication ={
    "admin": "admin123",
    "analyst": "data456",
    "user": "pass789" 
}
roles = {
        "admin": "full access",
        "analyst": "Analytical access",
        "user": "limited access"
    }
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    
    if username in authentication and authentication[username] == password:
        print(f"Welcome, {username}! You have successfully logged in.")
        print(f"Access level: {roles[username]}")
        return True
    elif username in authentication and authentication[username] != password:
        print("Incorrect password. Please try again.")
    else:
        print("Invalid username or password. Please try again.")
        
login()