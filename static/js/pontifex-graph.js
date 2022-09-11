/*
This is the js file loading the node specific json file and 
crating the corresponding CytoJS graph
*/
$.getJSON(current_id + ".json" , function (data) {

  var cy = cytoscape({
    container: document.getElementById("cy"),
    elements: data,

    style: cytoscape
      .stylesheet()
      .selector("edge")
      .css({
        width: 8,
        "line-color": 'data(color)',
        "target-arrow-color": "data(color)",
        "target-arrow-shape": "triangle",
        label: "", //'data(label)',
        "font-size": "14px",
        "curve-style": "bezier",
        color: "white",
        "text-outline-width": 2,
        "text-outline-color": "#888",
        "background-color": "#888",
        "text-wrap": "wrap",
        "line-style": "data(style)",
      })
      .selector("node")
      .css({
        width: 70,
        height: 70,
        "text-wrap": "wrap",
        content: "data(label)",
        "text-valign": "center",
        color: "white",
        "text-outline-width": 2,
        "text-outline-color": "#1d2d35",
        "background-color": "data(color)",
      })
      .selector(":selected")
      .css({
        "background-color": "black",
        "line-color": "black",
        "target-arrow-color": "black",
        "source-arrow-color": "black",
        "text-outline-color": "black",
      }),

    layout: {
      name: "circle",
    },
  });
  cy.userZoomingEnabled( false );
  cy.userPanningEnabled( false )
  cy.on("tap", "node", node_clicked);
  cy.on("tap", "edge", edge_clicked);
  cy.getElementById(current_id).style("background-color", "#5d2f86"); //alt. border-color
}
);

function node_clicked(evt) {
  var node = evt.target;
  const index = node.data()["id"];
  const nr = index.slice(0, 1);
  if (index == current_id) {
    window.open(`../${index}/`,"_self")
  } else {
    window.open(`../../chapter${nr}/${index}/`,"_self")
  }
}

function edge_clicked(evt) {
  var edge = evt.target;
  console.clear();
  console.log(edge.style("label"));
  const std_text = "Click on an edge to get a description of the connection!";
  document.getElementById('edge-message').innerHTML = "<b>Description of the connection</b>: " +  edge.data("label");
}
