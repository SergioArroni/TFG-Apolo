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
            calculadora.igual()
            break;
        
        case '.':
            calculadora.punto();
            break;

        case 'C':
            calculadora.delete();
            break;  
    }
});

class Calculadora {

    constructor(){
        this.pantalla = "0";
        this.mrc = "0";
        this.canAddNumber = true;
    }

    canAddOperator() {
        var lastElement = this.pantalla.slice(-1);
        if (lastElement.valueOf() != "+".valueOf() && lastElement.valueOf() != "-".valueOf() && lastElement.valueOf() != "*".valueOf()
            && lastElement.valueOf() != "/".valueOf()) {
            return true;
        } return false;
    }

    suma() {
    	this.canAddNumber = true;
        if (this.canAddOperator()) {
            this.pantalla += "+";
        }
        document.getElementById("pantalla").value = this.pantalla;
    }

    resta() {
    	this.canAddNumber = true;
        if (this.canAddOperator()) {
            this.pantalla += "-";
        }
        document.getElementById("pantalla").value = this.pantalla;
    }

    mul() {
    	this.canAddNumber = true;
        if (this.canAddOperator()) {
            this.pantalla += "*";
        }
        document.getElementById("pantalla").value = this.pantalla;
    }

    div() {
    	this.canAddNumber = true;
        if (this.canAddOperator()) {
            this.pantalla += "/";
        }
        document.getElementById("pantalla").value = this.pantalla;
    }

    add(number) {
        if ((this.pantalla.valueOf() == "0" && number.valueOf() != "." && this.canAddNumber) || this.pantalla.valueOf()=="NaN" || this.pantalla.valueOf()=="Infinity" )
            this.pantalla = ""+ number;
        else if(this.canAddNumber)
            this.pantalla += number;
        document.getElementById("pantalla").value = this.pantalla;
    }

    clear() {
        this.pantalla = "0";
        this.canAddNumber = true;
        document.getElementById("pantalla").value = this.pantalla;
    }

    solve() {
        try {
            var number = "";
            var list = "";
            var pant = this.pantalla.toString();

            for (var i = 0; i < pant.length; i++) {
                if(!(pant.charAt(i).valueOf() >= '0' && pant.charAt(i).valueOf() <= '9')){
                    list += Number(number).toString() + pant.charAt(i).valueOf();
                    number = "";
                }else{
                    number += pant.charAt(i);
                }
              }
            list += number;
            document.getElementById("pantalla").value =  Number(eval(list));
            this.pantalla = "" + Number(eval(this.pantalla));
        }
        catch (err) {
            throw new TypeError('A ocurrido un error: ');
        }
    }

    madd() {
        try {
            if (this.mrc.valueOf() == "0")
                this.mrc = eval(this.pantalla);
            else
                this.mrc += eval(this.pantalla);
        }
        catch (err) {
            throw new TypeError('A ocurrido un error: ');
        }
    }

    mres() {
        try {
            this.mrc -= eval(this.pantalla);
        }
        catch (err) {
            throw new TypeError('A ocurrido un error: ');
        }
    }

    mshow() {
        document.getElementById("pantalla").value = this.mrc;
        this.pantalla = this.mrc;
        this.canAddNumber = false;
    }

    mclear() {
        this.mrc = "0";
        this.pantalla = this.mrc;
    }
}

class CalculadoraCientifica extends Calculadora{

    constructor (){
        super();
        this.angulos = 'DEG';
        this.hyppulsado = false;
        this.shiftpulsado = false;
        this.elevado = 0;
        this.exp = false;
    }
    
    delete(){
        var texto = this.pantalla.toString().substring(0,this.pantalla.length-1);
        this.pantalla = texto.toString();
        document.getElementById("pantalla").value = this.pantalla + '';
    }

