// Canvas component for drawing shapes

import React, { useRef, useEffect } from 'react';

interface CanvasProps {
    width: number;
    height: number;
}

const Canvas: React.FC<CanvasProps> = ({ width, height }) => {
    const canvasRef = useRef<HTMLCanvasElement>(null);
    <button onClick={() => console.log('button to draw on canvas')}>
          Draw Canvas
    </button>
    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        // Set canvas dimensions
        canvas.width = width;
        canvas.height = height;

        canvas.addEventListener('click', () => {
            // Draw a 200px radius circle in the top right corner of the canvas
            ctx.beginPath();
            ctx.arc(200, 200, 200, 0, 2 * Math.PI);
            ctx.stroke();
            ctx.fillStyle = 'red';
        });
    }, [width, height]);

    return <canvas ref={canvasRef} />;
};

export default Canvas;
