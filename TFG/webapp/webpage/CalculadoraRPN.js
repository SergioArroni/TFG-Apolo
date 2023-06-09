"use strict";

document.addEventListener('keydown', (event) => {

    const keyName = event.key;

    switch (keyName){
        
        case '0':
            calculadora.add(0);
            break;
        case '1':
            calculadora.add(1);
            break;
        case '2':
            calculadora.add(2);
            break;
        case '3':
            calculadora.add(3);
            break;
        case '4':
            calculadora.add(4);
            break;
        case '5':
            calculadora.add(5);
            break;
        case '6':
            calculadora.add(6);
            break;
        case '7':
            calculadora.add(7); 
            break; 
        case '8':
            calculadora.add(8);
            break;
        case '9':
            calculadora.add(9);
            break;
        case '+':
            calculadora.sum();
            break;
        case '-':
            calculadora.resta();
            break;

        case '*':
            calculadora.mul();
            break;
        
        case '/':
            calculadora.div();
            break;
            
        case '=':
            calculadora.enter()
            break;
        
        case '.':
            calculadora.punto();
            break;

        case 'C':
            calculadora.delete();
            break;  
    }
});

class PilaLIFO { 
	constructor (){ 
		this.pila = new Array();
	}
	apilar(valor){
		this.pila.push(valor);
	}
	desapilar(){
		return (this.pila.pop());
	}
}

class Calculadora {
	constructor(pilabuena){
		this.resultado=document.getElementById("resultado");
		this.evaluable="";
		this.m=0.0;
		this.lastR=0;
		this.pila= pilabuena;
	}
	add(number){
		resultado.value = resultado.value + number;
		this.evaluable += number;
	}
	punto(){
		resultado.value = resultado.value + ".";
		this.evaluable += ".";
	}
	pi(){
		resultado.value = resultado.value + "\u03C0";
		this.evaluable += Math.PI;
	}
	enter(){
		if(this.evaluable!=""){
			this.pila.apilar(Number(this.evaluable));
			resultado.value = resultado.value + "\n";
			this.evaluable="";
		}
	}
	repaint(){
		resultado.value="";
		for (var i in this.pila.pila) {
			resultado.value += this.pila.pila[i]+"\n";
		}
	}
	mul(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar();
			this.evaluable=Number(b*a);
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	div(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar(); 
			this.evaluable=Number(b/a);
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	sum(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar();
			this.evaluable=Number(b+a);
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	resta(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar();
			this.evaluable=Number(b-a);
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	clear(){
		resultado.value = "";
		this.evaluable="";
		this.pila.pila=new Array();
	}
    delete(){
		/** 
        this.pila.desapilar();
        this.repaint();
        resultado.value += this.evaluable;
        this.enter();
		*/
		resultado.value = resultado.value.substring(0,resultado.value.length-1);
		this.evaluable = this.evaluable.substring(0,this.evaluable.length-1);
    }
	cuadrado(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			this.evaluable=Number(Math.pow(a,2));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	pow(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar();
			this.evaluable=Number(Math.pow(a,b));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	sin(){
		if(this.evaluable==""){
			this.evaluable=Number(Math.sin(this.pila.desapilar()));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	cos(){
		if(this.evaluable==""){
			this.evaluable=Number(Math.cos(this.pila.desapilar()));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	tan(){
		if(this.evaluable==""){
			this.evaluable=Number(Math.tan(this.pila.desapilar()));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	sqrt(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			this.evaluable=Number(Math.sqrt(a));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	log(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			this.evaluable=Number(Math.log(a));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	factorial(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			if(a>=0 && a%1==0){
				this.evaluable += this.factorialRecursivo(a);
				this.repaint();
				resultado.value += this.evaluable;
				this.enter();
			}else{
				this.pila.apilar(a);
				alert("El factorial debe de ser de un numero natural");
			}
		}

	}
	factorialRecursivo (n) { 
		if (n == 0){ 
			return 1; 
		}
		return Number(n * this.factorialRecursivo (n-1)); 
	}
	masmenos(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			this.evaluable=Number(-a);
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	exponente(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar();
			this.evaluable=Number(a*(10**b));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
	mod(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			var b=this.pila.desapilar();
			this.evaluable=Number(b%a);
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
    base10(){
		if(this.evaluable==""){
			var a=this.pila.desapilar();
			this.evaluable=Number(Math.pow(10,a));
			this.repaint();
			resultado.value += this.evaluable;
			this.enter();
		}
	}
}
var pila =  new PilaLIFO();
var calculadora = new Calculadora(pila);