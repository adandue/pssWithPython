const readline = require('readline');

// clue-play.js

// Juego de adivinanzas con pistas progresivas

// Configuración del juego
const secretWord = "javascript";
const clues = [
    "Es un lenguaje de programación.",
    "Es muy utilizado en desarrollo web.",
    "Su nombre incluye 'script'.",
    "Es el lenguaje que estás usando ahora."
];

// Inicializar la interfaz de entrada y salida
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para iniciar el juego
function startGame() {
    console.log("¡Bienvenido al juego de adivinanzas!");
    console.log("Tienes que adivinar la palabra secreta basada en las pistas.");
    askForGuess(0);
}

// Función para pedir una respuesta al usuario
function askForGuess(clueIndex) {
    if (clueIndex >= clues.length) {
        console.log("¡Lo siento, te has quedado sin pistas! La palabra secreta era:", secretWord);
        rl.close();
        return;
    }

    console.log("Pista:", clues[clueIndex]);
    rl.question("¿Cuál es tu respuesta? ", (answer) => {
        if (answer.toLowerCase() === secretWord) {
            console.log("¡Felicidades! Adivinaste la palabra secreta.");
            rl.close();
        } else {
            console.log("Respuesta incorrecta. Vamos a la siguiente pista.");
            askForGuess(clueIndex + 1);
        }
    });
}

// Iniciar el juego
startGame();