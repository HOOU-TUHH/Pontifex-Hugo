  let cy = cytoscape({
    container: document.getElementById("cy"), // container to render in

    elements: [
      // list of graph elements to start with
      // { group: 'nodes',data: { id: 'n1' }, position: { x: 200, y: 100 } },
      // { group: 'nodes',data: { id: 'n2' }, position: { x: 100, y: 50 } },
      // { group: 'edges',data: { id: 'e0', source: 'n1', target: 'n2' } }
    ],

    style: [
      // the stylesheet for the graph
      {
        selector: "node",
        style: {
          "background-color": "#69e",
          label: "data(id)",
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
        "line-color": "#369",
        "target-arrow-color": "#369",
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
        width: "data(size)",
        height: "data(size)",
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
      name: "grid",
      rows: 1,
    },
  });

  cy.add(
[
{
      "data": {
            "id": "000",
            "label": "Logic and Sets",
            "meta": " SLL01",
            "content": "Logic is the foundation to formulate proofs and to understand the language of mathematics.",
            "notes": "000-snippet.html",
            "video": "https://www.youtube.com/embed/DU4wKBDm2Z4?start=7",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=Library/SDSU/Discrete/Logic/ttcontratautB4.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://etherpad.studiumdigitale.uni-frankfurt.de/p/klfjsdklfjadsfkjdslkaf000?showControls=true&showChat=true&showLineNumbers=true&useMonospaceFont=false",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 400,
            "y": 60
      }
},
{
      "data": {
            "id": "100",
            "label": "Sequences",
            "meta": " RA02 ",
            "content": "These object are needed to define limits later on.",
            "notes": "100-snippet.html",
            "video": "https://www.youtube.com/embed/1SguKALJji8?start=17",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=Library/UMN/calculusStewartCCC/s_11_1_5.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://etherpad.studiumdigitale.uni-frankfurt.de/p/klfjsdklfjadsfkjdslkaf100?showControls=true&showChat=true&showLineNumbers=true&useMonospaceFont=false",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 300,
            "y": 160
      }
},
{
      "data": {
            "id": "200",
            "label": "Series",
            "meta": "RA15",
            "content": "Ein Satz",
            "notes": "200-snippet.html",
            "video": "https://www.youtube.com/embed/",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://pads.rz.tuhh.de/p/",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 400,
            "y": 260
      }
},
{
      "data": {
            "id": "300",
            "label": "Continuous Functions",
            "meta": "RA23",
            "content": "Ein Satz",
            "notes": "300-snippet.html",
            "video": "https://www.youtube.com/embed/",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://pads.rz.tuhh.de/p/",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 300,
            "y": 360
      }
},
{
      "data": {
            "id": "400",
            "label": "Elementary Functions",
            "meta": "RA33",
            "content": "Ein Satz",
            "notes": "400-snippet.html",
            "video": "https://www.youtube.com/embed/",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://pads.rz.tuhh.de/p/",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 400,
            "y": 460
      }
},
{
      "data": {
            "id": "500",
            "label": "Differentiation",
            "meta": "RA34",
            "content": "Ein Satz",
            "notes": "500-snippet.html",
            "video": "https://www.youtube.com/embed/",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://pads.rz.tuhh.de/p/",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 300,
            "y": 560
      }
},
{
      "data": {
            "id": "600",
            "label": "Integration",
            "meta": "RA48",
            "content": "Ein Satz",
            "notes": "600-snippet.html",
            "video": "https://www.youtube.com/embed/",
            "webwork": "https://demo.webwork.rochester.edu/webwork2/html2xml?&answersSubmitted=0&sourceFilePath=.pg&problemSeed=123567890&displayMode=MathJax&courseID=daemon_course&userID=daemon&course_password=daemon&outputformat=simple",
            "discussion": "https://pads.rz.tuhh.de/p/",
            "size": 105
      },
      "group": "nodes",
      "position": {
            "x": 400,
            "y": 660
      }
},
{
      "data": {
            "source": "000",
            "target": "100",
            "label": " "
      },
      "group": "edges"
},
{
      "data": {
            "source": "100",
            "target": "200",
            "label": " "
      },
      "group": "edges"
},
{
      "data": {
            "source": "200",
            "target": "300",
            "label": " "
      },
      "group": "edges"
},
{
      "data": {
            "source": "300",
            "target": "400",
            "label": " "
      },
      "group": "edges"
},
{
      "data": {
            "source": "400",
            "target": "500",
            "label": " "
      },
      "group": "edges"
},
{
      "data": {
            "source": "500",
            "target": "600",
            "label": " "
      },
      "group": "edges"
}
]
  );
  cy.userZoomingEnabled( false );
  cy.userPanningEnabled( false );
  cy.on("click", "node", node_clicked);
  cy.on("tap", "node", node_clicked);
  
  function node_clicked(evt) {
    var node = evt.target;
    const index = node.data()["id"];
    const first = index[0];
    window.open(`../chapter${first}/${index}/`,"_self")
  };

  cy.on("click", "edge", function (evt) {
    var edge = evt.target;
    console.clear();
    console.log(edge.id());
    if (edge.style("label") == "") {
      edge.style("label", edge.data("label"));
    } else {
      edge.style("label", "");
    }
  })