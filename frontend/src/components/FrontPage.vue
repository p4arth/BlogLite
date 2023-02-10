<template>
    <div>
      <header>
        
        <!-- <img src = "../assets/bl_logo.png"> -->
        <NavBar />
      </header>
    </div>
</template>
  
<script>
  import NavBar from './NavBar.vue';
  export default {
    name: 'FrontPage',
    components: {
      NavBar
    }
  }
</script>
  
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  body {
    /* margin-left:10%; */
    /* margin-right:10%; */
    font-family: 'montserrat', sans-serif;
  }
  header {
    width: 100vw;
    background-color: rgb(179, 238, 248);
    padding: 10px;
    border: 20px;
    border-bottom: 1px solid #494949;
  }
</style>