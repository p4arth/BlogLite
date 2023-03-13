<template>
    <nav>
      <div class = "menu-item-logo">
        <img src = "../assets/bl_logo.png">
        <form @submit.prevent="search" style="float:left;">
            <b-icon id="search-nav"
                    icon="search" 
                    scale="1.2"
                    style="margin-left:10px">
                </b-icon>
            <input id="search-query"
                   class = "search-bar" 
                   type="text" placeholder="Search.." autocomplete="false">
        </form>
      </div>
      <div class = "menu-container">
        <div  class="menu-item" style="padding-right:1%">
            <a href="./publish">
                <b-icon id="publish-nav" icon="pencil-square" scale="1.6">
                </b-icon>
            </a>
        </div>
        <div class="menu-item">
            <a href="#">
                <b-icon id="notif-nav" icon="bell" scale="1.6">
                </b-icon>
            </a>
        </div>
        <img id="home-nav-img" :src = "pfp_link">
        <DropDown  :items="dropdownItems" />
      </div>
    </nav>
</template>
  
<script>
import DropDown from "./DropDown.vue";
export default {
    name: 'HomeNav',
    components: {
        DropDown,
    },
    data() {
        return {
            dropdownItems: [
                {
                    title: "Profile",
                    link: `http://127.0.0.1:8080/${localStorage.currUser}/profile`
                },
                {
                    title: "My Blogs",
                    link: "./my-blogs"
                },
                {
                    title: "Stats",
                    link: "./profile"
                },
            ],
            pfp_link: "",
        }
    },
    mounted(){
      const path = `http://127.0.0.1:5000/api/get/profile_picture/${localStorage.currUser}`
      fetch(path, {
            methods: "GET",
            headers: {
                  'Content-Type': 'application/json',
                  'Authorization': localStorage.jwtToken,
                },
            }
        )
        .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
        })
        .then(
          data => {
            this.pfp_link = data.link;
          }
        )
    },
    methods: {
        search: function(){
            const searchTerm = document.getElementById("search-query").value;
            let currUrl =  `http://127.0.0.1:8080/search/`
            let queryString = "?q=" + encodeURIComponent(searchTerm);
            let fUrl = currUrl + queryString;
            window.location.href = fUrl;
            
        }
    }
}
</script>
  
<style scoped>
img {
    float:left;
    margin-top:8px;
    height: 30%;
    width: 25%;
}
#home-nav-img{
    width: 35px;
    height: 35px;
    border-radius: 30px;
    margin-top: 5px;
    margin-bottom: 15px;
}
.search-bar{
    width: 70%;
    border: none;
    margin-left:10px;
    height: 40px;
    outline: none;
    text-align: left;
}
.menu-item-logo {
    margin-right: 0px;
    height:50%;
}

.menu-container {
  width: 600px;
  display: flex;
  justify-content: flex-end;
  border-bottom: 0px;
}

nav {
    display: flex;
    align-items: left;
    justify-content: space-between;
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
    background-color: rgb(252, 255, 255);
    border-color: rgb(253, 255, 255);
}
nav .menu-item a {
    color: inherit;
    text-decoration: none;
}
#publish-nav, #notif-nav, #search-nav{
    color:rgb(97, 97, 97);
}
#publish-nav:hover, #notif-nav:hover{
    color:rgb(0, 0, 0);
}

#corner-item{
    margin-right: 20%;
    background-color: rgb(239, 242, 243);
    border-color: #f1f1f1;
    margin-right:0;
}
</style>