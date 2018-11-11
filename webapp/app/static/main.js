'use strict';

document.addEventListener('DOMContentLoaded', init);

function init() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) loginForm.addEventListener('submit', handleLogin);

    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) logoutButton.addEventListener('click', handleLogout);
}

function getLoginFormInfo() {
    const emailEl = document.getElementById("emailInput");
    const passwordEl = document.getElementById("passwordInput");
    const email = emailEl.value;
    const password = passwordEl.value;
    return { email: email, password: password };
}

function handleLogin() {
    let userInfo = getLoginFormInfo()
    $.post({ 
        url: "/api/user/login",
        data: JSON.stringify(getLoginFormInfo()),
        type: "POST",
        contentType: "application/json",
        success: (_) => {
            window.location.href = "/";
        },
        error: (error) => {
            alert(error.responseText);
        }
    });

    return false;
}

function handleLogout() {
    document.cookie = 'username=;expires=Thu, 01 Jan 1970 00:00:01 GMT';
    window.location.href = "/";
}
