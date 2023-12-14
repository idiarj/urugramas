export class tabsClientes {

    constructor(obj){
         this.obtenerCuerpo = document.getElementById('cuerpo');
         
         this.obj = obj;

         this.divHead = document.createElement('div');
         this.contenedorTotal = document.createElement('div');
         this.barra = document.createElement('div');

         this.crearCuerpo();
         this.divsBotones = document.querySelector('.contenedor .cabecera .divOpciones div')
         this.paneles = document.querySelectorAll('.contenedor .panelInfo');
         this.botones = document.querySelectorAll('.boton');
         this.todasBarras = document.querySelectorAll('.divOpciones .animacionSpan');
         this.showOption();

         
    }

    crearCuerpo(){   
       
       this.contenedorTotal.classList.add('contenedor');
       this.divHead.classList.add('cabecera');


       this.obtenerCuerpo.appendChild(this.contenedorTotal);
       this.contenedorTotal.appendChild(this.divHead);
       
       

       this.addOptions(this.obj);

      } 

    addOptions(arr){
        
         for (let index = 0; index < arr.length; index++){
            let divBotones = document.createElement('div');
            let CreandoBoton = document.createElement('button');
            let panelDiv = document.createElement('div');
            let spanAnimacion = document.createElement('div');
         
   
            divBotones.classList.add('divOpciones')
            CreandoBoton.classList.add('boton');
            panelDiv.classList.add('panelInfo');
            spanAnimacion.classList.add('animacionSpan');
            

                
            let divOpciones = this.divHead.appendChild(divBotones);
            divOpciones.appendChild(spanAnimacion);
            divOpciones.appendChild(CreandoBoton);
            this.contenedorTotal.appendChild(panelDiv);


            CreandoBoton.innerText = arr[index]['buttonText'];
            if((typeof arr[index]['panelContent']) === 'object'){
                panelDiv.appendChild( arr[index]['panelContent'] )
            }else{
            panelDiv.innerHTML = arr[index]['panelContent'];
         }
            
   

         }
         

 } 

 showOption(){
    this.paneles[0].style.visibility = 'visible';
    this.todasBarras[0].style.visibility = 'visible';

    this.botones.forEach( (botones, i) => {
        botones.addEventListener('click', () => {
            //barra
            this.todasBarras.forEach( barras => {
                barras.style.visibility = 'hidden';
            });
            this.todasBarras[i].style.visibility = 'visible';

            //paneles
            this.paneles.forEach( paneless => {
                paneless.style.visibility = 'hidden';
            });
            this.paneles[i].style.visibility = 'visible';
        })
    });

}

}







