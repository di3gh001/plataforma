import { tiempoultimo } from "../scenes/game.js";
import { game } from "../index.js";
export class Fin {
    constructor(scene) {
        this.relatedScene = scene;
    }

    preload() {
        this.relatedScene.load.image('buttonfin', 'static/img/guardar.png');
    }

    create() {
        this.finboton = this.relatedScene.add.sprite(game.config.width / 2, 200, 'buttonfin').setInteractive();
        this.finboton.on('pointerover', () => {
            this.finboton.setFrame(1);
        });
        this.finboton.on('pointerdown', () => {
            const textoAdicional = "DERECHA";
            window.location.href = `/puntos?tiempo=${JSON.stringify(tiempoultimo)}&texto=${encodeURIComponent(textoAdicional)}`;

        });
    }
}
