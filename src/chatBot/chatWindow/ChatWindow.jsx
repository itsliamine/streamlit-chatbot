import React from "react";

import { styles } from "../Styles";
import ChatBox from "./ChatBox";





const ChatWindow = props => {
    return (
        <div
        className="transition-5"
        style= {{

            ...styles.chatWindow,
            ...{opacity : props.visible ? '1' : '0'}
        }}
        >
       <ChatBox/>
        </div>
    )
}


export default ChatWindow;