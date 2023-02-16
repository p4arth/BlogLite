<template>
    <nav>
      <div class = "menu-item-logo">
        <img src = "../assets/bl_logo.png">
      </div>
      <div class = "menu-container">
        <div class="menu-item"><a href="#">About</a></div>
        <div class="menu-item"><a href="#">Github</a></div>
        <div class="menu-item">
            <p @click="modalType = 'login'" id="login-modal-click" v-b-modal.modal-login>
                Log In
            </p>
        </div>
        <div id = "corner-item" class="menu-item">
            <p @click="modalType = 'signup'" id = "signup-modal-click"  v-b-modal.modal-login>
                Sign Up
            </p>
            <!-- <b-modal id="modal-login" title="BootstrapVue">
                <p>
                    Hello from signup
                </p>
            </b-modal> -->
        </div>
        <!-- MAIN AUTHENTICATION MODAL -->
        <b-modal @shown="changeModal()" 
                 id="modal-login" 
                 centered>
                <div class="text-center mb-4">
                    <h5 id = "auth-modal-title" class="modal-title">Welcome to BlogLite</h5>
                </div>
                <form id = "auth-form" @submit.prevent = "submit" method = "POST">
                    <div id = "email-div">
                      <input type="email" id="email" name="email" placeholder = "Enter Email" autocomplete = "off" required />
                    </div>
                    <div id = "username-div">
                      <input type="text" id="username" name="username" placeholder = "Enter username"  autocomplete = "off" required />
                    </div>
                    <div id = "password-div">
                      <input id="password" name="password" placeholder = "Enter password" autocomplete = "off" required />
                    </div>
                    <input type="submit" :value="modal_ok_button_value" />
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
    data() {
        return {
            modal_ok_button_value: "Signup",
            modalType: "",
        }
    },
    methods:{
        changeModal: function(){
            if(this.modalType === 'login'){
                const email = document.getElementById("email-div");
                email.remove();
                const modalTitle = document.getElementById("auth-modal-title");
                modalTitle.innerHTML = "Welcome Back.";
                this.modal_ok_button_value = "Log In";
            }
        },
        submit: function(){
            // Authenticates if the user is logging in.
            if(this.modalType === "login"){
                const loginPath = 'http://127.0.0.1:5000/api/login';
                const username = document.getElementById("username").value;
                const password = document.getElementById("password").value;
                console.log(username);
                console.log(password);
                const result = axios.post(loginPath,
                                        {name: username, password: password}, 
                                        {headers: {'Content-Type': 'application/json'}})
                                        .then((response) => response.data)
                                        .then((user) => {
                                            return [user.username, user.status, user.auth_token];
                                        });
                
                const loginChanges = async () => {
                    const [username, status, token] = await result;
                    console.log(token);
                    if(status === "Authenticated"){
                        console.log(1);
                        localStorage.setItem("jwtToken", token);
                        localStorage.setItem("currUser", username);
                        setAuthHeader(token);
                        console.log("hereeeeeeeee");
                        // const passwordDiv = document.getElementById("password-div");
                        // const newP =  document.createElement("p");
                        // newP.innerText = "Authenticated!";
                        // passwordDiv.appendChild(newP);
                        window.location.href = `../${username}/homepage`;
                    }
                    else{
                        // const loginDiv = document.getElementById("login-form-div");
                        // const newP =  document.createElement("p");
                        // newP.innerText = "Unable to Authenticate. Try again!";
                        // loginDiv.appendChild(newP);
                    }
                };
                loginChanges();
                // console.log(window.location.href);
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
    },
}
</script>
  
<style >
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