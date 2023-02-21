<template>
<div>
    <header>    
        <HomeNav />
    </header>
    <div id = "main-my-blogs" class = "container">
        <div class = "follower-blogs">
            <div style="margin-left: 1%;
                        margin-top: 5%;
                        margin-bottom: 2%;
                        border-bottom: 1px solid black;">
                <h2>
                  <b v-if="!isProfile">Your Stories</b>
                  <b v-else >{{ user }}</b>
                </h2>
            </div>
            <div id = "blog-container" v-for="post in followerPosts" :key="post.id">
                <BlogCard :post="post" :publisher="true" @post-deletion="location.reload()"/>
            </div>
        </div>
        <div class = "div-reccom">
            <!-- <div v-if="!isProfile" class = "div-recc-topics">Recommended Topics</div>
            <div v-else class = "div-recc-topics">
              
            </div>
            <div v-if="!isProfile" class = "div-recc-blogs">Recommended Blogs</div>
            <div v-else class = "div-recc-topics">
            </div> -->
            <slot></slot>
        </div>
    </div>
</div>
</template>

<script>
import HomeNav from "../HomeNav.vue";
import BlogCard from "../BlogCard.vue"
export default {
    components: {
        HomeNav,
        BlogCard
    },
    props: ["user", "isProfile"],
    data() {
        return {
            followerPosts: [],
            current_user: "",
        }
    },
    created(){
      // Get details about the current user.
      if(this.user !== ""){
        const userPath = `http://127.0.0.1:5000/api/${this.$route.params.username}`;
        fetch(userPath, {
          headers: {"Authorization": localStorage.jwtToken}
        })
        .then(reponse => reponse.json())
        .then(data => this.current_user = data);
      }
    },
    mounted() {
      // Used to get blogs by the current user.
      if(this.user === localStorage.username){
        const path1 = `http://127.0.0.1:5000/api/${this.$route.params.username}/my-blogs`;
        fetch(path1, {
          headers: {"Authorization": localStorage.jwtToken}
        })
        .then(response => response.json())
        .then(data => {
          this.followerPosts = data
        });
      }
      // Get blogs of the other user if user != current user.
      else{
        const path1 = `http://127.0.0.1:5000/api/blogs/${this.user}`;
        fetch(path1, {
          headers: {"Authorization": localStorage.jwtToken}
        })
        .then(response => response.json())
        .then(data => {
          this.followerPosts = data
        });
      }
    },
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
.main-my-blogs{
  background-color: rgb(255, 248, 248);
  margin-top: 2%;
  margin-left: 18%;
  margin-right: 0%;
  align-items: center;
  justify-content: center;
}
.follower-blogs{
  float:left;
}

#blog-container{
  width: 100%;
  margin-right: 5%;
}
.div-reccom{
  float: right;
  height: 100vh;
  justify-content: center;
  /* margin-top: 2%; */
  width: 40%;
  border-left: 1px solid black;
}
/* .div-recc-topics{
  height: 50vh;
  background-color: red;
}
.div-recc-blogs{
  height: 50vh;
  background-color: blue;
} */
</style>