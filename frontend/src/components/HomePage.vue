<template>
  <div>
    <header>
      <HomeNav />
    </header>
  </div>
</template>

<script>
// NEED TO DESTROY THE TOKEN WHEN A USER LOGS OUTTTTTTT.
import HomeNav from "./HomeNav.vue";
export default {
    components: {
      HomeNav,
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
      console.log(this.current_user);
      console.log(this.current_user);
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

<style>
header {
    width: 100%;
    background-color: rgb(243, 246, 247);
    padding: 10px;
    border: 20px;
    border-bottom: 2px solid #494949;
  }
</style>