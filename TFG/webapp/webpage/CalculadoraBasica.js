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
            calculadora.suma();
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
            calculadora.solve()
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
        if (this.pantalla.valueOf() == "0" && number.valueOf() != "." && this.canAddNumber)
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
            alert("Error = " + err);
            document.getElementById("pantalla").value = "Error";
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
            alert("Error = " + err);
            document.getElementById("pantalla").value = "Error";
        }
    }

    mres() {
        try {
            this.mrc -= eval(this.pantalla);
        }
        catch (err) {
            alert("Error = " + err);
            document.getElementById("pantalla").value = "Error";
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

var calculadora = new Calculadora();