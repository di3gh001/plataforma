import { game } from "../index.js";
import { iniciar } from "../componentes/botoninicio.js";
export class Inicio extends Phaser.Scene {

    constructor() {
        super({ key: 'inicio' });
        this.Iniciar = new iniciar(this);
    }
    preload() {
        this.load.image('fondo', './static/img/fondo1.jpg');
        this.load.image('gameover', './static/img/gameover.png');
        this.Iniciar.preload();


    }
    create() {
        this.add.image(game.config.width / 2, game.config.height / 2, 'fondo');
        this.Iniciar.create(),
            this.inicioboton = this.add.image(game.config.width / 2, game.config.height / 4, 'gameover')

    }
}

