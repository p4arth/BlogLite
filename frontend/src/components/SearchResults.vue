<template>
<div>
    <header>    
        <HomeNav />
    </header>
    <!-- HTML TO DISPLAY USER RESULTS -->
    <div class = "container">
        <div class="clearfix" id="search-user-div" v-for="(user, index) in searchRes" :key="index">
            <div style="float:left">
                <b>
                    <a :href="`../${user.username}/profile`" style="color:inherit">
                        {{ user.full_name }}
                    </a>
                </b>
                <br>
                <small>{{ user.username }}</small>
            </div>
            <div>
                <img style="float:right" v-if="user.pfp_link" :src="user.pfp_link">
                <img style="float:right" v-else src="../assets/blankpropic.png">
            </div>
        </div>
    </div>
</div>
</template>

<script>
import HomeNav from './HomeNav.vue';
export default{
    name: "SearchResults",
    props: ['query'],
    data() {
        return {
            searchRes: "",
        }
    },
    components: {
        HomeNav,
    },
    mounted(){
        let currUrl =  `http://127.0.0.1:5000/api/search/`
        let queryString = "?q=" + encodeURIComponent(this.query);
        let fUrl = currUrl + queryString;
        fetch(fUrl, {
                methods: "GET",
                headers: {
                        'Content-Type': 'application/json',
                        'Authorization': localStorage.jwtToken,
                    },
                }
            )
            .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
            })
            .then(
                data => {
                    this.searchRes = data.results;
                    console.log(this.searchRes);
                }
            )
    }
}
</script>

<style scoped>
header {
    width: 100%;
    background-color: rgb(243, 246, 247);
    padding: 10px;
    padding-bottom: 0px;
    border: 20px;
    border-bottom: 2px solid #494949;
}
.container{
    margin-top: 0.5%;
}
#search-user-div{
    border: 1px solid black;
    border-radius: 10px;
    padding: 1%;
    margin: auto;
    width: 40%;
}
img {
    width: 10%;
    height: 10%;
}
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
</style>