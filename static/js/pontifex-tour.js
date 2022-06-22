//$(function() {
  
  // define tour
  var tour = new Tour({
    debug: true,
    basePath: location.pathname.slice(0, location.pathname.lastIndexOf('/')),
    steps: [{
      element: "#cy",
      title: "The Network",
      content: "Visualizes the network"
    }, {
      path: "/newPage.html",
      element: "#my-other-element",
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