    abrirparentesis(){
        var texto = this.pantalla + '(';
        this.pantalla = texto;
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    cerrarparentesis(){
        var texto = this.pantalla + ')';
        this.pantalla = texto;
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    mr(){
        this.pulsado = false;
        super.mrc();
    }

    mc(){
        this.pulsado = true;
        super.mrc();
    }

    ms(){
        this.memoria = this.pantalla.toString();
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    ce(){
        var number;
        for(var i = this.pantalla.length-1; i >= 0; i--) {
           if (!isNaN(this.pantalla.substring(i))){
                number = this.pantalla.substring(i);
           }
         }

        this.pantalla = this.pantalla.substring(0,this.pantalla.length - number.length);

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    cos(){
        try { 
 
            var angulo;
            var texto = document.getElementById("pantalla").value;
            if (this.angulos == 'DEG')
                angulo = texto * (Math.PI / 180);
            else if (this.angulos == 'RAD')
                angulo = texto;
            else
                angulo = texto * 0.015707963267949;
            if (this.shiftpulsado && this.hyppulsado){
                this.pantalla = Math.round(Math.acosh(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                this.shiftpulsado = false;
                this.hyppulsado = false;
            } else if (this.shiftpulsado){
                this.pantalla = Math.round(Math.acos(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                this.shiftpulsado = false;
            } else if (this.hyppulsado){
                this.pantalla = Math.round(Math.cosh(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                this.hyppulsado = false;
            } else
                this.pantalla = Math.round(Math.cos(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    sin(){
        try { 
 
            var angulo;
            var texto = document.getElementById("pantalla").value;

            if (this.angulos == 'DEG')
                angulo = texto * (Math.PI / 180);
            else if (this.angulos == 'RAD')
                angulo = texto;
            else
                angulo = texto * 0.015707963267949;

                if (this.shiftpulsado && this.hyppulsado){
                    this.pantalla = Math.round(Math.asinh(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                    this.shiftpulsado = false;
                    this.hyppulsado = false;
                } else if (this.shiftpulsado){
                    this.pantalla = Math.round(Math.asin(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                    this.shiftpulsado = false;
                } else if (this.hyppulsado){
                    this.pantalla = Math.round(Math.sinh(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                    this.hyppulsado = false;
                } else
                    this.pantalla = Math.round(Math.sin(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    tan(){
        try { 
 
            var angulo;
            var texto = document.getElementById("pantalla").value;

            if (this.angulos == 'DEG')
                angulo = texto * (Math.PI / 180);
            else if (this.angulos == 'RAD')
                angulo = texto;
            else
                angulo = texto * 0.015707963267949;

            if (this.shiftpulsado && this.hyppulsado){
                this.pantalla = Math.round(Math.atanh(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                this.shiftpulsado = false;
                this.hyppulsado = false;
            } else if (this.shiftpulsado){
                this.pantalla = Math.round(Math.atan(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                this.shiftpulsado = false;
            } else if (this.hyppulsado){
                this.pantalla = Math.round(Math.tanh(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
                this.hyppulsado = false;
            } else
                this.pantalla = Math.round(Math.tan(angulo) * Math.pow(10, 10)) / Math.pow(10, 10);
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    sqrt(){
        try { 
            this.pantalla = Math.sqrt(document.getElementById("pantalla").value).toString();
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    cuadrado(){
        try { 
            this.pantalla = Math.pow(document.getElementById("pantalla").value, 2).toString();
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    pow(){
        if (this.pantalla.substring(this.pantalla.length-1) != '^' && this.pantalla.substring(this.pantalla.length-1) != ''){
            for (var i = 0; i< this.pantalla.length; i++)
                if (!isNaN(this.pantalla.substring(i)))
                    this.elevado = this.pantalla.substring(i,this.pantalla.length);
       
            var texto = this.pantalla.toString() + '^';
        }
        
        this.pantalla = texto;
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    potencia10(){
        try { 
            this.pantalla = Math.pow(10, document.getElementById("pantalla").value).toString();
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    log(){
        try { 
            this.pantalla = Math.log10(document.getElementById("pantalla").value).toString();
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    factorial(){
        try { 
            this.pantalla = this.factorialrecursivo(document.getElementById("pantalla").value).toString();
        }
        catch(err) {
            this.pantalla = 'Error = ' + err;
            alert(err);
        }

        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    factorialrecursivo(num){
        if(num < 0)
            throw new TypeError('Negative numbers are not allowed!');
        else if (num <= 1)
            return 1;
        else
            return num * this.factorialrecursivo(num - 1);
    }

    pi(){
        var pi = Math.PI;
        var texto = this.pantalla + pi;
        this.pantalla = texto;
        document.getElementById("pantalla").value = this.pantalla;
    }

    masmenos(){
        var texto = this.pantalla;
            if (texto.substring(0,1) == '-')
                texto = texto.substring(1);
            else
                texto = '-' + this.pantalla;
        this.pantalla = texto.toString();
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    exp1(){
        var texto = this.pantalla;
        if (texto.substring(texto.length - 4) != ",e+0")
        {
            var texto = this.pantalla + ",e+0";
            this.pantalla = texto;
        }
        document.getElementById("pantalla").value = this.pantalla;
    }

    fe(){
        var texto = this.pantalla;
        if (texto.toString().includes('e')){
            this.pantalla = Number.parseFloat(texto);
        }  
        else{
            this.pantalla = Number.parseFloat(texto).toExponential();
        }

        document.getElementById("pantalla").value = this.pantalla;
    }

    deg(){
            if (this.angulos == 'DEG'){
                this.angulos = 'RAD';
            } else if (this.angulos == 'RAD'){
                this.angulos = 'GRAD';
            } else {
                this.angulos = 'DEG';
            }
    }

    hyp(){
        if (this.hyppulsado)
            this.hyppulsado = false;
        else
            this.hyppulsado = true;
    }

    mod(){
        var texto = this.pantalla + '%';
        this.pantalla = texto;
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    shift(){
        if (this.shiftpulsado)
            this.shiftpulsado = false;
        else
            this.shiftpulsado = true;
    }

    punto(){
        this.pulsado = false;
        var texto = this.pantalla + '.';
        this.pantalla = texto;
        document.getElementById("pantalla").value = this.pantalla.toString();
    }

    solve() {
        try {
            var number = "";
            var list = "";
            var pant = this.pantalla.toString();
            var elevable = false;
            var base = 0;
            var exponente = 0;
            var elevacion = 0;

            for (var i = 0; i < pant.length; i++) {
                if(pant.charAt(i).valueOf() == "^"){
                    if(!elevacion){
                        elevable=true;
                        base =  Number(number);
                    }
                    number = "";
                }
                else if(!(pant.charAt(i).valueOf() >= '0' && pant.charAt(i).valueOf() <= '9')){
                    if(pant.charAt(i).valueOf() == "(" || pant.charAt(i).valueOf() == ")"){
                        if(number != ""){
                            list += Number(number) + pant.charAt(i).valueOf();
                        }else{
                            list += pant.charAt(i).valueOf();
                        }

                    }
                    else if(elevable && number != ""){
                        elevable =  false;
                        exponente =  Number(number);
                        list+= Number(Math.pow(base,exponente)) + pant.charAt(i).valueOf();
                    }
                    else if(number != ""){
                        list += Number(number) + pant.charAt(i).valueOf();
                    }else{
                        list +=  pant.charAt(i).valueOf();
                    }
                    number = "";
                }else{
                    number += pant.charAt(i);
                }
              }
                 if(elevable){
                    elevable =  false;
                    exponente =  Number(number);
                    list+= Number(Math.pow(base,exponente));
                }else if(number != ""){
                    list += Number(number);
                }
            this.pantalla = "" + Number(eval(list));
            document.getElementById("pantalla").value =  this.pantalla;

        }
        catch (err) {
            throw new TypeError('A ocurrido un error: ');
        }
    }
}

var calculadora = new CalculadoraCientifica();




