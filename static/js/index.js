function fileName() {
    console.log('hi')
    var name = document.getElementById("customFileInput").files[0].name;
    var nextSibling = document.getElementsByClassName("custom-file-label")[0];
    nextSibling.innerText = name
  }

function Loading()
{
var button = document.getElementById("predict");
button.style.display = 'none'
console.log('done')
var text = document.getElementById("loadtext");
text.innerText = 'Please Wait...'
}