window. addRow = function addRow(btn) {   
    const options=["click","Enter","GetTitle","Clear","Input"];      
    var parentRow = btn.parentNode.parentNode;
    var table = parentRow.parentNode;
    var rowCount = table.rows.length;
    
    var row = table.insertRow(rowCount);
  
    var cell1 = row.insertCell(0);
    var element1 = document.createElement("input");
    element1.type = "text";
    element1.name="Xpath_info";
    element1.placeholder="Xpath";
    cell1.appendChild(element1);
    var cell2 = row.insertCell(1);
    var element3 = document.createElement("input");
    element3.type="text";
    element3.id="ifYes";
    element3.name="Input_text_1";
    element3.style="display: none;";
    cell2.appendChild(element3);
    var cell3 = row.insertCell(2);
    var element2 = document.createElement("select");
    element2.name="Actions";
    element2.addEventListener("change",yesnoCheck);
    //element2.type = "select";
    for(let i=0;i<options.length;i++)
    {
    var option1 = document.createElement("option");
    option1.innerHTML = options[i];
    option1.value = options[i];
    element2.add(option1);
    cell3.appendChild(element2);
    }
    // var option2 = document.createElement("option");
    // option2.innerHTML = "Enter";
    // option2.value = "2";
    // element2.add(option2, null);
  }
  
  window. Delete = function Delete(btn) { 
    var parentRow = btn.parentNode.parentNode;
    var table = parentRow.parentNode;
    var rowCount = table.rows.length;
    if(rowCount!=1)
    {
    table.deleteRow(rowCount-1);
    }
  }
  
  function yesnoCheck() {
    let test,data,i;
    test = document.getElementsByName("Actions");
    data = document.getElementsByName("Input_text_1");
    for(i=0;i<test.length;i++)
    {
    if (test[i].value == "Input" && data[i].style.display != "block") 
    {
    alert("This field is to send data");
        data[i].style.display = "block";
    }
    if (test[i].value != "Input" && data[i].style.display == "block")
    {
        alert("The Input field is changed");
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
    