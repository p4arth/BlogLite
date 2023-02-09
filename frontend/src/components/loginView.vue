<template>
    <div class="container">
        <div class="row">
            <div class="col-6" style = "padding-top: 15%;padding-left: 10%;">
            <img src="../assets/login_image.png" width="500" height="500">
            </div>
            <div class="col-6" style = "padding-top: 10%;padding-right: 15%;">
            <div class="card mx-auto" style="width: 20rem;height: 40rem;">
                <div class="card-body" style = "padding-top: 30%;text-align: center;">
                    <h3 class="card-title text-center mb-4">Enter BlogLite</h3>
                    <div id = "login-form-div">
                        <form id = "login-form" @submit.prevent = "submit" method = "POST">
                            <input type = "text" class="form-control form-control-lg" id = "username" name = "login-username" autocomplete="off" placeholder = "username" required /><br>
                            <input type = "password" class="form-control form-control-lg" id = "password" name = "login-password" autocomplete="off" placeholder = "password" required>
                            <!-- {% if message | default(false)  %}
                                <p id = "message">Incorect username or password!</p>
                            {% endif %} -->
                            <button type="submit" id = "login-button" class="btn btn-primary">Log In</button>
                        </form>
                    </div>
                    <div>
                        <p>
                            New User?
                            <a href = "/signup">
                                Sign Up!
                            </a>
                        </p>
                    </div>
            </div>
        </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import setAuthHeader from '../utils/setAuthHeader.js';
export default{
    data(){
        return {
            dataentry: {
                name:"",
                password:"",
            },
        };
    },
    methods:{
        submit: function(){
            const path = 'http://127.0.0.1:5000/api/login';
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            const result = axios.post(path,
                       {name: username, password: password}, 
                       {headers: {'Content-Type': 'application/json'}})
                       .then((response) => response.data)
                       .then((user) => {
                        return [user.username, user.status, user.auth_token];
                       });
            
            const changes = async () => {
                const [username, status, token] = await result;
                if(status === "Authenticated"){
                    localStorage.setItem("jwtToken", token);
                    setAuthHeader(token);
                    window.location.href = `../${username}/homepage`;
                }
                else{
                    const loginDiv = document.getElementById("login-form-div");
                    const newP =  document.createElement("p");
                    newP.innerText = "Unable to Authenticate. Try again!";
                    loginDiv.appendChild(newP);
                }
            };
            changes();
        }
    }
}
</script>

<style>
    body {
        width: 100%;
    }
    #login-button{
        margin:8px;
    }
    #message{
        background-color: red;
        margin-left: 9%;
        margin-right: 9%;
        margin-top: 2%;
        margin-bottom: -1%;
        color: white;
        border-radius: 6px;
    }
</style>