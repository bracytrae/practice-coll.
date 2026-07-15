const startBtn = document.querySelector(".btn-start");

const minuteDiv = document.querySelector(".minutes");

const secondDiv = document.querySelector(".seconds");

const appMessage = document.querySelector(".app-message");

let myInterval;

let timerIsRunning = false;

const appTimer = () => {
  if (timerIsRunning) {
    appMessage.textContent = "session has already started";

    return;
    
  }

  timerIsRunning = true;

  appMessage.textContent = "focus time";

  let totalSeconds = Number.parseInt(minuteDiv.textContent, 10) * 60;

  const updateSeconds = () => {

    totalSeconds -= 1;

    const minutesLeft = Math.floor(totalSeconds / 60);

    const secondsLeft = totalSeconds % 60;

    minuteDiv.textContent = String(minutesLeft);

    secondDiv.textContent = String(secondsLeft).padStart(2, "0");

    if (totalSeconds <= 0) {

      clearInterval(myInterval);

      timerIsRunning = false;

      appMessage.textContent = "session complete";
      
    }
  };

  myInterval = setInterval(updateSeconds, 1000);

};

startBtn.addEventListener("click", appTimer);
