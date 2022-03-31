//$.getJSON("/nodes/" + current_id + "/" + current_id + ".json" , function (data) {
$.getJSON(current_id + ".json" , function (data) {
  console.log(data);

  var cy = cytoscape({
    container: document.getElementById("cy"),
    elements: data,
    style: [
      // the stylesheet for the graph
      {
        selector: "node",
        style: {
          "background-color": "#69e",
          label: "data(label)",
        },
      },

      {
        selector: "edge",
        style: {
          width: 1,
          "line-color": "#369",
          "target-arrow-color": "#369",
          "target-arrow-shape": "triangle",
          label: "data(label)",
          "font-size": "14px",
          color: "#777",
        },
      },
    ],

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
        "text-outline-color": "#888",
        "background-color": "#999999",
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

  cy.on("click", "node", node_clicked);
  cy.on("click", "edge", edge_clicked);
  cy.getElementById(current_id).style("background-color", "red"); //alt. border-color
}
);

function node_clicked(evt) {
  var node = evt.target;
  const index = node.data()["id"];
  if (index == current_id) {
    window.open(`../${index}/${index}-node.html`,"_self")
  } else {
    window.open(`../${index}/${index}.html`,"_self")
  }
}

function edge_clicked(evt) {
  var edge = evt.target;
  console.clear();
  console.log(edge.id());
  if (edge.style("label") == "") {
    edge.style("label", edge.data("label"));
  } else {
    edge.style("label", "");
  }
}