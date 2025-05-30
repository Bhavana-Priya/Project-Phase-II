let usernameRef = document.getElementById("username");
let passwordRef = document.getElementById("password");
let confirmPasswordRef = document.getElementById("confirm_password");
let eyeL = document.querySelector(".eyeball-l");
let eyeR = document.querySelector(".eyeball-r");
let handL = document.querySelector(".hand-l");
let handR = document.querySelector(".hand-r");

// Normal eye position
let normalEyeStyle = () => {
  eyeL.style.cssText = "left: 0.6em; top: 0.6em;";
  eyeR.style.cssText = "right: 0.6em; top: 0.6em;";
};

// Normal hand position
let normalHandStyle = () => {
  handL.style.cssText =
    "height: 2.81em; top: 8.4em; left: 7.5em; transform: rotate(0deg);";
  handR.style.cssText =
    "height: 2.81em; top: 8.4em; right: 7.5em; transform: rotate(0deg);";
};

// Event listeners for inputs

usernameRef.addEventListener("focus", () => {
  eyeL.style.cssText = "left: 0.75em; top: 1.12em;";
  eyeR.style.cssText = "right: 0.75em; top: 1.12em;";
  normalHandStyle(); // Reset hand position
});

passwordRef.addEventListener("focus", () => {
  handL.style.cssText =
    "height: 6.56em; top: 3.87em; left: 11.75em; transform: rotate(-155deg);";
  handR.style.cssText =
    "height: 6.56em; top: 3.87em; right: 11.75em; transform: rotate(155deg);";
  normalEyeStyle(); // Reset eye position
});

confirmPasswordRef.addEventListener("focus", () => {
  handL.style.cssText =
    "height: 6.56em; top: 3.87em; left: 11.75em; transform: rotate(-155deg);";
  handR.style.cssText =
    "height: 6.56em; top: 3.87em; right: 11.75em; transform: rotate(155deg);";
  normalEyeStyle(); // Close eyes when focused on confirm password
});

// Reset on clicking outside all inputs
document.addEventListener("click", (e) => {
  let clickedElem = e.target;
  if (
    clickedElem !== usernameRef &&
    clickedElem !== passwordRef &&
    clickedElem !== confirmPasswordRef
  ) {
    normalEyeStyle();
    normalHandStyle();
  }
});

