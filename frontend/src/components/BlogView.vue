<template>
<div>
    <header>
      <HomeNav />
    </header>
    <div v-if="flag === ''" class="main-blogpage">
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
    <div class="main-blogpage" v-else>
        {{ this.flag }}
    </div>
</div>
</template>

<script>
import HomeNav from "./HomeNav.vue";
export default{
    name: "BlogView",
    components: {
      HomeNav,
    },
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
header {
    width: 100%;
    background-color: rgb(243, 246, 247);
    padding: 10px;
    padding-bottom: 0px;
    border: 20px;
    border-bottom: 2px solid #494949;
}
.main-blogpage{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgb(255, 248, 248);
}
#content{
    margin-right: 600px;
    margin-left: 600px;
}
</style>