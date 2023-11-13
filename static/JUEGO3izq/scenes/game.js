import { Detection } from "../detectionizq.js";
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
        this.puntos = 3;

    }

    preload() {
        this.load.image('background', 'static/img/fondo1.jpg');
        this.load.image('dona', 'static/img/mosquito.png');
        this.load.image('caja', 'static/img/equals.png');
        this.load.image('piso', 'static/img/mesabien.png');

    }

    create() {
        this.add.image(game.config.width / 2, game.config.height / 2, 'background');
        this.plataforma = this.physics.add.image(650, 500, 'piso').setImmovable();
        this.plataforma.body.allowGravity = false;
        this.plataforma.setScale(1, 0.5);

        this.caja = this.physics.add.image(500, 100, 'caja');
        this.caja.body.allowGravity = true;
        this.physics.add.collider(this.caja, this.plataforma);

        this.caja1 = this.physics.add.image(600, 100, 'caja');
        this.caja1.body.allowGravity = true;
        this.physics.add.collider(this.caja1, this.plataforma);

        this.caja2 = this.physics.add.image(700, 100, 'caja');
        this.caja2.body.allowGravity = true;
        this.physics.add.collider(this.caja2, this.plataforma);

        this.ball = this.physics.add.image(game.config.width / 2, game.config.height / 2, 'dona').setImmovable();
        this.ball.body.allowGravity = false;

        this.ball1 = this.physics.add.image(game.config.width / 2, game.config.height / 2, 'dona').setImmovable();
        this.ball1.body.allowGravity = false;

        if (!this.hayCajasEnPantalla()) {
            this.final();
        }
        
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
        const position = window.point;

        this.ball.x = position.x4;
        this.ball.y = position.y4;

        this.ball1.x = position.x8;
        this.ball1.y = position.y8;

        // Actualiza el texto con el tiempo
        this.textoTiempo.setText('Tiempo: ' + this.tiempo.minutos + ':' + this.tiempo.segundos);
        this.moverCaja();
        this.moverCaja1();
        this.moverCaja2();
        if (!this.hayCajasEnPantalla()) {
            this.final();
        }
    }
    hayCajasEnPantalla() {
        const alturaPantalla = game.config.height;

        return this.caja.y < alturaPantalla ||
            this.caja1.y < alturaPantalla ||
            this.caja2.y < alturaPantalla;
    }

    moverCaja() {
        const distanciaMinima = 50; // Ajusta la distancia mínima según tus necesidades

        // Calcula la distancia entre ambas bolas y la caja
        const distanciaBall = Phaser.Math.Distance.Between(this.caja.x, this.caja.y, this.ball.x, this.ball.y);
        const distanciaBall1 = Phaser.Math.Distance.Between(this.caja.x, this.caja.y, this.ball1.x, this.ball1.y);

        // Si ambas bolas están lo suficientemente cerca de la caja, muévela
        if (distanciaBall < distanciaMinima && distanciaBall1 < distanciaMinima) {
            this.caja.setPosition((this.ball.x + this.ball1.x) / 2, (this.ball.y + this.ball1.y) / 2);
        }

        // Aquí puedes agregar lógica adicional si es necesario
    }
    moverCaja1() {
        const distanciaMinima = 50; // Ajusta la distancia mínima según tus necesidades

        // Calcula la distancia entre ambas bolas y la caja
        const distanciaBall = Phaser.Math.Distance.Between(this.caja1.x, this.caja1.y, this.ball.x, this.ball.y);
        const distanciaBall1 = Phaser.Math.Distance.Between(this.caja1.x, this.caja1.y, this.ball1.x, this.ball1.y);

        // Si ambas bolas están lo suficientemente cerca de la caja, muévela
        if (distanciaBall < distanciaMinima && distanciaBall1 < distanciaMinima) {
            this.caja1.setPosition((this.ball.x + this.ball1.x) / 2, (this.ball.y + this.ball1.y) / 2);
        }

        // Aquí puedes agregar lógica adicional si es necesario
    }
    moverCaja2() {
        const distanciaMinima = 50; // Ajusta la distancia mínima según tus necesidades

        // Calcula la distancia entre ambas bolas y la caja
        const distanciaBall = Phaser.Math.Distance.Between(this.caja2.x, this.caja2.y, this.ball.x, this.ball.y);
        const distanciaBall1 = Phaser.Math.Distance.Between(this.caja2.x, this.caja2.y, this.ball1.x, this.ball1.y);

        // Si ambas bolas están lo suficientemente cerca de la caja, muévela
        if (distanciaBall < distanciaMinima && distanciaBall1 < distanciaMinima) {
            this.caja2.setPosition((this.ball.x + this.ball1.x) / 2, (this.ball.y + this.ball1.y) / 2);
        }

        // Aquí puedes agregar lógica adicional si es necesario
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

}
