import React, { useState } from 'react';

function Calculator() {
  const [input, setInput] = useState('');
  const [operator, setOperator] = useState(null);
  const [prevValue, setPrevValue] = useState(null);

  const handleNumberClick = (number) => {
    setInput(input + number);
  };

  const handleOperatorClick = (operation) => {
    if (prevValue === null) {
      setPrevValue(parseFloat(input));
      setInput('');
    } else {
      const currentValue = parseFloat(input);
      const newValue = calculate(prevValue, currentValue, operator);
      setPrevValue(newValue);
      setInput('');
    }
    setOperator(operation);
  };

  const handleEqualsClick = () => {
    if (prevValue !== null && operator !== null) {
      const currentValue = parseFloat(input);
      const newValue = calculate(prevValue, currentValue, operator);
      setPrevValue(newValue);
      setInput(String(newValue));
      setOperator(null);
    }
  };

  const handleClearClick = () => {
    setInput('');
    setOperator(null);
    setPrevValue(null);
  };

  const calculate = (prevValue, currentValue, operator) => {
    switch (operator) {
      case '+':
        return prevValue + currentValue;
      case '-':
        return prevValue - currentValue;
      case '*':
        return prevValue * currentValue;
      case '/':
        return prevValue / currentValue;
      default:
        return currentValue;
    }
  };

  return (
    <div className="calculator">
      <div className="display">{input || '0'}</div>
      <div className="buttons">
        <button onClick={() => handleNumberClick('1')}>1</button>
        <button onClick={() => handleNumberClick('2')}>2</button>
        <button onClick={() => handleNumberClick('3')}>3</button>
        <button onClick={() => handleOperatorClick('+')}>+</button><br></br>
        <button onClick={() => handleNumberClick('4')}>4</button>
        <button onClick={() => handleNumberClick('5')}>5</button>
        <button onClick={() => handleNumberClick('6')}>6</button>
        <button onClick={() => handleOperatorClick('-')}>-</button><br></br>
        <button onClick={() => handleNumberClick('7')}>7</button>
        <button onClick={() => handleNumberClick('8')}>8</button>
        <button onClick={() => handleNumberClick('9')}>9</button>
        <button onClick={() => handleOperatorClick('*')}>*</button><br></br>
        <button onClick={() => handleNumberClick('0')}>0</button>
        <button onClick={() => handleClearClick()}>C</button>
        <button onClick={() => handleEqualsClick()}>=</button>
        <button onClick={() => handleOperatorClick('/')}>/</button>
      </div>
    </div>
  );
}

export default Calculator;
