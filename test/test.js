const readline = require('readline').createInterface({

input: process.stdin,
output: process.stdout
});

readline.question('Enter first number: ', (num1) => {
readline.question('Enter second number: ', (num2) => {
    const sum = Number(num1) + Number(num2);
    console.log(`The sum is: ${sum}`);
    readline.close();
});
});