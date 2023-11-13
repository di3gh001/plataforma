import { Detection } from "../detection.js";
import { game } from "../index.js";
var prueba = 'pruebita';
export { prueba };
export let tiempoultimo = null;
export class Game extends Phaser.Scene {

    constructor() {
        super({ key: 'game' });
        this.detection = new Detection();

        this.puntos = 0;
        this.tiempo = {
            minutos: '00',
            segundos: '00'
        };

        this.tiempoultimo = this.tiempo;
        this.mejortiempo = this.tiempo;
    }

    preload() {
        this.load.image('background', 'static/img/fondoraton.jpg');
        this.load.image('gameover', 'static/img/gameover.png');
        this.load.image('raton', 'static/img/raton.png');
        this.load.image('gato', 'static/img/gato.png');
    }

    create() {

        this.add.image(game.config.width / 2, game.config.height / 2, 'background');
        this.gameoverImage = this.add.image(100, 90, 'gameover');
        this.gameoverImage.visible = false;

        this.gato = this.physics.add.image(400, 460, 'gato');
        this.gato.body.allowGravity = false;
        
        this.raton = this.physics.add.image(200, 200, 'raton');
        this.raton.setCollideWorldBounds(true);
        this.raton.body.allowGravity = false;
        this.physics.add.overlap(this.gato, this.raton, this.comerRaton, null, this);
        this.time.addEvent({
            delay: 1000,
            loop: true,
            callback: () => {
                this.actualizarTiempo();
            }
        })
    }

    update() {

        const position = window.point;
        this.gato.x = position.x8;
        this.gato.y = position.y8;
        this.actualizarPuntos();
    }

    comerRaton(gato, raton) {
        this.puntos++;

        raton.destroy();
        this.colocarRatonAleatoriamente();


        if (this.puntos === 5) {
            this.final();
            // Detener el cronómetro cuando se llega a 10 puntos
        }
    }
    final() {
        tiempoultimo = this.tiempo;
        this.scene.start('felicidades');
    }
    actualizarPuntos() {
        // Si existe un texto de puntos anterior, lo eliminamos
        if (this.textoPuntos) {
            this.textoPuntos.destroy();
        }

        if (this.textoTiempo) {
            this.textoTiempo.destroy();
        }

        // Creamos un nuevo texto para mostrar los puntos
        this.textoPuntos = this.add.text(16, 16, `Puntos: ${this.puntos}`, { fontSize: '32px', fill: '#fff' });

        // Creamos un nuevo texto para mostrar el tiempo
        this.textoTiempo = this.add.text(300, 16, `Tiempo: ${this.tiempo.minutos}:${this.tiempo.segundos}`, { fontSize: '32px', fill: '#fff' });
    }

    actualizarTiempo() {
        // Incrementamos los segundos
        this.tiempo.segundos++;

        // Aseguramos que los segundos estén en formato de dos dígitos (por ejemplo, '01' en lugar de '1')
        this.tiempo.segundos = (this.tiempo.segundos >= 10) ? this.tiempo.segundos : '0' + this.tiempo.segundos;

        // Si los segundos llegan a 60, reiniciamos a cero los segundos y aumentamos los minutos
        if (this.tiempo.segundos >= 60) {
            this.tiempo.segundos = '00';
            this.tiempo.minutos++;
            this.tiempo.minutos = (this.tiempo.minutos >= 10) ? this.tiempo.minutos : '0' + this.tiempo.minutos;
        }
        // Llamamos a la función para actualizar los puntos y el tiempo en pantalla
        this.actualizarPuntos();
    }

    finpartida() {
        this.add.text(game.config.width / 2, game.config.height / 2, 'Lo Lograste', {
            fontSize: '50px',
            fill: 'red'
        }).setOrigin(0.5);
        this.tiempoultimo = this.tiempo;

        var nuevoTiempo = parseInt(this.tiempo.minutos + this.tiempo.segundos);
        var mejorTiempo = parseInt(this.mejortiempo.minutos + this.mejortiempo.segundos);
        if (nuevoTiempo > mejorTiempo) {
            mejortiempo = this.tiempo;
        }

        this.scene.pause();
        setTimeout(() => {
            this.scene.stop();
            this.scene.start('game');

        }, 2000)
    }

    colocarRatonAleatoriamente() {
        const randomX = Phaser.Math.RND.between(300, game.config.width - 300);
        const randomY = Phaser.Math.RND.between(200, game.config.height - 200);

        // Creamos una nueva instancia del ratón
        this.raton = this.physics.add.image(randomX, randomY, 'raton');
        this.raton.setCollideWorldBounds(true);

        // Establecemos una nueva colisión entre el gato y el nuevo ratón
        this.physics.add.overlap(this.gato, this.raton, this.comerRaton, null, this);
        this.raton.body.allowGravity = false;
    }

}


