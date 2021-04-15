<template>

<div class="node_box">
 
    <div class="chartheader">
      <h3>Node network</h3>
            <div class="help-tip-container">
                <div class="help-tip">
                    <p>The top posts is the 3 tweets with the most retweets. The reason it is sorted by retweets and not likes is because more retweets means a wider reach.</p>
                </div>
            </div>
    </div>

<div class="node_container">
<div id="graph">
  <svg xmlns="http://www.w3.org/2000/svg" 
       :width="width+'px'"
       :height="height+'px'"
       @mousemove="drag($event)"
       @mouseup="drop()"
       v-if="bounds.minX"
       :messages="{empty: 'No data'}"
       >
    
    <line v-for="link in graph.links"
          :x1="coords[link.source.index].x"
          :y1="coords[link.source.index].y"
          :x2="coords[link.target.index].x"
          :y2="coords[link.target.index].y"
          stroke="#aaa" stroke-width="1" v-bind:key="link"/>

    <g class="item" transform="translate(0, 0)" v-for="(node, i) in graph.nodes"
    :key="i"
    > 
      <circle class="node circle-node" 
              :cx="coords[i].x"
              :cy="coords[i].y"
              :r="graph.nodes[i].size" :fill="colors[Math.ceil(Math.sqrt(node.index))]"
              stroke="white" stroke-width="1"
              @mousedown="currentMove = {x: $event.screenX, y: $event.screenY, node: node}" v-bind:key="i"
            
              />
      <text
      class="node-text"
      :x="coords[i].x"
      :y="coords[i].y"
      @mouseover="showIndex = i"
      @click="gotowebpage(node.id)"
      :class="{'text-active': showIndex === i}"
      >{{node.id}}</text>
    </g>
  </svg>
</div>
</div>

</div>
</template>


<script>
import * as d3 from "d3";

export default {
  el: "#graph",
  props:['listdata'],
  data: function(){
    return{
    graph: {
      nodes: this.listdata.nodes,
      links: this.listdata.links
    },
    width: 500,
    height: 400,
    padding: 20,
    colors: ['#696969','#696969','#696969','#696969','#696969','#696969','#696969','#696969', '#696969', '#696969', '#696969', '#696969', '#696969', '#696969', '#696969', '#696969'],
    simulation: null,
    currentMove: null,
    label: null,
    showIndex: 0
    }
  },
  computed: {
    nodes(){
      console.log(this.listdata.nodes)
      console.log(this.listdata.links)
      //this.changenodes(this.$store.state.nodes)
      //return this.$store.state.nodes
      return {}
    },
    links(){
      //this.changelinks(this.$store.state.links)
      //return this.$store.state.links
      return {}
    },
    bounds() {
      return {
        minX: Math.min(...this.graph.nodes.map(n => n.x)),
        maxX: Math.max(...this.graph.nodes.map(n => n.x)),
        minY: Math.min(...this.graph.nodes.map(n => n.y)),
        maxY: Math.max(...this.graph.nodes.map(n => n.y))
      }
    },
    coords() {
      return this.graph.nodes.map(node => {
        return {
          x: this.padding + (node.x - this.bounds.minX) * (this.width - 5*this.padding) / (this.bounds.maxX - this.bounds.minX),
          y: this.padding + (node.y - this.bounds.minY) * (this.height - 2*this.padding) / (this.bounds.maxY - this.bounds.minY)
        }
      })
    }   
  },
  created(){
     this.simulation = d3.forceSimulation(this.graph.nodes)
        .force('charge', d3.forceManyBody().strength(-100))
        .force('link', d3.forceLink(this.graph.links).id(function(d) { return d.id;}))
        .force('x', d3.forceX())
        .force('y', d3.forceY())
    this.createTextNodes() 
  },
  methods: {
    drag(e) {
      if (this.currentMove) {
        this.currentMove.node.fx = this.currentMove.node.x - (this.currentMove.x - e.screenX) * (this.bounds.maxX - this.bounds.minX) / (this.width - 2 * this.padding)
        this.currentMove.node.fy = this.currentMove.node.y -(this.currentMove.y - e.screenY) * (this.bounds.maxY - this.bounds.minY) / (this.height - 2 * this.padding)
        this.currentMove.x = e.screenX
        this.currentMove.y = e.screenY
      }
    },
    drop(){
      delete this.currentMove.node.fx
      delete this.currentMove.node.fy    
      this.currentMove = null
      this.simulation.alpha(1)
      this.simulation.restart()
    },
    changenodes(newnodes){
      this.graph.nodes = newnodes
    },
    changelinks(newlinks){
      this.graph.links = newlinks
      
    },
    addLabel(nodes){
      for (let i in nodes){
        nodes[i].append("text")
        .text(function(d) {
        return d.id;
      })
      .attr('x', 6)
      .attr('y', 3);
      }
    },
    createTextNodes() {
      let nodes = d3.selectAll("circle");
      console.log(nodes);
      if (nodes.length > 0) {
        nodes.forEach(node => {
        let n = node.append("svg").attr("width", 10).attr("height", 10); 
        n.append("text")
        .attr('x', 10)
        .attr('y', 10)
        .attr('stroke', 'green')
        .style("font-size", 11)
        .text("text")
      });  
      }
    },
    gotowebpage(username){
      window.open(`https://www.twitter.com/${username}`)
    }
  }
}

</script>

<style scoped>

.chartheader{
    height: 45px;
    display: flex;
}
.chartheader h3{
    font-weight: 900;
    font-size: 1.25em;
    line-height: 1.5;
}

.node-text {
  opacity: 0;
}
.text-active {
  opacity: 1;
}
.node_container{
  border: 1px solid #dddfea;
  align-items: center;
  height: 450px;
  padding-top: 25px;
  padding-left: 55px;
  
}

.graph{
padding-left: 30px;

}

.header{
  display: flex;
  padding: 10px;
  font-family: Quicksand,Helvetica,Arial,sans-serif;
  font-weight: 900;
  font-size: 1.25em;
  line-height: 1.5;
  color: #26293c;
}

</style>