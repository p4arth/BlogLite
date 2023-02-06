<template>
    <div class="col-md-1 col-lg-1 border " style = "padding-top:-10%;padding-bottom: 100%;">
        <div class="d-flex flex-column flex-shrink-0 bg-light" style="width:4.5rem;margin:0px;position: fixed;padding-top: 13%;">
            <a :href="`.${username}/homepage`" class="d-block p-3 link-dark text-decoration-none border-bottom" title="Home" data-bs-toggle="tooltip" data-bs-placement="right">
                <img src="../assets/home.png" alt = "Home" style = "padding-left:5px;" width="36" height="30">
            </a>
            <a :href="`.${username}/publish_new_article`" style = "padding-left:22px;" class="nav-link py-3 border-bottom" title="Publish" data-bs-toggle="tooltip" data-bs-placement="right">
                <img src="../assets/publish.png"  width="33" height="32">
            </a>
            <a :href="`.${username}/my-blogs`" class="nav-link py-3 border-bottom" title="My Blogs" data-bs-toggle="tooltip" data-bs-placement="right">
                <img src="../assets/my_blogs.png" style = "padding-left:5px;" width="40" height="35" >
            </a>
            <div class="dropdown border-top">
                <a href="#" class="d-flex align-items-center justify-content-center p-3 link-dark text-decoration-none dropdown-toggle" id="dropdownUser3" data-bs-toggle="dropdown" aria-expanded="false">
                    <img src="https://images.pexels.com/photos/6985001/pexels-photo-6985001.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="mdo" width="24" height="24" class="rounded-circle">
                </a>
                <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser3">
                    <li>
                        <a class="dropdown-item" :href="`/${username}/publish_new_article`">
                            New Blog
                        </a>
                    </li>
                    <li>
                        <a class="dropdown-item" :href="`/${username}/my-blogs`">
                            My Blogs
                        </a>
                    </li>
                    <li>
                        <a class="dropdown-item" :href="`/${username}/my-profile`">
                            Profile</a>
                        </li>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                    <li>
                        <a class="dropdown-item" href="/login">
                            Log Out
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import {useRoute} from 'vue-router';
export default {
    name: "NavBar",
    data() {
        return {
            username: ""
        } 
    },
    mounted(){
        const route = useRoute();
        this.username = route.params.username;
    }
}
// export default{
//     data(){
//         return {
//             dataentry: {
//                 name:"",
//                 password:"",
//             },
//         };
//     },
//     methods:{
//         submit: function(){
//             const path = 'http://127.0.0.1:5000/api/signup';
//             const username = document.getElementById("username").value;
//             const password = document.getElementById("password").value;
//             const result = axios.post(path,
//                        {name: username, password: password}, 
//                        {headers: {'Content-Type': 'application/json'}})
//                        .then((response) => response.data)
//                        .then((user) => {
//                         return [user.username, user.status];
//                        });
//             const changes = async () => {
//                 const [username, status] = await result;
//                 if(status === "New User Created"){
//                     window.location.href = `../login`;
//                     const loginDiv = document.getElementById("login-form-div");
//                     const newP =  document.createElement("p");
//                     newP.innerText = "Login using your new credentials";
//                     loginDiv.appendChild(newP);
//                 }
//                 else if (status === "Username is already taken") {
//                     const loginDiv = document.getElementById("signup-form-div");
//                     const newP =  document.createElement("p");
//                     newP.innerText = `Username: ${username} is already taken`;
//                     loginDiv.appendChild(newP);
//                 }
//                 else{
//                     const loginDiv = document.getElementById("signup-form-div");
//                     const newP =  document.createElement("p");
//                     newP.innerText = `Trouble signing user up`;
//                     loginDiv.appendChild(newP);
//                 }
//                 console.log(status);
//                 console.log(username);
//             };
//             changes();
//         }
//     }
// }
</script>

<!-- <style>
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
     -->