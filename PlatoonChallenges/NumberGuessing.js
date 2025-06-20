numberArray = [];
const btn = document.querySelector("#button");

function randNum(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let randomNumber = randNum(1, 100)
console.log(randomNumber);
// generates a random number

function gameMessage(message) {
    let messageDiv = document.querySelector("#gameMessage");
    // Gets access to the existing 'messageDiv'
    numberList(); // Call numberList to display the list of guesses
    if (messageDiv) {
        messageDiv.innerHTML = "";
    } else {
        messageDiv = document.createElement("div");
        messageDiv.id = "gameMessage";
        document.body.appendChild(messageDiv);
    }
    // If doesn't exist then created
    const textNode = document.createTextNode(message);
    // create text node to display game message
    messageDiv.appendChild(textNode);
}

function numberList() {
    let numberDiv = document.createElement("div");
    numberDiv.id = "numberList";
    document.body.appendChild(numberDiv);
    let list = document.createElement("ul");
    list.id = "numberListItems";
    numberDiv.appendChild(list);
    list.style.display = "flex";
    list.style.flexDirection = "column";
    let listItem = document.createElement("li");
    listItem.id = "numberListItem";
    listItem.innerHTML = "Your guesses: ";
    list.appendChild(listItem);
    numberArray.forEach((number) => {
        let item = document.createElement("li");
        item.innerHTML = number;
        list.appendChild(item);
    });
}

function checkGuess() {
    let userInput = document.querySelector("#Number"); // Get the input element
    userInput = Number(userInput.value); // Convert userInput to a number
    gameMessage("Guess a number between 1 and 100")
    if (userInput === randomNumber) {
        gameMessage("You guessed CORRECTLY and YOU WIN!");
    } else if (userInput > randomNumber) {
        numberArray.push(userInput);
        gameMessage("Your guess is too high. Try again!")
    } else if (userInput < randomNumber) {
        numberArray.push(userInput);
        gameMessage("Your guess is too low. Try again!")
    }
}

btn.addEventListener("click", checkGuess)
