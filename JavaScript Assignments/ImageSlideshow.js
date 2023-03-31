import React, { useState, useEffect } from "react";
function ImageSlideshow({ images, duration }) {
    const [currentImageIndex, setCurrentImageIndex] = useState(0);
     useEffect(() => {// exit early when there are no images    
        if (!images.length) return;// move to the next image after the specified duration    
        const intervalId = setInterval(() => {
            setCurrentImageIndex((currentImageIndex) => {
                 const nextIndex = (currentImageIndex + 1) % images.length;
                 return nextIndex;
                });
                 }, duration);
                 return () => clearInterval(intervalId); 
                }, [images, duration]);
                 return ( 
                 <div className="slideshow">
                    <img src={images[currentImageIndex]} alt="slideshow" />
                    
                    <h1>MY ALBUM</h1> 
                    
                </div> 
                );
            }
            export default ImageSlideshow;