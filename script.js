function submitForm() {
const name = document.getElementById("name");
const email = document.getElementById("email");
const message = document.getElementById("message");
formData = {"name":name.value,"email":email.value,"message":message.value};
name.value = "";
email.value = "";
message.value = "";
console.log(formData);
fetch("/submit", {
    method: "POST",
    body: JSON.stringify(formData),
})
    .then((response) => {
    console.log(response.text())
    })
    .catch((error) => {
        console.error("Error submitting the form:", error);
    });
}

