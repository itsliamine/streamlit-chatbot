import React, { useState, useRef, useEffect } from "react";
import "./chatBox.css";
import MicIcon from "@mui/icons-material/Mic";
import Markdown from "react-markdown";
import {motion} from "framer-motion"

const ChatBox = () => {
  // State to hold the messages
  const [messages, setMessages] = useState([
	{ text: "Bonjour! Je suis Handie, comment puis-je vous aider aujourd'hui ?", type: "bot-message" },
  ]);
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
	<div className="chatbot-container" style={{ fontFamily: "Avenir !important" }}>
	  <h1>Chatbot Droit Pluriel</h1>
	  <div className="chat-container">
		{messages.map((message, index) => (
		  <div key={index} className={`message ${message.type}`} 
			style={{
				display: "flex",
				alignItems: "center",
				justifyContent: "center",
				marginLeft: "10px",
				fontSize: "16px"
			}}
		  >
			{message.type === "bot-message" ? (
				<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="#8E2621" class="bi bi-robot" viewBox="0 0 16 16">
					<path d="M6 12.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5M3 8.062C3 6.76 4.235 5.765 5.53 5.886a26.6 26.6 0 0 0 4.94 0C11.765 5.765 13 6.76 13 8.062v1.157a.93.93 0 0 1-.765.935c-.845.147-2.34.346-4.235.346s-3.39-.2-4.235-.346A.93.93 0 0 1 3 9.219zm4.542-.827a.25.25 0 0 0-.217.068l-.92.9a25 25 0 0 1-1.871-.183.25.25 0 0 0-.068.495c.55.076 1.232.149 2.02.193a.25.25 0 0 0 .189-.071l.754-.736.847 1.71a.25.25 0 0 0 .404.062l.932-.97a25 25 0 0 0 1.922-.188.25.25 0 0 0-.068-.495c-.538.074-1.207.145-1.98.189a.25.25 0 0 0-.166.076l-.754.785-.842-1.7a.25.25 0 0 0-.182-.135"/>
					<path d="M8.5 1.866a1 1 0 1 0-1 0V3h-2A4.5 4.5 0 0 0 1 7.5V8a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1v1a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-1a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1v-.5A4.5 4.5 0 0 0 10.5 3h-2zM14 7.5V13a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V7.5A3.5 3.5 0 0 1 5.5 4h5A3.5 3.5 0 0 1 14 7.5"/>
				</svg>
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
		<motion.button whileTap={{scale: 0.7}} onClick={sendMessage} className="send-button">
			<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" class="bi bi-send" viewBox="0 0 16 16">
				<path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576zm6.787-8.201L1.591 6.602l4.339 2.76z"/>
			</svg>
		</motion.button>
	  </div>
	</div>
  );
};

export default ChatBox;