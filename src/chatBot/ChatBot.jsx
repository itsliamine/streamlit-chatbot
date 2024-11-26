import React, { useRef,useEffect , useState } from "react";
import ChatWindow from "./chatWindow/ChatWindow";
import Icon from "./Icon";

const ChatBot = () => {
  const ref = useRef(null);
  useEffect(()=>{
    function handleClickOutside(event){
      if(ref.current && !ref.current.contains(event.target)){
        setChatWindowVisible(false);
      }
    }
    document.addEventListener("mousedown",handleClickOutside);
    return ()=>{
      document.removeEventListener("mousedown",handleClickOutside);
    }
  },[ref])




  const [chatWindowVisible, setChatWindowVisible] = useState(false);
  return (
    <div ref={ref}>
      <ChatWindow visible={chatWindowVisible} />
      <Icon
        onClick={() => setChatWindowVisible(true)}
        style={{ position: "fixed", bottom: "50px", right: "30px" }}
      />
    </div>
  );
};

export default ChatBot;
