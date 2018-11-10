'use strict';

window.addEventListener('DOMContentLoaded', init);

function init() {
    document.getElementById('loginForm').addEventListener('submit', handleLogin);
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
