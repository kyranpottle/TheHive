'use strict';

document.body.addEventListener('DOMContentLoaded', init);

function init() {

}

function getLoginFormInfo() {
    const emailEl = document.getElementById("emailInput");
    const passwordEl = document.getElementById("passwordInput");
    const email = emailEl.value;
    const password = passwordEl.value;
    emailEl.value = "";
    passwordEl.value = "";
    return { email: email, password: password };
}
