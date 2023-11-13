import { Detection } from "../detection.js";
import { game } from "../index.js";
export let tiempoultimo = null;
export class Game extends Phaser.Scene {

    constructor() {
        super({ key: 'game' });
        this.detection = new Detection();
        this.velocidadMaxima = 200;
        this.puntos = 0;
        this.tiempo = {
            minutos: '00',
            segundos: '00'
        };

        this.tiempoultimo = this.tiempo;
        this.mejortiempo = this.tiempo;

    }

    preload() {
        this.load.image('background', 'static/img/fondo2.jpg');
        this.load.image('dona', 'static/img/pelota.png');
        this.load.image('rectangulo', 'static/img/equals.png');
        this.load.image('crate32', 'static/img/equals.png');
        this.load.image('plataforma', 'static/img/platform.png');
    }

    create() {
        this.add.image(game.config.width / 2, game.config.height / 2, 'background');
        this.plataforma = this.physics.add.image(300, 450, 'plataforma').setImmovable();
        this.plataforma.body.allowGravity = false;
        this.plataforma.setScale(5, 1);

        // Agrega el gato como un sprite con físicas
        this.gato = this.physics.add.image(game.config.width / 2, game.config.height / 2, 'dona').setImmovable();
        this.gato.body.allowGravity = false;
        this.gato.setCollideWorldBounds(true);

        // Crea un grupo para gestionar los rectángulos
        this.rectangulosGroup = this.physics.add.group();

        // Crea varios rectángulos y agrégales físicas
        this.crearRectangulo(200, 300);
        this.crearRectangulo(300, 300);
        this.crearRectangulo(400, 300);
        this.crearRectangulo(250, 200);
        this.crearRectangulo(350, 200);
        this.crearRectangulo(300, 100);

        // Configura colisiones
        this.physics.add.collider(this.rectangulosGroup, this.rectangulosGroup); // Añadido para colisiones entre rectángulos
        this.physics.add.collider(this.gato, this.rectangulosGroup, this.empujarRectangulo, null, this);
        this.physics.add.collider(this.rectangulosGroup, this.plataforma);

        // Texto para mostrar el número de rectángulos
        this.textoNumRectangulos = this.add.text(16, 16, 'Número de rectángulos: ' + this.rectangulosGroup.getLength(), { fontSize: '24px', fill: '#fff' });

        // Texto para mostrar el tiempo
        this.textoTiempo = this.add.text(game.config.width - 300, 16, 'Tiempo: ' + this.tiempo.minutos + ':' + this.tiempo.segundos, { fontSize: '24px', fill: '#fff' });

        this.time.addEvent({
            delay: 1000,
            loop: true,
            callback: () => {
                this.actualizarTiempo();
            }
        })
    }
    update() {
        // Configura colisiones entre rectángulos
        this.physics.world.collide(this.rectangulosGroup, this.rectangulosGroup, null, null, this);

        // Actualiza la posición del gato después de las colisiones
        const position = window.point;
        this.gato.x = position.x8;
        this.gato.y = position.y8;

        // Actualiza el grupo de rectángulos
        this.rectangulosGroup.children.iterate(rectangulo => {
            if (rectangulo && rectangulo.y > game.config.height) {
                rectangulo.destroy(); // Elimina el rectángulo
            }
        });

        // Actualiza el texto con el número de rectángulos
        this.textoNumRectangulos.setText('Número de rectángulos: ' + this.rectangulosGroup.getLength());

        // Actualiza el texto con el tiempo
        this.textoTiempo.setText('Tiempo: ' + this.tiempo.minutos + ':' + this.tiempo.segundos);
        if (this.rectangulosGroup.getLength() === 0) {
            this.final();
        }
    }
    final() {
        tiempoultimo = this.tiempo;
        this.scene.start('felicidades');
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

    empujarRectangulo(gato, rectangulo) {
        // Verifica que gato y rectangulo tengan la propiedad 'body'
        if (gato.body && rectangulo.body) {
            // Configura la velocidad del rectángulo para simular el empuje
            rectangulo.setVelocityX(gato.body.velocity.x * 1.5);
            rectangulo.setVelocityX(-200); // Ajusta la velocidad de caída al empujar
            rectangulo.setAngularVelocity(300);
        }
    }
    crearRectangulo(x, y) {
        const rectangulo = this.physics.add.image(x, y, 'rectangulo');
        rectangulo.body.allowGravity = true;
        rectangulo.setBounce(0.4);
        rectangulo.setScale(0.8, 0.8);
        this.rectangulosGroup.add(rectangulo);
        return rectangulo;
    }
}
