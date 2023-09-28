// import { useState } from 'react'
import React, { useState, useRef, useEffect } from "react";
import "./App.css";
// import Canvas from './components/Canvas'

function GetState(currentState: boolean) {
  return !currentState;
}

export default function App() {
  const [isButtonClicked, setIsButtonClicked] = useState(false);

  const toggleCanvas = () => {
    // toggle button click
    setIsButtonClicked(!isButtonClicked);
    console.log(`Button clicked: ${isButtonClicked}`);
    return isButtonClicked;
  };
  return (
    <>
      <div>
        <h1>ERT TypeScript Assessment</h1>
        <button onClick={toggleCanvas}>Draw/Clear Canvas</button>
      </div>
      <div style={{ width: "400px", height: "400px", padding: "2rem", justifySelf: "center" }}>
        {isButtonClicked && <Canvas width={400} height={400} isClicked={isButtonClicked}/>}
      </div>
    </>
  );
}

interface CanvasProps {
  width: number;
  height: number;
  isClicked: boolean;
}

const Canvas: React.FC<CanvasProps> = ({ width, height, isClicked }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;

    const ctx = canvas?.getContext("2d");

    // Set canvas dimensions
    if (canvas && ctx) {
      canvas.width = width;
      canvas.height = height;
    } else {
      console.log("Canvas or context not found");
      return;
    }

    // canvas.addEventListener("click", () => {
    //   console.log("Canvas clicked");
    //   handleButtonClick();
    // });

    if (isClicked) {
      // Draw a 200px red-filled radius circle in the top right corner of the canvas
      ctx.beginPath();
      ctx.arc(300, 100, 100, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fillStyle = "red";
      ctx.fill();
      // Draw an ellipse in bottom left corner of canvas
      ctx.beginPath();
      ctx.ellipse(100, 300, 50, 75, Math.PI / 4, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fillStyle = "blue";
      ctx.fill();
    } else {
      // Clear the canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }, [width, height]);

  return <canvas ref={canvasRef} />;
};
