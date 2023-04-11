// Message Time Out

setTimeout(function () {
    let alert_messages = document.getElementById('msgs');
    let alert = new bootstrap.Alert(alert_messages);
    alert.close();
  }, 2500);

// Nav Icon: X icon / Hamburger icon switch
  function navIcon() {

    if (document.getElementById("sc-menu-icon").innerHTML == '<i class="fa-solid fa-bars white-text"></i>') {
      document.getElementById("sc-menu-icon").innerHTML = '<i class="fa-solid fa-x blue-text"></i>';
    } else {
      document.getElementById("sc-menu-icon").innerHTML = '<i class="fa-solid fa-bars white-text">';
    }
  }