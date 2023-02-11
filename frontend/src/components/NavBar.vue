<template>
    <nav>
      <div class = "menu-item-logo">
        <img src = "../assets/bl_logo.png">
      </div>
      <div class = "menu-container">
        <div class="menu-item"><a href="#">About</a></div>
        <div class="menu-item"><a href="#">Github</a></div>
        <div class="menu-item"><a href="./login">Log In</a></div>
        <div id = "corner-item" class="menu-item"><a href="./signup">Sign Up</a></div>
      </div>
    </nav>
</template>
  
<script>
export default {
    name: 'NavBar',
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
</style>