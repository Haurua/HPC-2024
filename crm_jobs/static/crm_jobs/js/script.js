function logoutConfirm() {
    let logoutForm = document.getElementById("logout-form");
    if (confirm("Do you want to logout?")) {
        logoutForm.submit();
    } else {
        return false;
    }
}