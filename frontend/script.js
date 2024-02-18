// Get the form element
const form = document.getElementById("patient_register");

// Add event listener for form submission

// window.onload = () => {
//   const queryString = window.location.search;
//   const urlParams = new URLSearchParams(queryString);
//   document.getElementsByName("cr_number")[0].value = urlParams.get("crn");
// };
form.addEventListener("submit", async function (event) {
  // Prevent the default form submission
  event.preventDefault();

  // Get form data
  /* The line `const formData = new FormData(form);` is creating a new instance of the FormData object
and passing in the form element as an argument. This allows you to easily access and manipulate the
form data. */
  const formData = new FormData(form);
  const first_name = formData.get("first_name");
  const last_name = formData.get("last_name");
  const full_name = first_name + " " + last_name;

  formData.set("full_name", full_name);
  formData.delete("first_name");
  formData.delete("last_name");


  /* The code is making an HTTP POST request to the "/api/person/" endpoint with the specified headers
  and request body. */
  const res = await fetch("http://127.0.0.1:8000/api/patient-registration/", {
    method: "POST",
    body: formData,
  });
  /* The line `const data = await res.json();` is parsing the response from the server as JSON and
storing it in the `data` variable. This allows you to access and use the data returned by the server
in your JavaScript code. */

  /* The `window.location.reload()` method is used to reload the current webpage. When this method is
  called, the browser will reload the page, effectively refreshing the content and resetting the
  state of the page to its initial state. This can be useful in scenarios where you want to update
  the content on the page after a certain action has been performed, such as submitting a form and
  receiving a response from the server. */
  const data = await res.json();
  if (data) {
    console.log(data);
  }
  // window.location.reload()
});
