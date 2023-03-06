<template>
<div>
    <!-- HTML TO DISPLAY USER RESULTS -->
    <div v-for="(user, index) in searchRes" :key="index">
        {{ user.username }}
    </div>
</div>
</template>

<script>
export default{
    name: "SearchResults",
    props: ['query'],
    data() {
        return {
            searchRes: "",
        }
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

<style>

</style>