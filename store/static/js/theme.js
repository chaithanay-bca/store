// Local storage-based user management
let users = JSON.parse(localStorage.getItem("users")) || [{ username: "admin", password: "password123" }];

function validateLogin() {
    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();
    let errorMessage = document.getElementById("error-message");

    let user = users.find(u => u.username === username && u.password === password);

    if (user) {
        localStorage.setItem("loggedInUser", username);
        alert("Login Successful!");
        document.getElementById("login-container").style.display = "none";
        document.getElementById("main-content").style.display = "block";
        filterProducts("All");
    } else {
        errorMessage.style.display = "block";
        errorMessage.textContent = "Invalid Username or Password";
    }
}

function registerUser() {
    let newUsername = document.getElementById("new-username").value.trim();
    let newPassword = document.getElementById("new-password").value.trim();

    if (!newUsername || !newPassword) {
        alert("Please fill in all fields.");
        return;
    }

    let existingUser = users.find(u => u.username === newUsername);
    if (existingUser) {
        alert("Username already taken.");
        return;
    }

    users.push({ username: newUsername, password: newPassword });
    localStorage.setItem("users", JSON.stringify(users));
    alert("Account Created!");
    showLoginForm();
}

document.addEventListener("DOMContentLoaded", () => filterProducts("All"));

function filterProducts(category) {
    alert(`Showing ${category} products`);
}
