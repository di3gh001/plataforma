import { Fin } from "../componentes/fin.js";
import { game } from "../index.js";
import { prueba } from "./game.js";
import { tiempoultimo } from "./game.js";


export class Felicidades extends Phaser.Scene {

    constructor() {
        super({ key: 'felicidades' });
        this.prueba = prueba;
        this.final = new Fin(this);


    }
    preload() {
        this.load.image('fondo', './static/img/fondo.png');
        this.load.image('gameover', './static/img/gameover.png');
        this.final.preload();
    }
    create() {


        // Aquí puedes usar 'tiempoultimo' para lo que necesites en tu escena Felicidades
        // Por ejemplo, puedes mostrarlo en un texto
        this.add.text(game.config.width / 2, game.config.height / 2, `Tiempo último: ${tiempoultimo.minutos}:${tiempoultimo.segundos}`, {
            fontSize: '32px',
            fill: '#fff'
        }).setOrigin(0.5);


        this.final.create();
        this.finalboton = this.add.image(game.config.width / 2, game.config.height / 4, 'gameover');
    }

}

