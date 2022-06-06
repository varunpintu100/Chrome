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
}// This is used to display the clock under the span
function display_ct() {
    var x = new Date()
    var ampm = x.getHours( ) >= 12 ? ' PM' : ' AM';
    var x1=x.getMonth() + 1+ "/" + x.getDate() + "/" + x.getFullYear(); 
    x1 = x1 + " - " +  x.getHours( )+ ":" +  x.getMinutes() + ":" +  x.getSeconds() + ":" +ampm;
    document.getElementById('ct').innerHTML = x1;
    display_c();
     }
    