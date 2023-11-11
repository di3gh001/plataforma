import { Point } from './point.js';

window.point = new Point();
export class Detection {
    constructor() {
        this.x = -3;
        this.y = -5;
        this.x1 = -3;
        this.y1 = -5;
        this.x2 = -3;
        this.y2 = -5;
        this.x3 = -3;
        this.y3 = -5;
        this.x4 = -3;
        this.y4 = -5;
        this.x5 = -3;
        this.y5 = -5;
        this.x6 = -3;
        this.y6 = -5;
        this.x7 = -3;
        this.y7 = -5;
        this.x8 = -3;
        this.y8 = -5;
        this.x9 = -3;
        this.y9 = -5;
        this.x10 = -3;
        this.y10 = -5;
        this.x11 = -3;
        this.y11 = -5;
        this.x12 = -3;
        this.y12 = -5;
        this.x13 = -3;
        this.y13 = -5;
        this.x14 = -3;
        this.y14 = -5;
        this.x15 = -3;
        this.y15 = -5;
        this.x16 = -3;
        this.y16 = -5;
        this.x17 = -3;
        this.y17 = -5;
        this.x18 = -3;
        this.y18 = -5;
        this.x19 = -3;
        this.y19 = -5;

        this.videoElement = document.getElementsByClassName('input_video')[0];

        this.cameraGame = new Camera(this.videoElement, {
            onFrame: async () => {
                await this.hands.send({ image: this.videoElement });
            },
            width: 200,
            height: 100
        });

        this.cameraGame.start();

        this.hands = new Hands({
            locateFile: (file) => {
                return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
            }
        });
        this.hands.setOptions({
            maxNumHands: 2,
            modelComplexity: 1,
            minDetectionConfidence: 0.5,
            minTrackingConfidence: 0.5
        });
        this.hands.onResults(this.onResults);
    }

    onResults(results) {
        if (results.multiHandLandmarks && results.multiHandedness) {
            const rightHandIndex = results.multiHandedness.findIndex(hand => hand.label === 'Left');

            if (rightHandIndex !== -1) {
                const rightHandLandmarks = results.multiHandLandmarks[rightHandIndex];
                const indexTip = rightHandLandmarks[0];
                const indexTip1 = rightHandLandmarks[1];
                const indexTip2 = rightHandLandmarks[2];
                const indexTip3 = rightHandLandmarks[3];
                const indexTip4 = rightHandLandmarks[4];
                const indexTip5 = rightHandLandmarks[5];
                const indexTip6 = rightHandLandmarks[6];
                const indexTip7 = rightHandLandmarks[7];
                const indexTip8 = rightHandLandmarks[8];
                const indexTip9 = rightHandLandmarks[9];
                const indexTip10 = rightHandLandmarks[10];
                const indexTip11 = rightHandLandmarks[11];
                const indexTip12 = rightHandLandmarks[12];
                const indexTip13 = rightHandLandmarks[13];
                const indexTip14 = rightHandLandmarks[14];
                const indexTip15 = rightHandLandmarks[15];
                const indexTip16 = rightHandLandmarks[16];
                const indexTip17 = rightHandLandmarks[17];
                const indexTip18 = rightHandLandmarks[18];
                const indexTip19 = rightHandLandmarks[19];

                // Obtiene la posición de la punta del dedo índice
                // Dibuja la punta del dedo índice
                if (indexTip && indexTip1 && indexTip2 && indexTip3 && indexTip4 && indexTip5 && indexTip6 && indexTip7 && indexTip8 && indexTip9 && indexTip10 && indexTip11 && indexTip12 && indexTip13 && indexTip14 && indexTip15 && indexTip16 && indexTip17 && indexTip18 && indexTip19) {
                    const x = 801 - (indexTip.x * 800);
                    const y = indexTip.y * 500;
                    const x1 = 801 - (indexTip1.x * 800);
                    const y1 = indexTip1.y * 500;
                    const x2 = 801 - (indexTip2.x * 800);
                    const y2 = indexTip2.y * 500;
                    const x3 = 801 - (indexTip3.x * 800);
                    const y3 = indexTip3.y * 500;
                    const x4 = 801 - indexTip4.x * 800;
                    const y4 = indexTip4.y * 500;
                    const x5 = 801 - indexTip5.x * 800;
                    const y5 = indexTip5.y * 500;
                    const x6 = 801 - indexTip6.x * 800;
                    const y6 = indexTip6.y * 500;
                    const x7 = 801 - indexTip7.x * 800;
                    const y7 = indexTip7.y * 500;
                    const x8 = 1002 - indexTip8.x * 1001;
                    const y8 = indexTip8.y * 600;
                    const x9 = 801 - indexTip9.x * 800;
                    const y9 = indexTip9.y * 500;
                    const x10 = 801 - indexTip10.x * 800;
                    const y10 = indexTip10.y * 500;
                    const x11 = 801 - indexTip11.x * 800;
                    const y11 = indexTip11.y * 500;
                    const x12 = 801 - indexTip12.x * 800;
                    const y12 = indexTip12.y * 500;
                    const x13 = 801 - indexTip13.x * 800;
                    const y13 = indexTip13.y * 500;
                    const x14 = 801 - indexTip14.x * 800;
                    const y14 = indexTip14.y * 500;
                    const x15 = 801 - indexTip15.x * 800;
                    const y15 = indexTip15.y * 500;
                    const x16 = 801 - indexTip16.x * 800;
                    const y16 = indexTip16.y * 500;
                    const x17 = 801 - indexTip17.x * 800;
                    const y17 = indexTip17.y * 500;
                    const x18 = 801 - indexTip18.x * 800;
                    const y18 = indexTip18.y * 500;
                    const x19 = 801 - indexTip19.x * 800;
                    const y19 = indexTip19.y * 500;

                    window.point.setPosition(x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16, x17, y17, x18, y18, x19, y19);

                }

            }
        }
    }

    getPosition() {
        return (this.x, this.y, this.x1, this.y1, this.x2, this.y2, this.x3, this.y3, this.x4, this.y4, this.x5, this.y5, this.x6, this.y6, this.x7, this.y7, this.x8, this.y8, this.x9, this.y9, this.x10, this.y10, this.x11, this.y11, this.x12, this.y12, this.x13, this.y13, this.x14, this.y14, this.x15, this.y15, this.x16, this.y16, this.x17, this.y17, this.x18, this.y18, this.x19, this.y19);
    }
}