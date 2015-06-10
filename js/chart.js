var width = 300,
    height = 300,
    radius = Math.min(width, height) / 2,
    innerRadius = 0.3 * radius;
var largestScore = 1.0;
var largestLike = 1.0;

function updateChart(name){
  d3.select("#circular_chart").select("svg").remove();
  largestScore = 1.0;
  largestLike = 1.0;

  var pie = d3.layout.pie()
      .sort(null)
      .value(function(d) { return d.width; });

  var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([0, 0])
    .html(function(d) {
      return "<div>" + d.data.filter_name + ": <span style='color:orangered'>" + d.data.score + Math.floor(Math.random() * 10) + "</span></div>"
      + "<img width='80px' src='" + d.data.img1 + "'>"
      + "<img width='80px' src='" + d.data.img2 + "'>"
      + "<img width='80px' src='" + d.data.img3 + "'>"
      + "<img width='80px' src='" + d.data.img4 + "'>";
    });

  var arc = d3.svg.arc()
    .innerRadius(innerRadius)
    .outerRadius(function (d) { 
      return (radius - innerRadius) * (Math.log(d.data.score) / Math.log(largestScore)) + innerRadius; 
    });

  var outlineArc = d3.svg.arc()
          .innerRadius(innerRadius)
          .outerRadius(radius);

  var svg = d3.select("#circular_chart").append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  svg.call(tip);

  d3.csv('filter_data/'+name+'.csv', function(error, data) {

    data.forEach(function(d) {
      d.color  = d.color;
      d.score  = d.score;
      d.width  = 1;
      d.filter_name  =  d.filter_name;
      if (parseFloat(d.score) > largestScore) largestScore = parseFloat(d.score);
      if (parseFloat(d.avg_like) > largestLike) largestLike = parseFloat(d.avg_like);
    });
    
    var path = svg.selectAll(".solidArc")
        .data(pie(data))
      .enter().append("path")
        .attr("fill", function(d) {
          domain = null,
          range = ["white", "green"],
          color = d3.scale.linear().domain([0,largestLike]).range(["white","green"]);
          return color(d.data.avg_like);
        })
        .attr("class", "solidArc")
        .attr("stroke", "gray")
        .attr("d", arc)
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide);

    svg.append("svg:text")
      .attr("class", "aster-score")
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .text(name);
  });
}