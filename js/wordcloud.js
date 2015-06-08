var fill = d3.scale.category20();
function updateWordCloud (name) {
  var tagData = [];
  var maxLike = 1;

  d3.select("#wordcloud").select("svg").remove();

  d3.csv('tag_count/'+name+'.csv', function(data) {
      data.forEach(function (d) {
          tagData.push([d.wordlist, d.avelike]);
          if (d.avelike > maxLike) maxLike = d.avelike;
      });

      d3.layout.cloud().size([500, 500])
          .words(tagData.map(function(d) {
              return {text: d[0], size: d[1]};
          }))
          .rotate(function() { return ~~(Math.random() * 2)*90; })
          .font("Impact")
          .fontSize(function(d) { return d.size*40/maxLike; })
          .on("end", draw)
          .start();
  });
}


function draw(words) {
  d3.select("#wordcloud").append("svg")
      .attr("width", 300)
      .attr("height", 300)
    .append("g")
      .attr("transform", "translate(150,150)")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
}