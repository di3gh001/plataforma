export class iniciar {
    constructor(scene) {
        this.relatedScene = scene;;
    }
    preload() {

        this.relatedScene.load.spritesheet('button', 'static/img/boton.png', { frameWidth: 190, frameHeight: 49 });

    }
    create() {
        //creamos el boton de inicio
        this.startButton = this.relatedScene.add.sprite(400, 230, 'button').setInteractive();
        this.startButton.on('pointerover', () => {
            this.startButton.setFrame(1);
        });

        this.startButton.on('pointerout', () => {
            this.startButton.setFrame(0);
        });

        this.startButton.on('pointerdown', () => {
            this.relatedScene.scene.start('game')
        });
    }
}