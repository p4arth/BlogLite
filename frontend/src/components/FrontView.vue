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
                    <div >
                        <form id = "login-form" @submit.prevent = "submit" method = "POST">
                            <input type = "text" class="form-control form-control-lg" id = "username" name = "login-username" autocomplete="off" placeholder = "username" required /><br>
                            <input type = "password" class="form-control form-control-lg" id = "password" name = "login-password" autocomplete="off" placeholder = "password" required>
                            <!-- {% if message | default(false)  %}
                                <p id = "message">Incorect username or password!</p>
                            {% endif %} -->
                            <button type="submit" id = "login-button" class="btn btn-primary">Log In</button>
                        </form>
                    </div>
                    <!-- <div>
                        <p>
                            New User?
                            <a href = "/signup">
                                Sign Up!
                            </a>
                        </p>
                    </div> -->
            </div>
        </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
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
            const returnObj = axios.post(path, {name: username, password: password}, 
                                        {headers: {'Content-Type': 'application/json'}}).data
            if (returnObj.status === "Authenticated"){
                window.location.href = '../${returnObj.username}/homepage';
            }
            window.console.log(returnObj);
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