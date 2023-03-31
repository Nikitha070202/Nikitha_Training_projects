import React, { useState } from 'react';

function Modal() {
  const [showModal, setShowModal] = useState(false);

  const handleCloseModal = () => {
    setShowModal(false);
  };

  const handleOpenModal = () => {
    setShowModal(true);
  };

  return (
    <div>
      <button onClick={handleOpenModal}>Click here</button>
      {showModal && (
        <div className="modal">
          <div className="modal-content">
            <img src="https://happybirthdaytime.com/wp-content/uploads/2020/03/Happy-Birthday-Gif-9.gif"/>
            <button onClick={handleCloseModal}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Modal;
