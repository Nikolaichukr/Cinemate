// The script to make flash messages disappear after the time have passed.

setTimeout(function () {
    let flashMessages = document.getElementsByClassName('flash');
    for (let i = 0; i < flashMessages.length; i++) {
        flashMessages[i].style.display = 'none';
    }
}, 5000); // 5000 milliseconds = 5 seconds
