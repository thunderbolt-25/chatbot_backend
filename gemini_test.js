const axios = require("axios");

const apiKey = "AIzaSyAZG8hH9B2yzk2-nlEJcUN56CAzmA1lhRg"; // Replace with your API key
const url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + apiKey;

const data = {
  contents: [{
    parts: [{ text: "Explain how AI works" }]
  }]
};

axios.post(url, data, {
  headers: {
    "Content-Type": "application/json"
  }
})
.then(response => {
  // Extract the content from the response and print it
  const content = response.data.candidates[0].content;
  console.log("Gemini Response Content:", content);
})
.catch(error => {
  console.error("Error calling the API:", error);
});
