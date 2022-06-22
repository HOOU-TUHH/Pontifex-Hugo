// Instance the tour
var tour = new Tour({
  steps: [
  {
    element: "#cy",
    title: "Title of my step",
    content: "Content of my step"
  },
  {
    element: "#cy",
    title: "Title of my step",
    content: "Content of my step"
  }
]});

// Initialize the tour
tour.init();

// Start the tour
tour.start();