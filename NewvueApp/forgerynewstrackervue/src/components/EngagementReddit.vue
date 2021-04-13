<template>
    <div>
    <div class="engagement-wrapper" v-show="listdata1.query != '' && listdata2.query == ''">
        <div class="engagement-container">

            <div class="topstats" data-bs-toggle="tooltip" data-bs-placement="top" title="The number of posts made with your tracked hashtag, keyword, URL and/or @mention." >
                <fa icon="comments" size="2x"/>
                    <h1>{{listdata1.engagementreddit.posts}}</h1>
                <p>Posts</p>
            </div>
            
            <div class="topstats" data-bs-toggle="tooltip" data-bs-placement="top" title="The number of users who have posted with your tracked hashtag, keyword, URL and/or @mention.">
                <fa icon="user" size="2x"/>
                <h1>{{listdata1.engagementreddit.users}}</h1>
                <p>Users</p>
            </div>

            <div class="topstats" data-bs-toggle="tooltip" data-bs-placement="top" title="When someone intentionally interacts with your post, that is considered an engagement. We factor in the following kinds of engagement:Twitter: Retweets + Likes" >
                <fa icon="heart" size="2x"/>
                <h1 class="display display-">{{listdata1.engagementreddit.engagement}}</h1>
                <p>Engagement</p>
            </div>
        </div>
    </div>

    <div class="engagement-wrapper" v-show="listdata1.query != '' && listdata2.query != ''">
        <div class="engagement-container">

            <div class="topstats" data-bs-toggle="tooltip" data-bs-placement="top" title="The number of posts made with your tracked hashtag, keyword, URL and/or @mention." >
                <fa icon="comments" size="2x"/>
            <div class="stats">
                    <h3>{{listdata1.engagementreddit.posts}}</h3>
                    <h5>&nbsp;vs&nbsp;</h5> 
                    <h3>{{listdata2.engagementreddit.posts}}</h3>
            </div>
                
                <p>Posts</p>
            </div>
            
            <div class="topstats" data-bs-toggle="tooltip" data-bs-placement="top" title="The number of users who have posted with your tracked hashtag, keyword, URL and/or @mention.">
                <fa icon="user" size="2x"/>
                 <div class="stats">
                    <h3>{{listdata1.engagementreddit.users}}</h3>
                    <h5>&nbsp;vs&nbsp;</h5> 
                    <h3>{{listdata2.engagementreddit.users}}</h3>
                </div>
                <p>Users</p>
            </div>

            <div class="topstats" data-bs-toggle="tooltip" data-bs-placement="top" title="When someone intentionally interacts with your post, that is considered an engagement. We factor in the following kinds of engagement:Twitter: Retweets + Likes" >
                <fa icon="heart" size="2x"/>
                 <div class="stats">
                    <h3>{{listdata1.engagementreddit.engagement}}</h3>
                    <h5>&nbsp;vs&nbsp;</h5> 
                    <h3>{{listdata2.engagementreddit.engagement}}</h3>
                </div>
                <p>Engagement</p>
            </div>
        </div>
    </div>
    </div>
</template>

<script>

export default {
    name: "engagementreddit",
    props:['listdata1', 'listdata2'],
    
}
</script>

<style scoped>
.engagement-wrapper{
    
    height: 150px;
    background-color: #ffd443;
    display: flex;
    justify-content: center;
    align-items: center;
 
}

.engagement-container{
    justify-content: space-evenly;
    margin: auto;
    display: flex;
    width: 100%;
    min-width: none;

}



.topstats{
    width: 100px;
    height: 70px;
    display: grid;
    grid-template-columns: 3em auto;
    grid-template-rows: 1fr 1em;
    margin-right: 120px;

}
.stats{ 
    width: 100px;
    display: inline-flex;
    align-items: center;
    line-height: 10px;  
}


</style>