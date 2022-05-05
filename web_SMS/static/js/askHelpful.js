/* Get the following Id */
let helpful = document.getElementById("helpful")
let thanks = document.getElementById("thanks")
let sorry = document.getElementById("sorry")
let yes = document.getElementById("yes")
let no = document.getElementById("no")

//Binding onclick event on Yes button
yes.addEventListener('click', function(){
  thanks.style.display = "block"
  sorry.style.display = "none"
  helpful.style.display = "none"
})

//Binding onclick event on No button
no.addEventListener('click', function(){
  sorry.style.display = "block"
  thanks.style.display = "none"
  helpful.style.display = "none"
})