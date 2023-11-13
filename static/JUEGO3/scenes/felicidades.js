import { Fin } from "../componentes/fin.js";
import { game } from "../index.js";
import { tiempoultimo } from "./game.js";


export class Felicidades extends Phaser.Scene {

    constructor() {
        super({ key: 'felicidades' });

        this.final = new Fin(this);


    }
    preload() {
        this.load.image('fondo', './static/img/finaljuego3.png');

        this.final.preload();
    }
    create() {
        this.finalboton = this.add.image(game.config.width / 2, game.config.height / 2, 'fondo');
        this.finalboton.setScale(0.7, 0.5)
        this.add.text(game.config.width / 2, 200, `Tiempo último: ${tiempoultimo.minutos}:${tiempoultimo.segundos}`, {
            fontSize: '32px',
            fill: '#fff'
        }).setOrigin(0.5);
        this.final.create();
    }

}

