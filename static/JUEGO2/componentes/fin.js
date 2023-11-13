import { tiempoultimo } from "../scenes/game.js";
export class Fin {
    constructor(scene) {
        this.relatedScene = scene;

    }

    preload() {
        this.relatedScene.load.image('buttonfin', 'static/img/guardar.png');
    }

    create() {
        this.finboton = this.relatedScene.add.sprite(400, 250, 'buttonfin').setInteractive();
        this.finboton.on('pointerover', () => {
            this.finboton.setFrame(1);
        });
        this.finboton.on('pointerdown', () => {
            const textoAdicional = "DERECHA";
            window.location.href = `/puntos2?tiempo=${JSON.stringify(tiempoultimo)}&texto=${encodeURIComponent(textoAdicional)}`;

        });
    }
}
