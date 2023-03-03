<template>
    <div>
      <header>
        <NavBar />
      </header>
      <div id = "content-jumbotron" class = "jumbotron">
        <div class = "jumbotron-content" >
            <h1 class="display-4">Start Unleashing your creativity</h1>
            <p class="lead">This is a simple example of a Bootstrap Jumbotron.</p>
            <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
            <a class="btn btn-primary btn-lg" role="button">Start Reading</a>
        </div>
      </div>
    </div>
</template>
  
<script>
import NavBar from './NavBar.vue';
export default {
  name: 'FrontPage',
  inheritAttrs: false,
  components: {
    NavBar,
  },
  data() {
    return {
      message: "Get Started!",
      path_url: "./login"
    }
  },
  mounted(){
    const path = window.location.href;
    if(path.includes("login")){
      if(this.message == "Get Started!"){
        this.message = "Welcome Back."
        this.path_url = "./signup"
        let element = document.getElementById("email");
        element.remove();
      }
    }
  }, 
}
</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@500&display=swap');
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  body {
    font-family: 'montserrat', sans-serif;
  }
  header {
    width: 100%;
    background-color: rgb(179, 238, 248);
    padding: 10px;
    border: 20px;
    border-bottom: 2px solid #494949;
  }
  #content-jumbotron{
    margin-right:0px;
    background-color: rgb(179, 238, 248);
    width: 100%;
    float:left;
    border-bottom: 2px solid #494949;
    border-radius: 0;
  }
  .jumbotron-content{
    margin: 4% 0% 4% 10%;
  }
  .card{
    width: 65%;
    height: 70%;
    border: 2px outset rgb(247, 166, 15);
    border-radius: 0;
    box-shadow: none;
    justify-content: center;
  }
  li{
    border:0;
    box-shadow: 0;
    justify-content: center;
    text-align: center;
  }
  .list-group, .list-group-flush{
    border:0;
    box-shadow: 0;
  }
  p, h1, h2, h3{
    font-family: 'Josefin Sans', sans-serif;
  }

  #email, #username, #password{
    margin-bottom: 10px;
    width: 80%;
    padding: 10px;
    font-size: 17px;
    border: 2px solid rgb(245, 243, 239);
    border-radius: 20px;
    outline: none;
    transition: background-color 0.2s ease-in-out;
  }
  
  input:hover{
    background-color: rgb(243, 208, 143);
  }
</style>