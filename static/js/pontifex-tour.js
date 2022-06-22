//$(function() {
  
  // define tour
  var tour = new Tour({
    debug: true,
    basePath: location.pathname.slice(0, location.pathname.lastIndexOf('/')),
    steps: [{
      element: "#edge-message-top",
      title: "The Network",
      content: "Visualizes the network"
    }, {
      element: "#edge-message",
      title: "Title of my step",
      content: "Content of my step"
    }]
  });

  // init tour
  tour.init();

  // start tour
  //$('#start-tour').click(function() {
  //  tour.restart();
  //});
  tour.start();
  

//});

