<template>
    <div>
      <header>
        <NavBar />
      </header>
      <div id = "content-jumbotron" class = "jumbotron">
        <div class = "jumbotron-content" style = "margin-left: 15.5%;">
            <h1 class="display-4">Start Unleashing your creativity</h1>
            <p class="lead">This is a simple example of a Bootstrap Jumbotron.</p>
            <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
            <a class="btn btn-primary btn-lg" role="button">Start Reading</a>
        </div>
      </div>
      <div id ="auth-jumbotron" class = "jumbotron">
        <div id = "auth-jumbotron-content" class = "jumbotron-content">
          <div class="card">
            
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <div>
                  <p class = "auth-message">
                    {{ message }}
                  </p>
                </div>
                <div>
                  <form>
                    <div>
                      <input type="email" id="email" name="email" placeholder = "Enter Email" autocomplete = "off" required>
                    </div>
                    <div>
                      <input type="text" id="username" name="username" placeholder = "Enter username"  autocomplete = "off" required>
                    </div>
                    <div>
                      <input type="password" id="password" name="password"  placeholder = "Enter password" autocomplete = "off" required>
                    </div>
                    <input type="submit" value="Sign Up">
                  </form>
                  <div>
                    Already a user? 
                    <a :href="`${path_url}`">
                      Log In
                    </a>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script>
import NavBar from './NavBar.vue';
  export default {
    name: 'FrontPage',
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
      // console.log(typeof path);
      if(path.includes("login")){
        if(this.message == "Get Started!"){
          this.message = "Welcome Back."
          this.path_url = "./signup"
          let element = document.getElementById("email");
          console.log(element);
          element.remove();

        }
      }
    },
  }
</script>
  
<style>
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
    width: 70%;
    float:left;
    border-bottom: 2px solid #494949;
    border-radius: 0;
  }

  #auth-jumbotron{
    background-color: rgb(235, 199, 134);
    width: 30%;
    height: 100vh;
    float:right;
    border-left: 2px solid #494949;
    border-radius: 0;
  }

  #auth-jumbotron-content{
    display: flex;
    justify-content: center;
    height: 100%;
    width: 100%;
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
  .auth-message{
    font-family: 'Josefin Sans', sans-serif;
    font-size: 40px;
  }
</style>