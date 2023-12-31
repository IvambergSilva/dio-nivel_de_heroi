class heroi {
    constructor(name, idade, tipo) {
        this.name = name;
        this.idade = idade;
        this.tipo = tipo;
    }


    verificarAtaque(tipo) {
        if (tipo === "mago") {
            this.ataque = "magia";
        } else if (tipo === "guerreiro") {
            this.ataque = "espada";
        } else if (tipo === "monge") {
            this.ataque = "artes marciais";
        } else if (tipo === "ninja") {
            this.ataque = "shuriken";
        }
    }

    atacar() {
        this.verificarAtaque(this.tipo)
        console.log(`O ${this.tipo} atacou usando ${this.ataque}`);
    }
}

let novoHeroi = new heroi("Berg", 23, "ninja")

novoHeroi.atacar()