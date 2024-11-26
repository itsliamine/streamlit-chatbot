import React, { useState, useRef } from "react";
import "./chatBox.css";
import MicIcon from "@mui/icons-material/Mic";
import Markdown from "react-markdown";

const ChatBox = () => {
  // State to hold the messages
  const [messages, setMessages] = useState([]);
  // State to hold the input value
  const [inputValue, setInputValue] = useState("");
  // State to track if speech recognition is active
  const [isListening, setIsListening] = useState(false);
  const recognitionRef = useRef(null);

  // Function to add a message to the state
  const addMessage = (text, type) => {
    setMessages((prev) => [...prev, { text, type }]);
  };

  // Function to toggle speech recognition
  const toggleSpeechRecognition = () => {
    // Check if the browser supports speech recognition
    if (!("webkitSpeechRecognition" in window)) {
      alert("Votre navigateur ne supporte pas la reconnaissance vocale");
      return;
    }

    // If not listening, start speech recognition
    if (!isListening) {
      const recognition = new window.webkitSpeechRecognition();
      recognition.lang = "fr-FR";
      recognition.continuous = false;
      recognition.interimResults = false;

      // Set the state to listening when recognition starts
      recognition.onstart = () => setIsListening(true);
      // Update the input value with the recognized speech
      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        setInputValue(transcript);
      };
      // Alert on recognition error
      recognition.onerror = () => alert("Erreur de reconnaissance vocale");
      // Set the state to not listening when recognition ends
      recognition.onend = () => setIsListening(false);
      recognitionRef.current = recognition;
      recognition.start();
    } else {
      // Stop the recognition if already listening
      recognitionRef.current.stop();
      setIsListening(false);
    }
  };

  // Function to send a message
  const sendMessage = async () => {
    // Check if the input value is not empty
    if (!inputValue.trim()) {
      alert("Veuillez saisir une question");
      return;
    }

    // Add the user message to the state
    addMessage(inputValue, "user-message");
    const msg = inputValue;

    // Clear the input value
    setInputValue("");

    try {
      // Send the input value to the API
      const response = await fetch("http://127.0.0.1:5000/api/data", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: msg }),
      });

      // Check if the response is ok
      if (!response.ok) throw new Error("Erreur de requête");

      // Parse the response data
      const data = await response.json();
      // Add the bot message to the state
      addMessage(data.resultat_traite, "bot-message");
    } catch {
      // Add an error message if the request fails
      addMessage(
        `
        Désolé, une erreur s'est produite lors de la récupération des données. Veuillez réessayer plus tard.
        `,
        "bot-message"
      );
    }
  };

  // Function to handle key press events
  const handleKeyPress = (e) => {
    // Send the message if the Enter key is pressed
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="chatbot-container">
      <h1>Chatbot Droit Pluriel</h1>
      <div className="chat-container">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.type}`}>
            {message.type === "bot-message" ? (
              <img src="./bot.png" alt="" />
            ) : (
              ""
            )}
            <div className="texts">
              <Markdown>{message.text}</Markdown>
            </div>
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          placeholder="Posez votre question ici..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyPress}
          className="input-field"
        />
        <button
          onClick={toggleSpeechRecognition}
          className={`mic-button ${isListening ? "listening" : ""}`}
        >
          <MicIcon style={{ fontSize: 30 }} />
        </button>
        <button onClick={sendMessage} className="send-button">
          Envoyer
        </button>
      </div>
    </div>
  );
};

export default ChatBox;
