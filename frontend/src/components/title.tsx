import { useState } from "react";
import axios from "axios";

type Props ={
    setMessages: any;
}

function Title({ setMessages } : Props){
    const [isResetting, setIsResetting] = useState(false)

    const resetConverstation = async () => {
        setIsResetting(true);

        await axios.get("http://localhost:8000/reset").then((res) => {
            if (res.status == 200) {
                setMessages([])
            }
        }).catch((err) => {
            console.error(err.message);
        })

        setIsResetting(false)
    }

    return <div>
            <button onClick={resetConverstation} className="bg-indigo-500 p-5">
                Reset
            </button>
           </div>
}

export default Title