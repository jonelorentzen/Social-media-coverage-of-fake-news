//Creating global variable that stores the dictionary pulled from the Twitter API storing all of the data from the tweets.
var allData;

//EventListener that calls the function start() when the site is loaded
window.addEventListener('DOMContentLoaded', () => start(), false);


// Async function that starts by fetching the data from the json response in the fetch() function. The fetch() function sets the allData variable to the dictionary with all of the data. 
// After the allData variable is set, we extract the public_metrics by the transform_data() function. It returns a list that is used as the parameter for plotting the chart by the chart() function.
async function start() {
    fetchdata().then(() => {
        console.log(allData);
        console.log(typeof allData);
        stat_list = transform_data(allData);
        top_retweets_list = sort_amountRT(allData);
        console.log("sorted list", top_retweets_list);
        chart(stat_list, top_retweets_list);
    }, false);
};

// Fetching the json response and setting it as the global allData variable.
async function fetchdata() {
    return fetch('http://127.0.0.1:5000/showinfo')
        .then(response => response.json())
        .then(data => {
            allData = data.data
        });
};

//showing/hiding bar-DIV
function barCanvas() {
    var x = document.getElementById("barCanvas");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

// Plotting the allData in the form of a bar chart
function chart(allData, top_retweets_list) {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Retweets', 'Likes', 'Reply', 'Quote'],
            datasets: [{
                label: "The most retweets is:" + top_retweets_list[0]["public_metrics"]["retweet_count"],
                data: allData,
                backgroundColor: [
                    'red',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 5
            }]
        },
        options: {
            scales: {
                x: {
                    stacked: true
                },
                y: {
                    stacked: true
                },
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
};

// Extracting the public metrics from allData
// The API returns 100 tweets that can be in the format for a orignal tweet, a reply to a tweet, a quote of a tweet or a retweet of a tweet
// The problem with the API is that most of 100 tweets we get from the API is retweets from another tweet
// A retweet only has the "retweet_count" from the orignal tweet
function transform_data(allData) {
    let total_retweets = 0
    let total_likes = 0
    let total_replies = 0
    let total_quotes = 0

    for (let i = 0; i < allData.length; i++) {
        if ("referenced_tweets" in allData[i]) {
            if (allData[i]['referenced_tweets']['0']["type"] !== "retweeted") {
                total_retweets += allData[i]['public_metrics']["retweet_count"]
                total_likes += allData[i]['public_metrics']["like_count"]
                total_replies += allData[i]['public_metrics']["reply_count"]
                total_quotes += allData[i]['public_metrics']["quote_count"]

            }
        } else {
            total_retweets += allData[i]['public_metrics']["retweet_count"]
            total_likes += allData[i]['public_metrics']["like_count"]
            total_quotes += allData[i]['public_metrics']["quote_count"]
            total_replies += allData[i]['public_metrics']["reply_count"]
        }
    }

    var total_list = [total_retweets, total_likes, total_quotes, total_replies]
    return total_list
};

// finding more of the person top 3 person that has got most retweets
// sort by amount of retweets
// send request with the three different ID´s
// retrieve more info about their account
// display information

function sort_amountRT(allData) {

    var orignal_tweets = []
    for (let i = 0; i < allData.length; i++) {
        if (!("referenced_tweets" in allData[i])) {
            orignal_tweets.push(allData[i]);
        }
    }
    orignal_tweets.sort((a, b)=>{ return b.public_metrics.retweet_count - a.public_metrics.retweet_count  })
    
    return orignal_tweets 
}