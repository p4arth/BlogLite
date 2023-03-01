<template>
    <div class="menu-item" @click="isOpen = !isOpen">
      <p>
        {{ title }}
      </p>
      <!-- <svg viewBox="0 0 1030 638" width="10">
        <path d="M1017 68L541 626q-11 12-26 12t-26-12L13 68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 43.5z" fill="#FFF">
        </path>
      </svg> -->
      <img src = "../assets/dropdown_png.png">
      <transition name="fade" appear>
        <div class="sub-menu" v-if="isOpen">
          <div v-for="(item, i) in items" :key="i" class="menu-item" id = "sub-menu-items">
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
        isOpen: false
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
    height: 10px;
  }
  nav .menu-item svg {
    width: 10px;
    margin-left: 10px;
    background: #837f7f;
  }
  nav .menu-item .sub-menu {
    position: absolute;
    background-color: #f5f0f0;
    top: calc(50% + 8px);
    left: 40%;
    transform: translateX(-70%);
    width: 200%;
    height: 50vh;
    border: 1px solid rgb(156, 153, 153);
    border-radius: 4px 4px 4px 4px;
  }
  #sub-menu-items{
    padding: 10px;
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
  