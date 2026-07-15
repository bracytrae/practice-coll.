// an index file that adds functionality to the web-page, enabling user interactions and dynamic behavior.

const display = document.getElementById('display'); 

/*
after this line javascript can interact with the
calculator's screen through the display variable. 
*/



function appendToDisplay(input){ // appends the input value on top of the display's current value, allowing users to build mathematical expressions.
    display.value += input; 
}

function clearDisplay(){ // this function clears the calculator screen.
    display.value = "";
}

function calculate (){ // this function evaluates the mathematical expression on the calculator screen and displays the result. If there's an error in the expression, it shows "Error" using try and catch to handle exceptions.

    try{
        display.value = eval(display.value);
    }
    catch (error){
        display.value = "Error";
    }

}
