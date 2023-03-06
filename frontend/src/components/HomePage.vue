<template>
  <div>
    <header>
      <HomeNav />
    </header>
    <div id = "main-homepage" class = "container">
      <div class = "follower-blogs">
        <div id = "blog-container" v-for="post in followerBlogs" :key="post.id">
          <BlogCard :post="post" :publisher="false"/>
        </div>
      </div>
      <div class = "div-reccom">
        <div class = "div-recc-topics">Recommended Topics</div>
        <div class = "div-recc-blogs">Recommended Blogs</div>
      </div>
    </div>
    
  </div>
</template>

<script>
import HomeNav from "./HomeNav.vue";
import BlogCard from "./BlogCard.vue"
export default {
    components: {
      HomeNav,
      BlogCard,
    },
    data() {
        return {
            followerBlogs: [],
            userSuggestions: [],
            current_user: "",
        }
    },
    created(){
      // Get details about the current user.
      const userPath = `http://127.0.0.1:5000/api/${this.$route.params.username}`;
      fetch(userPath, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(reponse => reponse.json())
      .then(data => this.current_user = data);
    },
    mounted() {
      // Used if user has followers.
      const path1 = `http://127.0.0.1:5000/api/${this.$route.params.username}/homepage`;
      fetch(path1, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(response => response.json())
      .then(data => {
        this.followerBlogs = data
      });

      // Used if user has no followers.
      const path2 = `http://127.0.0.1:5000/api/${this.$route.params.username}/homepage`;
      fetch(path2, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(response => response.json())
      .then(data => {
        this.userSuggestions = data
      });
    },
}

</script>

<style scoped>
.follower-blogs{
  float:left;
}
#blog-container{
  width: 105%;
  margin-right: 5%;
}
#main-homepage{
  background-color: rgb(255, 248, 248);
  margin-top: 2%;
  margin-left: 18%;
  margin-right: 0%;
  align-items: center;
  justify-content: center;
}
header {
    width: 100%;
    background-color: rgb(243, 246, 247);
    padding: 10px;
    padding-bottom: 0px;
    border: 20px;
    border-bottom: 2px solid #494949;
}

.div-reccom{
  float: right;
  text-align: center;
  justify-content: center;
  margin-top: 2%;
  width: 40%;
}
.div-recc-topics{
  height: 50vh;
  background-color: red;
}
.div-recc-blogs{
  height: 50vh;
  background-color: blue;
}
</style>