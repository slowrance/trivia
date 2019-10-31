function reveal() {
    console.log(this.name);
    let myParent = this.parentNode;
    let choices_div = myParent.getElementsByClassName("choices");
    console.log(choices_div);
    let choices = choices_div[0].getElementsByClassName("choice");
    let correct_answer = choices[this.name];
    correct_answer.style.background = "#009c00";

}

let buttons = document.getElementsByClassName("btn");



for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', reveal);
}
console.log("js working")