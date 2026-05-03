// ===============================
// Applicant.js
// Handles:
// 1. Navbar login-state
// 2. Login / Signup modals
// 3. Redirect by user type
// 4. Logout
// 5. Resume upload
// 6. Resume analysis result display
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
// Applicant Page Elements
// =====================================================
const resume = document.getElementById('resumeFile');
const uploadZone = document.getElementById('uploadZone');
const fileStatus = document.getElementById('file-content');
const fileName = document.getElementById('fileName');
const jd = document.getElementById('jobDescription');
const analyzeBtn = document.getElementById('analyzeBtn');

const emptyState = document.getElementById('emptyState');
const analysisResult = document.getElementById('analysisResult');

const scoreText = document.getElementById('scoreText');
const scoreRemark = document.getElementById('scoreRemark');
const scoreProgress = document.getElementById('scoreProgress');

const matchedSkillsList = document.getElementById('matchedSkillsList');
const missingSkillsList = document.getElementById('missingSkillsList');
const feedbackList = document.getElementById('feedbackList');
const suggestionList = document.getElementById('suggestionList');

let selectedResumeFile = null;
let skillChart = null;


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


function protectApplicantPage() {
    const user = getLoggedUser();

    // Logged-out users can still view the page and open login modal.
    if (!user.user_id) {
        return;
    }

    // If a recruiter opens Applicant page, send them to Recruiter page.
    if (user.user_type === 'recruiter' || user.user_type === 'employer') {
        window.location.href = 'Recruiter.html';
    }
}


function logoutUser() {
    localStorage.clear();
    alert('Logged out successfully.');
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
// Resume Upload Functions
// =====================================================
uploadZone.addEventListener('click', () => {
    resume.click();
});


resume.addEventListener('change', () => {
    const file = resume.files[0];

    if (!file) {
        return;
    }

    if (file.type !== 'application/pdf') {
        alert('Please upload only a PDF file.');
        resume.value = '';
        selectedResumeFile = null;
        return;
    }

    selectedResumeFile = file;

    fileName.style.display = 'block';
    fileName.textContent = `Uploaded file: ${file.name}`;
    fileStatus.textContent = 'File Uploaded Successfully!';
});


uploadZone.addEventListener('dragover', (event) => {
    event.preventDefault();
    uploadZone.classList.add('dragover');
});


uploadZone.addEventListener('dragleave', () => {
    uploadZone.classList.remove('dragover');
});


uploadZone.addEventListener('drop', (event) => {
    event.preventDefault();
    uploadZone.classList.remove('dragover');

    const file = event.dataTransfer.files[0];

    if (!file) {
        return;
    }

    if (file.type !== 'application/pdf') {
        alert('Please upload only a PDF file.');
        selectedResumeFile = null;
        return;
    }

    selectedResumeFile = file;

    fileName.style.display = 'block';
    fileName.textContent = `Uploaded file: ${file.name}`;
    fileStatus.textContent = 'File Uploaded Successfully!';
});


function dataValidate() {
    if (!selectedResumeFile) {
        alert('Please upload a resume before analyzing.');
        return false;
    }

    if (!jd.value.trim()) {
        alert('Please enter a job description before analyzing.');
        return false;
    }

    return true;
}


// =====================================================
// Analysis Result Display Functions
// =====================================================
function displayAnalysisResult(data) {
    const analysis = data.analysis;

    if (!analysis) {
        alert('Invalid analysis response from server.');
        return;
    }

    if (emptyState) {
        emptyState.classList.add('d-none');
    }

    analysisResult.classList.remove('d-none');

    const finalScore = analysis.final_match_score || 0;

    scoreText.textContent = `${finalScore}%`;
    scoreProgress.style.width = `${finalScore}%`;
    scoreProgress.textContent = `${finalScore}%`;

    scoreRemark.textContent = getScoreRemark(finalScore);

    renderBadgeList(matchedSkillsList, analysis.matched_skills, 'text-bg-success');
    renderBadgeList(missingSkillsList, analysis.missing_skills, 'text-bg-danger');

    renderTextList(feedbackList, analysis.feedback);
    renderTextList(suggestionList, analysis.suggestions);

    if (analysis.chart_data && analysis.chart_data.skill_match_chart) {
        renderSkillChart(analysis.chart_data.skill_match_chart);
    }

    analysisResult.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}


function getScoreRemark(score) {
    if (score >= 80) {
        return 'Excellent match. The resume is highly suitable for the job description.';
    }

    if (score >= 60) {
        return 'Good match. The resume is relevant, but some improvements are needed.';
    }

    if (score >= 40) {
        return 'Average match. The resume partially matches the job description.';
    }

    return 'Low match. The resume needs significant improvement for this job description.';
}


function renderBadgeList(container, items, badgeClass) {
    container.innerHTML = '';

    if (!items || items.length === 0) {
        const message = document.createElement('p');
        message.className = 'text-secondary mb-0';
        message.textContent = 'No skills found.';
        container.appendChild(message);
        return;
    }

    items.forEach(item => {
        const badge = document.createElement('span');
        badge.className = `badge ${badgeClass} me-2 mb-2 p-2`;
        badge.textContent = item;
        container.appendChild(badge);
    });
}


function renderTextList(container, items) {
    container.innerHTML = '';

    if (!items || items.length === 0) {
        const li = document.createElement('li');
        li.textContent = 'No feedback available.';
        container.appendChild(li);
        return;
    }

    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        container.appendChild(li);
    });
}


function renderSkillChart(chartData) {
    const ctx = document.getElementById('skillChart');

    if (!ctx) {
        return;
    }

    if (skillChart !== null) {
        skillChart.destroy();
    }

    skillChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: chartData.labels,
            datasets: [{
                data: chartData.values
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}


// =====================================================
// Analyze Resume
// =====================================================
analyzeBtn.addEventListener('click', async () => {
    if (!dataValidate()) {
        return;
    }

    try {
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = 'Analyzing...';

        const formData = new FormData();

        formData.append('resume', selectedResumeFile);
        formData.append('jobDescription', jd.value.trim());

        const userId = localStorage.getItem('user_id');

        if (userId) {
            formData.append('user_id', userId);
        }

        const response = await fetch('http://localhost:3000/api/analyze', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            console.log('Analysis Result:', data);
            displayAnalysisResult(data);
        } else {
            console.error('Server Error:', data);
            alert(`Error: ${data.error || data.message || 'Something went wrong'}`);
        }

    } catch (error) {
        console.error('Request Error:', error);
        alert('Could not connect to the server.');
    } finally {
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = 'Analyze My Resume';
    }
});


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
protectApplicantPage();