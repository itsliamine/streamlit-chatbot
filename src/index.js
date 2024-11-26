import React from 'react';
import './index.css';
import ReactDOM from 'react-dom/client';
import ChatBot from './chatBot/ChatBot';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ChatBot/>
  </React.StrictMode>
);

