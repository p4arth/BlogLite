<template>
<div class="container">
    <div v-if="flag === ''">
        <div id="title">
            <h1>
                {{ post.title }}
            </h1>
        </div>
        <div id="image">
            <img :src="post.image_url" style="width:500px;height:300px">
        </div>
        <div id="content" v-html="post.caption"></div>
    </div>
    <div v-else>
        {{ this.flag }}
    </div>
</div>
</template>

<script>
export default{
    name: "BlogView",
    data() {
        return {
            post: "",
            flag: ""
        }
    },
    created(){
        const path = `http://127.0.0.1:5000/api/get/post/${this.$route.params.post_id}`;
        const response = fetch(path, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            const postData = async () => {
                this.post = await response;
                console.log(this.post);
                if (this.post.username !== this.$route.params.username){
                    this.flag = "YOU SNEAKY FUCKERRR";
                }
            }
        postData();
    }
}
</script>

<style scoped>

</style>