// ===============================
// Recruiter.js
// Handles:
// 1. Navbar login-state
// 2. Login / Signup modals
// 3. Redirect by user type
// 4. Same-page logout
// 5. Recruiter PDF upload
// 6. Applicant ranking display
// ===============================


// =====================================================
// Navbar Auth Elements
// =====================================================
const loginNavBtn = document.getElementById('loginNavBtn');
const userMenuBox = document.getElementById('userMenuBox');

const navUserDp = document.getElementById('navUserDp');
const navUserName = document.getElementById('navUserName');

const dropdownUserDp = document.getElementById('dropdownUserDp');
const dropdownUserName = document.getElementById('dropdownUserName');
const dropdownUserEmail = document.getElementById('dropdownUserEmail');

const logoutBtn = document.getElementById('logoutBtn');


// =====================================================
// Login Elements
// =====================================================
const loginEmail = document.getElementById('loginEmail');
const loginPassword = document.getElementById('loginPassword');
const loginButton = document.getElementById('loginButton');
const toggleLoginPassword = document.getElementById('toggleLoginPassword');


// =====================================================
// Signup Elements
// =====================================================
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


// =====================================================
// Recruiter Page Elements
// =====================================================
const uploadBox = document.getElementById('uploadBox');
const applicantResumes = document.getElementById('applicantResumes');
const selectedFiles = document.getElementById('selectedFiles');

const jobTitle = document.getElementById('jobTitle');
const jobDescription = document.getElementById('jobDescription');
const rankApplicantsBtn = document.getElementById('rankApplicantsBtn');

const emptyState = document.getElementById('emptyState');
const rankingTableWrapper = document.getElementById('rankingTableWrapper');
const rankingTableBody = document.getElementById('rankingTableBody');

const totalApplicants = document.getElementById('totalApplicants');
const topScore = document.getElementById('topScore');
const recruiterName = document.getElementById('recruiterName');

let selectedResumeFiles = [];


// =====================================================
// User / Navbar Functions
// =====================================================
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


function getInitial(name) {
    if (!name || name.trim() === '') {
        return 'U';
    }

    return name.trim()[0].toUpperCase();
}


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

    if (recruiterName) {
        recruiterName.textContent = user.name || 'Recruiter';
    }

    setProfileCircle(navUserDp, user);
    setProfileCircle(dropdownUserDp, user);
}


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


function protectRecruiterPage() {
    const user = getLoggedUser();

    // Logged-out users can still view page and open login modal.
    if (!user.user_id) {
        return;
    }

    // If applicant opens Recruiter page, send them to Applicant page.
    if (user.user_type === 'applicant' || user.user_type === 'job-seeker') {
        alert('This page is only for recruiters.');
        window.location.href = 'Applicant.html';
    }
}


function logoutUser() {
    localStorage.clear();

    alert('Logged out successfully.');

    // Stay on same page and update navbar
    setupAuthNavbar();
}


// =====================================================
// Login / Signup Modal Functions
// =====================================================
function togglePassword(inputElement, buttonElement) {
    if (!inputElement || !buttonElement) {
        return;
    }

    const type = inputElement.getAttribute('type') === 'password' ? 'text' : 'password';

    inputElement.setAttribute('type', type);
    buttonElement.textContent = type === 'password' ? 'Show' : 'Hide';
}


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


// =====================================================
// Upload Functions
// =====================================================
uploadBox.addEventListener('click', () => {
    applicantResumes.click();
});


applicantResumes.addEventListener('change', () => {
    const files = Array.from(applicantResumes.files);

    selectedResumeFiles = files.filter(file => file.type === 'application/pdf');

    if (selectedResumeFiles.length !== files.length) {
        alert('Only PDF files are allowed.');
    }

    displaySelectedFiles();
});


uploadBox.addEventListener('dragover', (event) => {
    event.preventDefault();
    uploadBox.classList.add('dragover');
});


uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('dragover');
});


uploadBox.addEventListener('drop', (event) => {
    event.preventDefault();
    uploadBox.classList.remove('dragover');

    const files = Array.from(event.dataTransfer.files);

    selectedResumeFiles = files.filter(file => file.type === 'application/pdf');

    if (selectedResumeFiles.length !== files.length) {
        alert('Only PDF files are allowed.');
    }

    displaySelectedFiles();
});


function displaySelectedFiles() {
    selectedFiles.innerHTML = '';

    if (selectedResumeFiles.length === 0) {
        selectedFiles.innerHTML = `<p class="small text-secondary mb-0">No PDF files selected.</p>`;
        return;
    }

    selectedResumeFiles.forEach((file, index) => {
        const fileDiv = document.createElement('div');
        fileDiv.className = 'file-chip';

        fileDiv.innerHTML = `
            <span>${index + 1}. ${file.name}</span>
            <span>${(file.size / 1024).toFixed(1)} KB</span>
        `;

        selectedFiles.appendChild(fileDiv);
    });
}


