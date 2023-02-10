<!-- <template>
    <div class="col-md-1 col-lg-1 border " style = "padding-top:-10%;padding-bottom: 100%;">
        <div class="d-flex flex-column flex-shrink-0 bg-light" style="width:4.5rem;margin:0px;position: fixed;padding-top: 13%;">
            <a :href="`../${username}/homepage`" class="d-block p-3 link-dark text-decoration-none border-bottom" title="Home" data-bs-toggle="tooltip" data-bs-placement="right">
                <img src="../assets/home.png" alt = "Home" style = "padding-left:5px;" width="36" height="30">
            </a>
            <a :href="`../${username}/publish_new_article`" style = "padding-left:22px;" class="nav-link py-3 border-bottom" title="Publish" data-bs-toggle="tooltip" data-bs-placement="right">
                <img src="../assets/publish.png"  width="33" height="32">
            </a>
            <a :href="`../${username}/my-blogs`" class="nav-link py-3 border-bottom" title="My Blogs" data-bs-toggle="tooltip" data-bs-placement="right">
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
</template> -->

<template>
    
    <nav>
      <div class = "menu-item-logo">
        <img src = "../assets/bl_logo.png">
      </div>
      <div class = "menu-container">
        <div class="menu-item"><a href="#">About</a></div>
        <div class="menu-item"><a href="#">Github</a></div>
        <!-- <DropDown title="Services" :items="services" /> -->
        <div class="menu-item"><a href="#">Log In</a></div>
        <div id = "corner-item" class="menu-item"><a href="#">Sign Up</a></div>
      </div>
    </nav>
</template>
  
<script>
// import DropDown from './DropDown';
export default {
    name: 'NavBar',
    // components: {
    //     DropDown
    // },
    data () {
        return {
        services: [
            {
                title: 'Web',
                link: '#'
            },
            {
                title: 'Design',
                link:'#'
            },
            {
                title: 'Videos',
                link: '#'
            }
        ]
        }
    }
}
</script>
  
<style>
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
  width: 700px;
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
    /* border: 1.5px solid rgb(121, 226, 245); */
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
</style>