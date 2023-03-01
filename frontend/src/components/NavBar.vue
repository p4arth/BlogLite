<template>
    <nav>
      <div class = "menu-item-logo">
        <img src = "../assets/bl_logo.png">
      </div>
      <div class = "menu-container">
        <div class="menu-item"><a href="#">About</a></div>
        <div class="menu-item"><a href="#">Github</a></div>
        <div class="menu-item">
            <p id="login-modal-click" v-b-modal.modal-login>
                Log In
            </p>
        </div>
        <div id = "corner-item" class="menu-item">
            <p id = "signup-modal-click"  v-b-modal.modal-signup>
                Sign Up
            </p>
        </div>
        <!-- MAIN AUTHENTICATION MODALS -->
        <b-modal id="modal-login" centered>
            <div class="text-center mb-4">
                <h5 id="auth-modal-title" class="modal-title">Welcome Back!</h5>
            </div>
            <form id="auth-form" @submit.prevent="submitLogin" >
                <div id="username-div">
                    <input type="text" 
                           id="username" 
                           name="username" 
                           placeholder="Enter username" 
                           autocomplete="off" required v-model="username" />
                </div>
                <div id="password-div">
                    <input id="password" 
                           name="password" 
                           placeholder="Enter password" 
                           autocomplete="off" required v-model="password" />
                </div>
                <input type="submit" value="Log In" />
            </form>
        </b-modal>
        <!-- SIGNUP MODAL -->
        <b-modal id="modal-signup" centered>
                <div class="text-center mb-4">
                    <h5 id = "auth-modal-title" class="modal-title">Get Started with BlogLite</h5>
                </div>
                <form id = "auth-form" @submit.prevent = "submitSignup">
                    <div id = "email-div">
                      <input type="email" 
                             id="email" 
                             name="email" 
                             placeholder = "Enter Email" 
                             autocomplete = "off" required />
                    </div>
                    <div id = "username-div">
                      <input type="text" 
                             id="username" 
                             name="username" 
                             placeholder = "Enter username"  
                             autocomplete = "off" required />
                    </div>
                    <div id = "password-div">
                      <input id="password" 
                             name="password" 
                             placeholder = "Enter password" 
                             autocomplete = "off" required />
                    </div>
                    <input type="submit" value="Sign Up" />
                </form>
        </b-modal>
      </div>
      <div>
        
      </div>
      
    </nav>
</template>
  
<script>
import axios from 'axios';
import setAuthHeader from '../utils/setAuthHeader.js';
export default {
    name: 'NavBar',
    inheritAttrs: false,
    emits: ['submit'],
    data() {
        return {
            username: "",
            password: "",
            email: "",
        }
    },
    methods: {
        submitLogin() {
            this.login(this.username, this.password);
        },
        submitSignup() {
            this.signup(this.email, this.username, this.password);
        },
        login: function(username, password){
            const loginPath = 'http://127.0.0.1:5000/api/login';
            const result = axios.post(
                loginPath,
                {name: username, password: password}, 
                {headers:
                     {'Content-Type':'application/json'}
                })
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
                        const passwordDiv = document.getElementById("password-div");
                        const newP =  document.createElement("p");
                        newP.innerText = "Authenticated!";
                        passwordDiv.appendChild(newP);
                        window.location.href = `../${username}/homepage`;
                    }
                    else{
                        const loginDiv = document.getElementById("password-div");
                        const newP =  document.createElement("p");
                        newP.innerText = "Unable to Authenticate. Try again!";
                        loginDiv.appendChild(newP);
                    }
                };
                loginChanges();    
        },
        signup: function(email, username, password){
            const signupPath = 'http://127.0.0.1:5000/api/signup';
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
                        newP.innerText = "Registration Successfull. Please Login with your new credentials";
                        passwordDiv.appendChild(newP);
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        window.location.href = `/`;
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
                };
                signupChanges();

        }

    },
}
</script>
  
<style scoped>
img {
    height: 30%;
    width: 30%
}
.menu-item-logo {
    margin-right: 0px;
    color: black;
    padding: 0px 0px;
    margin-right: 0px;
    position: left;
    text-align: left;
    border: 0px solid white;
    border-radius: 0px;
    display: flex;
    transition: 0.4s;
}

.menu-container {
  width: 600px;
  display: flex;
  justify-content: flex-end;
  border-bottom: 0px;
}

nav {
    display: flex;
    align-items: center;
    justify-content: center;
}
nav .menu-item {
    color: black;
    padding: 10px 30px;
    margin-right: 10px;
    position: relative;
    text-align: center;
    border-radius: 20px;
    display: flex;
    transition: 0.4s;
}
nav .menu-item.active,
nav .menu-item:hover {
    background-color: rgb(121, 226, 245);
    border-color: rgb(121, 226, 245);
}
nav .menu-item a {
    color: inherit;
    text-decoration: none;
}
#corner-item{
    margin-right: 20%;
    background-color: rgb(121, 226, 245);
    border-color: #f1f1f1;
}

#login-modal-click{
    font-weight: normal !important;
    margin: 0px;
}
#signup-modal-click{
    margin: 0px;
}
#modal-login{
    border: none !important;
    justify-content: center;
}
.modal-header{
    border: none;
}
.modal-footer{
  display: none !important;
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