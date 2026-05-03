const profileDp = document.getElementById('profileDp');
const profileNameHeading = document.getElementById('profileNameHeading');
const profileEmailHeading = document.getElementById('profileEmailHeading');

const profileName = document.getElementById('profileName');
const profileEmail = document.getElementById('profileEmail');
const profileDob = document.getElementById('profileDob');
const profileGender = document.getElementById('profileGender');
const profileOccupation = document.getElementById('profileOccupation');
const profileUserType = document.getElementById('profileUserType');

const editProfileBtn = document.getElementById('editProfileBtn');
const saveProfileBtn = document.getElementById('saveProfileBtn');
const cancelProfileBtn = document.getElementById('cancelProfileBtn');
const profileActionButtons = document.getElementById('profileActionButtons');

let originalProfileData = null;

function requireLogin() {
    const userId = localStorage.getItem('user_id');

    if (!userId) {
        alert('Please login first.');
        window.location.href = 'Home.html';
        return false;
    }

    return true;
}

async function loadProfile() {
    if (!requireLogin()) {
        return;
    }

    const userId = localStorage.getItem('user_id');

    try {
        const response = await fetch(`http://localhost:3000/api/profile/${userId}`);
        const data = await response.json();

        if (!response.ok) {
            alert(data.message || 'Could not load profile.');
            return;
        }

        originalProfileData = data.user;

        fillProfile(data.user);

    } catch (error) {
        console.error('Profile load error:', error);
        alert('Could not connect to server.');
    }
}

function fillProfile(user) {
    profileNameHeading.textContent = user.name || '-';
    profileEmailHeading.textContent = user.email || '-';

    profileName.value = user.name || '';
    profileEmail.value = user.email || '';
    profileDob.value = user.dob || '';
    profileGender.value = user.gender || '';
    profileOccupation.value = user.occupation || '';
    profileUserType.value = user.user_type || '';

    profileDp.textContent = user.name ? user.name[0].toUpperCase() : 'U';

    localStorage.setItem('user_name', user.name || '');
    localStorage.setItem('user_email', user.email || '');
    localStorage.setItem('user_type', user.user_type || '');
}

function setEditMode(isEditing) {
    profileName.disabled = !isEditing;
    profileDob.disabled = !isEditing;
    profileGender.disabled = !isEditing;
    profileOccupation.disabled = !isEditing;

    profileActionButtons.classList.toggle('d-none', !isEditing);
    editProfileBtn.classList.toggle('d-none', isEditing);
}

editProfileBtn.addEventListener('click', () => {
    setEditMode(true);
});

cancelProfileBtn.addEventListener('click', () => {
    fillProfile(originalProfileData);
    setEditMode(false);
});

saveProfileBtn.addEventListener('click', async () => {
    const userId = localStorage.getItem('user_id');

    if (!profileName.value.trim()) {
        alert('Name cannot be empty.');
        return;
    }

    try {
        const response = await fetch(`http://localhost:3000/api/profile/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: profileName.value.trim(),
                dob: profileDob.value,
                gender: profileGender.value,
                occupation: profileOccupation.value.trim()
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.message || 'Profile update failed.');
            return;
        }

        originalProfileData = data.user;

        fillProfile(data.user);
        setEditMode(false);

        alert('Profile updated successfully.');

    } catch (error) {
        console.error('Profile update error:', error);
        alert('Could not connect to server.');
    }
});

loadProfile();