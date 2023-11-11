import { Game } from './scenes/game.js';
import { Inicio } from './scenes/inicio.js';
import { Felicidades } from './scenes/felicidades.js';

const config = {
    type: Phaser.AUTO,
    width: 1200,
    height: 500,
    scene: [Inicio, Game, Felicidades],
    backgroundColor: 'black',
    parent: 'Juego_atrapa',
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 400 },
            debug: false
        }
    }
}

var game = new Phaser.Game(config);
export { game };
