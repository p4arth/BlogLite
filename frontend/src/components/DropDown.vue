<template>
    <div id="dropDown-menu-item" class="menu-item" @click="isOpen = !isOpen">
      <img src = "../assets/dropdown_png.png">
      <transition name="fade" appear>
        <div class="sub-menu" v-if="isOpen">
          <div id = "sub-menu-items" 
               v-for="(item, i) in items" :key="i" 
               class="menu-item" >
            <a :href="item.link">{{ item.title }}</a>
          </div>
          <div class="menu-item" id="logout">
            <a @click="logout" href="/">Log Out</a>
          </div>
        </div>
      </transition>
    </div>
</template>
  
<script >
  export default {
    name: 'DropDown',
    props: ['title', 'items'],
    data () {
      return {
        isOpen: false,
      }
    },
    methods: {
      logout: function(){
        localStorage.removeItem('currUser');
        localStorage.removeItem('jwtToken');
      }
    }
  }
</script>
  
<style scoped>
  img {
    margin-top: 8px;
    margin-left: 5px;
    width: 10px;
    height: 10px;
  }
  #dropDown-menu-item{
    padding-left: 0px;
  }
  nav .menu-item svg {
    width: 10px;
    margin-left: 10px;
    background: #837f7f;
  }
  nav .menu-item .sub-menu {
    position: absolute;
    background-color: #f5f0f0;
    top: calc(50% + 18px);
    left: 40%;
    transform: translateX(-90%);
    width: 500%;
    height: 50vh;
    border: 1px solid rgb(156, 153, 153);
    border-radius: 4px 4px 4px 4px;
  }
  #sub-menu-items, #logout{
    padding: 10px;
    border-radius: 0px;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: all .1s ease-out;
  }
  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }
</style>
  