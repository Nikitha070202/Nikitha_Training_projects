import React, { useState, useEffect } from 'react';

function CountdownTimer() {
  const [seconds, setSeconds] = useState(30);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    let intervalId;
    if (isActive) {
      intervalId = setInterval(() => {
        setSeconds((prevSeconds) => prevSeconds - 1);
      }, 1000);
    }
    return () => clearInterval(intervalId);
  }, [isActive]);

  const handleStart = () => {
    setIsActive(true);
  };

  const handleReset = () => {
    setIsActive(false);
    setSeconds(60);
  };

  return (
    <div>
      <h1>{seconds}s</h1>
      {!isActive && seconds === 60 && (
        <button onClick={handleStart}>Start</button>
      )}
      {isActive && (
        <button onClick={() => setIsActive(false)}>Pause</button>
      )}
      {!isActive && seconds < 60 && (
        <button onClick={handleReset}>Reset</button>
      )}
      {seconds === 0 && <h2>Time's up!</h2>}
    </div>
  );
}

export default CountdownTimer;

