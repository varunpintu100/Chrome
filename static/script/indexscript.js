// function yesnoCheck(that) {
//     if (that.value == "Input") {
//   alert("This field is to send data");
//         document.getElementById("ifYes").style.display = "block";
//     } else {
//         document.getElementById("ifYes").style.display = "none";
//     }
// }
function display_c(){
    var refresh=1000; // Refresh rate in milli seconds
    mytime=setTimeout('display_ct()',refresh)
}
function display_ct() {
    var x = new Date()
    var x1=x.toUTCString();// changing the display to UTC string
    document.getElementById('ct').innerHTML = x1;
    tt=display_c();
}
    