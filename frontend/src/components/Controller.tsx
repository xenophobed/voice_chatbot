import { useState } from "react";

function Controller(){

    const [isLoading, setIsLoading] = useState(false);
    const [messages, setMessages] = useState<any[]>([]);
    const createBlobUrl = (data: any) => {};

    const handleStop = () => {}


    return (
        <div className="h-screen, overflow-y-hidden">
            <div>Title</div>
            <div className="flex flex-col justify-between h-full overflow-y-scroll underline pd-96">
                Placeholder
            </div>
        </div>
    )
}

export default Controller;
