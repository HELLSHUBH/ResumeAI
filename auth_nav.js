function getLoggedUser() {
    return {
        user_id: localStorage.getItem('user_id'),
        name: localStorage.getItem('user_name'),
        email: localStorage.getItem('user_email'),
        user_type: localStorage.getItem('user_type'),
        profile_picture: localStorage.getItem('user_profile_picture')
    };
}

function getInitial(name) {
    if (!name || name.trim() === "") {
        return "U";
    }

    return name.trim()[0].toUpperCase();
}

function setProfileCircle(element, user) {
    if (!element) {
        return;
    }

    if (user.profile_picture) {
        element.textContent = "";
        element.style.backgroundImage = `url('${user.profile_picture}')`;
    } else {
        element.style.backgroundImage = "none";
        element.textContent = getInitial(user.name);
    }
}

function setupAuthNavbar() {
    const loginNavBtn = document.getElementById('loginNavBtn');
    const userMenuBox = document.getElementById('userMenuBox');

    const navUserDp = document.getElementById('navUserDp');
    const navUserName = document.getElementById('navUserName');

    const dropdownUserDp = document.getElementById('dropdownUserDp');
    const dropdownUserName = document.getElementById('dropdownUserName');
    const dropdownUserEmail = document.getElementById('dropdownUserEmail');

    const logoutBtn = document.getElementById('logoutBtn');

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

    navUserName.textContent = user.name || "User";
    dropdownUserName.textContent = user.name || "User";
    dropdownUserEmail.textContent = user.email || "No email";

    setProfileCircle(navUserDp, user);
    setProfileCircle(dropdownUserDp, user);

    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            localStorage.clear();
            window.location.href = 'Home.html';
        });
    }
}

setupAuthNavbar();