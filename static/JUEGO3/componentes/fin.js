import { tiempoultimo } from "../scenes/game.js";
export class Fin {
    constructor(scene) {
        this.relatedScene = scene;

    }

    preload() {
        this.relatedScene.load.image('buttonfin', 'static/img/botondon.png');
    }

    create() {
        this.finboton = this.relatedScene.add.sprite(400, 230, 'buttonfin').setInteractive();
        this.finboton.on('pointerover', () => {
            this.finboton.setFrame(1);
        });
        this.finboton.on('pointerdown', () => {
            window.location.href = `/puntos3?tiempo=${JSON.stringify(tiempoultimo)}`;
        });
    }
}
