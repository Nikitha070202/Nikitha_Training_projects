import React, { useState } from 'react';

function FormComponent() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [isChecked, setIsChecked] = useState(false);
  const [selectedOption, setSelectedOption] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission here
  }

  return (
    <form onSubmit={handleSubmit}>
    
      <label htmlFor="name">Name:</label><br></br>
      <input type="text" id="name" value={name} onChange={(event) => setName(event.target.value)} /><br></br>
    
      <label htmlFor="email">Email:</label><br></br>
      <input type="email" id="email" value={email} onChange={(event) => setEmail(event.target.value)} /><br></br>

      <label htmlFor="phone">Phone:</label><br></br>
      <input type="tel" id="phone" value={phone} onChange={(event) => setPhone(event.target.value)} /><br></br>

      
      <label htmlFor="radio1">Male</label>
      <input type="radio" id="radio1" name="radio-group" value="Male" checked={selectedOption === 'Male'} onChange={(event) => setSelectedOption(event.target.value)} />

      <label htmlFor="radio2">Female</label>
      <input type="radio" id="radio2" name="radio-group" value="Female" checked={selectedOption === 'Female'} onChange={(event) => setSelectedOption(event.target.value)} /><br></br>
      <label htmlFor="checkbox1">Java</label>
      <input type="checkbox" id="checkbox1" checked={isChecked} onChange={(event) => setIsChecked(event.target.checked)} /><br></br>
      <label htmlFor="checkbox2">Python</label>
      <input type="checkbox" id="checkbox2" checked={isChecked} onChange={(event) => setIsChecked(event.target.checked)} /><br></br>
      
      <button type="submit">Submit</button>
    </form>
  );
}

export default FormComponent;
