<template>
    <div class="geochart-box-container">
        <div class="chartheader">
            <h3>Locations</h3>
            <div class="help-tip-container">
                <div class="help-tip">
                    <p>The geo chart represents the location of the users tweeting or interacting with the tweets. We only get the location that the user has defined, so this chart is not 100% accurate.</p>
                </div>
            </div>
        </div>
        <div class="geochart-box">
            <div class="geochart-container">
                <geo-chart :data="listdata" :messages="{empty: 'No data'}" width="600px"></geo-chart>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: "geochart",
    props:['listdata'],

    
}
</script>

<style scoped>
.geochart-box{
    align-items: center;
    border: 1px solid #dddfea;
    padding: 20px;
    
    height: 450px;
   
}

.chartheader{
    height: 45px;
    display: flex;
}
.chartheader h3{
    font-weight: 900;
    font-size: 1.25em;
    line-height: 1.5;
}
.geochart-container{
    padding-top: 35px;
}
.help-tip-container{
    z-index: 100;
    padding: 2.5px 0px 0px 5px;
}
.help-tip{
    text-align: center;
    background-color: #BCDBEA;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    font-size: 14px;
    line-height: 25px;
    cursor: default;
}

.help-tip:before{
    content:'?';
    font-weight: bold;
    color:#fff;
}

.help-tip:hover p{
    display:block;
    transform-origin: 100% 0%;
    -webkit-animation: fadeIn 0.3s ease-in-out;
    animation: fadeIn 0.3s ease-in-out;

}

.help-tip p{    /* The tooltip */
    display: none;
    text-align: left;
    background-color: #1E2021;
    padding: 20px;
    width: 300px;
    border-radius: 3px;
    box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
    right: -4px;
    color: #FFF;
    font-size: 13px;
    line-height: 1.4;
}

.help-tip p:before{ /* The pointer of the tooltip */
    content: '';
    width:0;
    height: 0;
    border:6px solid transparent;
    border-bottom-color:#1E2021;

}

.help-tip p:after{ /* Prevents the tooltip from being hidden */
    width:100%;
    height:40px;
    content:'';
   
}

/* CSS animation */

@-webkit-keyframes fadeIn {
    0% { 
        opacity:0; 
        transform: scale(0.6);
    }

    100% {
        opacity:100%;
        transform: scale(1);
    }
}

@keyframes fadeIn {
    0% { opacity:0; }
    100% { opacity:100%; }
}


</style>

