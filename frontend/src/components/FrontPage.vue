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
      <!-- <div id ="auth-jumbotron" class = "jumbotron">
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
                  <form id = "auth-form" @submit.prevent = "submit" method = "POST">
                    <div id = "email-div">
                      <input type="email" id="email" name="email" placeholder = "Enter Email" autocomplete = "off" required>
                    </div>
                    <div id = "username-div">
                      <input type="text" id="username" name="username" placeholder = "Enter username"  autocomplete = "off" required>
                    </div>
                    <div id = "password-div">
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
      </div> -->
    </div>
</template>
  
<script>
  import NavBar from './NavBar.vue';
  import axios from 'axios';
  import setAuthHeader from '../utils/setAuthHeader.js';
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
    methods: {
      submit: function(){
        const currPath = window.location.href;
        // Authenticats if the user is logging in.
        if(currPath.includes("login")){
          const loginPath = 'http://127.0.0.1:5000/api/login';
          const username = document.getElementById("username").value;
          const password = document.getElementById("password").value;
          const result = axios.post(loginPath,
                       {name: username, password: password}, 
                       {headers: {'Content-Type': 'application/json'}})
                       .then((response) => response.data)
                       .then((user) => {
                        return [user.username, user.status, user.auth_token];
                       });
          const loginChanges = async () => {
            const [username, status, token] = await result;
            if(status === "Authenticated"){
              localStorage.setItem("jwtToken", token);
              localStorage.setItem("currUser", username);
              setAuthHeader(token);
              console.log("hereeeeeeeee");
              const passwordDiv = document.getElementById("password-div");
              const newP =  document.createElement("p");
              newP.innerText = "Authenticated!";
              passwordDiv.appendChild(newP);
              window.location.href = `../${username}/homepage`;
            }
            else{
                const loginDiv = document.getElementById("login-form-div");
                const newP =  document.createElement("p");
                newP.innerText = "Unable to Authenticate. Try again!";
                loginDiv.appendChild(newP);
            }
          };
          loginChanges();
        }
        // Authenticates if the user is signing up.
        else{
          const signupPath = 'http://127.0.0.1:5000/api/signup';
          const username = document.getElementById("username").value;
          const password = document.getElementById("password").value;
          const email = document.getElementById("email").value;
          const signupResult = axios.post(signupPath,
                       {name: username, password: password, email: email}, 
                       {headers: {'Content-Type': 'application/json'}})
                       .then((response) => response.data)
                       .then((user) => {
                        return [user.username, user.status];
                       });
          const signupChanges = async () => {
            const [username, status] = await signupResult;
            if(status === "New User Created"){
              const passwordDiv = document.getElementById("password-div");
              const newP =  document.createElement("p");
              newP.innerText = "Registration Successfull. Redirecting...";
              passwordDiv.appendChild(newP);
              window.location.href = `../login`;
            }
            else if (status === "Username is already taken") {
              const oldP =  document.getElementById("p-dup-username");
              if(oldP){
                oldP.remove();
              }
              const usernameDiv = document.getElementById("username-div");
              const newP =  document.createElement("p");
              newP.setAttribute("id", "p-dup-username");
              newP.innerText = `Username: ${username} is already taken`;
              usernameDiv.appendChild(newP);
            }
            else{
                const loginDiv = document.getElementById("signup-form-div");
                const newP =  document.createElement("p");
                newP.innerText = `Trouble signing user up`;
                loginDiv.appendChild(newP);
            }
            console.log(status);
            console.log(username);
          };
          signupChanges();
        }
      }
    }
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