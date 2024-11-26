import React, { useState } from "react";
import { styles } from "./Styles";

const Icon = props => {
  const [hovered, setHovered] = useState(false);

  return (
    <div style={props.style}>
      <div
        className="transition-3"
        style={{
          ...styles.avatarHello,
          ...{ opacity: hovered ? "1" : "0" },
        }}
      >
        Bonjour je suis un chatbot, comment puis-je vous aider ?
      </div>
      <div
        onClick={()=>props.onClick && props.onClick() }
        className="transition-3"
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={{
          ...styles.chatWithMeButton,
          ...{ border: hovered ? "none" : "4px solid #8D0D20" },
        }}
      />
    </div>
  );
};


export default Icon;