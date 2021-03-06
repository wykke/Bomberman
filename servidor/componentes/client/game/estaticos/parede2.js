import Objeto from "../objeto.js"
import sprites from "../../assets/sprites.js"

export default class Parede2 extends Objeto{
    constructor(id, posicaoX, posicaoY){
        const spriteIdle = "../"+sprites.folder + sprites.parede2
        super(id, posicaoX, posicaoY, spriteIdle)

        this.createDom()
    }
    createDom(){
        this.dom.classList.add("parede2")
        let sprite = document.createElement("img")
        sprite.src = this.spriteIdle
        
        this.dom.appendChild(sprite)
    }
}