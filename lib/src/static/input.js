/*
 * if you are not already aware this grabs the current url of the page
 */
let url = window.location.href;

/* 
 * data = {} is what we are sending to the backend to be processed
 */
function send_video_option_input(typ) {
    /*
     * send the option we receive from the user to our api
     * this may return 1 which tells us that the operation 
     * is not available on the backend
     */
    send_option(url+"/option", typ)
        .then(data => {
            if(data === 1) {
                alert("Unsupported Function");
            }
    });

    /* 
     * we have to alert the user otherwise they will just spam the api
     */
    alert("unsupported operation");
} 

async function send_option(url, typ) {
    const data = {
        "typ": "next_vid",
    };

    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(data)
    });

    return response.json();
}
