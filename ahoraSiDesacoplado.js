import { tabsClientes } from "./tabsClientes";

export class ahoraSiDesacoplado{
    constructor(){
        this.personalizacion = [
            { buttonText: 'Los inventores del racismo', panelContent: '<img src="./imagenes/pablomaduro.jpg">' },
            { buttonText: 'Soy el Boton 2', panelContent: c },
            { buttonText: 'Yo cuando me gradue', panelContent: '<img src="https://media.tenor.com/IWOe1FcDUCIAAAAC/jotaro-plane-window.gif">' },
            { buttonText: 'Need For Comandante', panelContent: '<img  src="./imagenes/chavez1.jpg">' },
            { buttonText: 'Me llamo Boton 352', panelContent: '<p>Haaland Balon de Or</p>' }
        ];
        this.tabInstancia();
    }
    tabInstancia(){
        let tabDesacoplado = new tabsClientes(this.personalizacion);

    }
}