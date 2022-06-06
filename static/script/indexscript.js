function yesnoCheck() {
    let test,data,i;
    test = document.getElementsByName("Actions");
    data = document.getElementsByName("Input_text_1");
    for(i=0;i<test.length;i++)
    {
    if (test[i].value == "Input") {
    alert("This field is to send data");
        data[i].style.display = "block";
    } else {
        data[i].style.display = "none";
    }
}
}
function display_c(){
    var refresh=1000; // Refresh rate in milli seconds
    mytime=setTimeout('display_ct()','yesnoCheck()',refresh)
}// This is used to display the clock under the span
function display_ct() {
    var x = new Date()
    var ampm = x.getHours( ) >= 12 ? ' PM' : ' AM';
    var x1=x.getMonth() + 1+ "/" + x.getDate() + "/" + x.getFullYear(); 
    x1 = x1 + " - " +  x.getHours( )+ ":" +  x.getMinutes() + ":" +  x.getSeconds() + "--" +ampm;
    document.getElementById('ct').innerHTML = x1;
    display_c();
     }
    