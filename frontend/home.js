// ===============================
// Home.js
// Handles:
// 1. Login / Signup modals
// 2. Password show/hide
// 3. Login-state navbar
// 4. User dropdown
// 5. Redirect by user type
// 6. Logout
// ===============================


// -------------------------------
// Navbar Auth Elements
// -------------------------------
const loginNavBtn = document.getElementById('loginNavBtn');
const userMenuBox = document.getElementById('userMenuBox');

const navUserDp = document.getElementById('navUserDp');
const navUserName = document.getElementById('navUserName');

const dropdownUserDp = document.getElementById('dropdownUserDp');
const dropdownUserName = document.getElementById('dropdownUserName');
const dropdownUserEmail = document.getElementById('dropdownUserEmail');

const logoutBtn = document.getElementById('logoutBtn');


// -------------------------------
// Login Elements
// -------------------------------
const loginEmail = document.getElementById('loginEmail');
const loginPassword = document.getElementById('loginPassword');
const loginButton = document.getElementById('loginButton');
const toggleLoginPassword = document.getElementById('toggleLoginPassword');


// -------------------------------
// Signup Elements
// -------------------------------
const signupName = document.getElementById('signupName');
const signupDob = document.getElementById('signupDob');
const signupGender = document.getElementById('signupGender');
const signupOccupation = document.getElementById('signupOccupation');
const signupUserType = document.getElementById('signupUserType');
const signupEmail = document.getElementById('signupEmail');
const signupPassword = document.getElementById('signupPassword');
const signupConfirmPassword = document.getElementById('signupConfirmPassword');
const signupButton = document.getElementById('signupButton');
const toggleSignupPassword = document.getElementById('toggleSignupPassword');
const toggleSignupConfirmPassword = document.getElementById('toggleSignupConfirmPassword');


// -------------------------------
// Utility: Get Logged User
// -------------------------------
function getLoggedUser() {
    return {
        user_id: localStorage.getItem('user_id'),
        name: localStorage.getItem('user_name'),
        email: localStorage.getItem('user_email'),
        user_type: localStorage.getItem('user_type'),
        dob: localStorage.getItem('user_dob'),
        gender: localStorage.getItem('user_gender'),
        occupation: localStorage.getItem('user_occupation'),
        profile_picture: localStorage.getItem('user_profile_picture')
    };
}


// -------------------------------
// Utility: Get Initial Letter
// -------------------------------
function getInitial(name) {
    if (!name || name.trim() === '') {
        return 'U';
    }

    return name.trim()[0].toUpperCase();
}


// -------------------------------
// Utility: Set Profile Circle
// -------------------------------
function setProfileCircle(element, user) {
    if (!element) {
        return;
    }

    if (user.profile_picture) {
        element.textContent = '';
        element.style.backgroundImage = `url('${user.profile_picture}')`;
    } else {
        element.style.backgroundImage = 'none';
        element.textContent = getInitial(user.name);
    }
}


// -------------------------------
// Setup Navbar According to Login State
// -------------------------------
function setupAuthNavbar() {
    const user = getLoggedUser();

    if (!loginNavBtn || !userMenuBox) {
        return;
    }

    if (!user.user_id) {
        loginNavBtn.classList.remove('d-none');
        userMenuBox.classList.add('d-none');
        return;
    }

    loginNavBtn.classList.add('d-none');
    userMenuBox.classList.remove('d-none');

    if (navUserName) {
        navUserName.textContent = user.name || 'User';
    }

    if (dropdownUserName) {
        dropdownUserName.textContent = user.name || 'User';
    }

    if (dropdownUserEmail) {
        dropdownUserEmail.textContent = user.email || 'No email';
    }

    setProfileCircle(navUserDp, user);
    setProfileCircle(dropdownUserDp, user);
}


// -------------------------------
// Password Toggle
// -------------------------------
function togglePassword(inputElement, buttonElement) {
    if (!inputElement || !buttonElement) {
        return;
    }

    const type = inputElement.getAttribute('type') === 'password' ? 'text' : 'password';

    inputElement.setAttribute('type', type);
    buttonElement.textContent = type === 'password' ? 'Show' : 'Hide';
}


if (toggleLoginPassword) {
    toggleLoginPassword.addEventListener('click', () => {
        togglePassword(loginPassword, toggleLoginPassword);
    });
}


if (toggleSignupPassword) {
    toggleSignupPassword.addEventListener('click', () => {
        togglePassword(signupPassword, toggleSignupPassword);
    });
}


if (toggleSignupConfirmPassword) {
    toggleSignupConfirmPassword.addEventListener('click', () => {
        togglePassword(signupConfirmPassword, toggleSignupConfirmPassword);
    });
}


