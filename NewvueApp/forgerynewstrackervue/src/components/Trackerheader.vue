<template>
    <div class="trackerheader_wrapper">
        
        <div class="trackerheader_title">
        <p>Real Time Tracker:</p>     
        <h1 class="display-1">
            <strong>"TRACKER"</strong>
        </h1>
        </div>

        <div class="trackerheader_filters">
            <label class="platformbox">
                <input type="checkbox" class="twitterchecbox">
                <img src="../assets/logo.png" class="checkboxpic">
                <input type="checkbox" class="twitterchecbox">
                <img src="../assets/logo.png" class="checkboxpic">
                <input type="checkbox" class="twitterchecbox">
                <img src="../assets/logo.png" class="checkboxpic">
            </label>
           
        </div>
    
    </div>
</template>

<script>


export default {
    name: "Trackerheader"

}
</script>

<style scoped>



.trackerheader_title{
    float: left;
    
}

.trackerheader_filters{
    position: absolute;
    right: 0    
}

.checkboxpic{
    width: 10%;
}

</style>
