
const DEMO_STUDENT_EMAIL = "student@college.edu";
const DEMO_STUDENT_PASSWORD = "Student@123";

function validateLogin(email, password) {
    if (typeof email !== "string" || typeof password !== "string") {
        return false;
    }

    if (email.trim() === "" || password === "") {
        return false;
    }

    return email.trim() === DEMO_STUDENT_EMAIL &&
           password === DEMO_STUDENT_PASSWORD;
}

window.validateLogin = validateLogin;