// -------------------------------
// Email Validation
// -------------------------------
function emailValidation(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!email) {
        alert('Email cannot be empty.');
        return false;
    }

    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return false;
    }

    return true;
}


// -------------------------------
// Password Validation
// -------------------------------
function passwordValidation(password) {
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d]).{8,}$/;

    if (!password) {
        alert('Password cannot be empty.');
        return false;
    }

    if (!passwordRegex.test(password)) {
        alert('Password must contain minimum 8 characters, uppercase, lowercase, number, and special character.');
        return false;
    }

    return true;
}


// -------------------------------
// Redirect Based on User Type
// -------------------------------
function redirectUserByType(userType) {
    if (userType === 'applicant' || userType === 'job-seeker') {
        window.location.href = 'Applicant.html';
        return;
    }

    if (userType === 'recruiter' || userType === 'employer') {
        window.location.href = 'Recruiter.html';
        return;
    }

    alert('Unknown user type. Please contact support.');
}


// -------------------------------
// Save User Data in Local Storage
// -------------------------------
function saveUserToLocalStorage(user) {
    localStorage.setItem('user_id', user.user_id);
    localStorage.setItem('user_name', user.name || '');
    localStorage.setItem('user_email', user.email || '');
    localStorage.setItem('user_type', user.user_type || '');

    if (user.dob) {
        localStorage.setItem('user_dob', user.dob);
    }

    if (user.gender) {
        localStorage.setItem('user_gender', user.gender);
    }

    if (user.occupation) {
        localStorage.setItem('user_occupation', user.occupation);
    }

    if (user.profile_picture) {
        localStorage.setItem('user_profile_picture', user.profile_picture);
    }
}


// -------------------------------
// Login Function
// -------------------------------
async function loginUser() {
    const emailValue = loginEmail.value.trim();
    const passwordValue = loginPassword.value;

    if (!emailValidation(emailValue)) {
        return;
    }

    if (!passwordValidation(passwordValue)) {
        return;
    }

    try {
        loginButton.disabled = true;
        loginButton.textContent = 'Logging in...';

        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: emailValue,
                password: passwordValue
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.message || 'Login failed');
            return;
        }

        saveUserToLocalStorage(data.user);

        alert('Login successful');

        redirectUserByType(data.user.user_type);

    } catch (error) {
        console.error('Login error:', error);
        alert('Could not connect to server.');
    } finally {
        loginButton.disabled = false;
        loginButton.textContent = 'Log In';
    }
}


// -------------------------------
// Signup Function
// -------------------------------
async function signupUser() {
    const nameValue = signupName.value.trim();
    const dobValue = signupDob.value;
    const genderValue = signupGender.value;
    const occupationValue = signupOccupation.value.trim();
    const userTypeValue = signupUserType.value;
    const emailValue = signupEmail.value.trim();
    const passwordValue = signupPassword.value;
    const confirmPasswordValue = signupConfirmPassword.value;

    if (!nameValue) {
        alert('Name cannot be empty.');
        return;
    }

    if (!userTypeValue) {
        alert('Please select user type.');
        return;
    }

    if (!emailValidation(emailValue)) {
        return;
    }

    if (!passwordValidation(passwordValue)) {
        return;
    }

    if (passwordValue !== confirmPasswordValue) {
        alert('Password and confirm password do not match.');
        return;
    }

    try {
        signupButton.disabled = true;
        signupButton.textContent = 'Signing up...';

        const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: nameValue,
                dob: dobValue,
                gender: genderValue,
                occupation: occupationValue,
                userType: userTypeValue,
                email: emailValue,
                password: passwordValue,
                confirmPassword: confirmPasswordValue
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.message || 'Signup failed');
            return;
        }

        saveUserToLocalStorage({
            ...data.user,
            dob: dobValue,
            gender: genderValue,
            occupation: occupationValue
        });

        alert('Signup successful');

        redirectUserByType(data.user.user_type);

    } catch (error) {
        console.error('Signup error:', error);
        alert('Could not connect to server.');
    } finally {
        signupButton.disabled = false;
        signupButton.textContent = 'Sign Up';
    }
}


// -------------------------------
// Logout Function
// -------------------------------
function logoutUser() {
    localStorage.clear();
    alert('Logged out successfully.');
    setupAuthNavbar();
}


// -------------------------------
// Button Events
// -------------------------------
if (loginButton) {
    loginButton.addEventListener('click', loginUser);
}

if (signupButton) {
    signupButton.addEventListener('click', signupUser);
}

if (logoutBtn) {
    logoutBtn.addEventListener('click', logoutUser);
}


// -------------------------------
// Initialize Navbar on Page Load
// -------------------------------
setupAuthNavbar();