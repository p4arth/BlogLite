<template>
    <div>
      <header>
        <NavBar />
      </header>
      <div class = "jumbotron">
        <div class = "jumbotron-content">
            <h1 class="display-4">Start Unleashing your creativity</h1>
            <p class="lead">This is a simple example of a Bootstrap Jumbotron.</p>
            <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
            <a class="btn btn-primary btn-lg" href="#" role="button">Start Reading</a>
        </div>
            
        </div>
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
    font-family: 'montserrat', sans-serif;
  }
  header {
    width: 100vw;
    background-color: rgb(179, 238, 248);
    padding: 10px;
    border: 20px;
    border-bottom: 1px solid #494949;
  }
  .jumbotron {
    border-bottom: 1px solid #494949;
    background-color: rgb(179, 238, 248);
  }
  .jumbotron-content{
    margin-right: 0%;
    margin-left: 15.5%;
  }
</style>