// =====================================================
// Recruiter Input Validation
// =====================================================
function validateRecruiterInput() {
    const user = getLoggedUser();

    if (!user.user_id) {
        alert('Please login as recruiter before ranking applicants.');
        return false;
    }

    if (user.user_type !== 'recruiter' && user.user_type !== 'employer') {
        alert('Only recruiters can rank applicants.');
        return false;
    }

    if (!jobTitle.value.trim()) {
        alert('Please enter job title.');
        return false;
    }

    if (!jobDescription.value.trim()) {
        alert('Please enter job description.');
        return false;
    }

    if (selectedResumeFiles.length === 0) {
        alert('Please upload at least one applicant resume.');
        return false;
    }

    return true;
}


// =====================================================
// Rank Applicants
// =====================================================
rankApplicantsBtn.addEventListener('click', async () => {
    if (!validateRecruiterInput()) {
        return;
    }

    try {
        rankApplicantsBtn.disabled = true;
        rankApplicantsBtn.textContent = 'Ranking...';

        const formData = new FormData();

        formData.append('recruiter_id', localStorage.getItem('user_id'));
        formData.append('jobTitle', jobTitle.value.trim());
        formData.append('jobDescription', jobDescription.value.trim());

        selectedResumeFiles.forEach(file => {
            formData.append('resumes', file);
        });

        const response = await fetch('/api/recruiter/rank', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || data.message || 'Ranking failed');
            return;
        }

        displayRankingResults(data.results);

    } catch (error) {
        console.error('Ranking error:', error);
        alert('Could not connect to server.');
    } finally {
        rankApplicantsBtn.disabled = false;
        rankApplicantsBtn.textContent = 'Rank Applicants';
    }
});


// =====================================================
// Display Ranking Results
// =====================================================
function displayRankingResults(results) {
    rankingTableBody.innerHTML = '';

    if (!results || results.length === 0) {
        emptyState.classList.remove('d-none');
        rankingTableWrapper.classList.add('d-none');
        totalApplicants.textContent = '0';
        topScore.textContent = '0%';
        return;
    }

    emptyState.classList.add('d-none');
    rankingTableWrapper.classList.remove('d-none');

    results.forEach((applicant, index) => {
        const row = document.createElement('tr');

        const score = applicant.final_match_score || 0;

        row.innerHTML = `
            <td class="fw-bold">#${index + 1}</td>

            <td>
                <div class="fw-semibold">${applicant.file_name || 'Applicant Resume'}</div>
                <div class="small text-secondary">Applicant Resume</div>
            </td>

            <td>
                <span class="score-pill ${getScoreClass(score)}">
                    ${score}%
                </span>
            </td>

            <td>${formatSkillList(applicant.matched_skills)}</td>

            <td>${formatSkillList(applicant.missing_skills)}</td>

            <td>
                <span class="badge ${getStatusClass(score)}">
                    ${getStatusText(score)}
                </span>
            </td>
        `;

        rankingTableBody.appendChild(row);
    });

    totalApplicants.textContent = results.length;
    topScore.textContent = `${results[0].final_match_score || 0}%`;
}


function formatSkillList(skills) {
    if (!skills || skills.length === 0) {
        return '<span class="text-secondary small">None</span>';
    }

    return skills.slice(0, 5).map(skill => {
        return `<span class="badge text-bg-light border me-1 mb-1">${skill}</span>`;
    }).join('');
}


function getScoreClass(score) {
    if (score >= 80) {
        return 'text-bg-success';
    }

    if (score >= 60) {
        return 'text-bg-warning';
    }

    return 'text-bg-danger';
}


function getStatusClass(score) {
    if (score >= 80) {
        return 'text-bg-success';
    }

    if (score >= 60) {
        return 'text-bg-warning';
    }

    return 'text-bg-danger';
}


function getStatusText(score) {
    if (score >= 80) {
        return 'Shortlist';
    }

    if (score >= 60) {
        return 'Review';
    }

    return 'Reject';
}


// =====================================================
// Event Listeners for Auth
// =====================================================
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

if (loginButton) {
    loginButton.addEventListener('click', loginUser);
}

if (signupButton) {
    signupButton.addEventListener('click', signupUser);
}

if (logoutBtn) {
    logoutBtn.addEventListener('click', logoutUser);
}


// =====================================================
// Initialize Page
// =====================================================
setupAuthNavbar();
protectRecruiterPage();
displaySelectedFiles();