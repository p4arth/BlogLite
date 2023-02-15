<template>
<div>
    <MyBlogs :user="`${this.user}`" :isProfile="true" >
        <div class = "profile-section">
            <img class = "profile-picture" 
                 src = "https://avatars.githubusercontent.com/u/75850838?s=400&u=7741546969ab6771831f3484d81e1272399d642c&v=4">        </div>
            <div class = "profile-username">
                <h4><b>Paarth Bhatnagar</b></h4>
            </div>
            <div class = "profile-caption">
                <small>
                    Hey! I am Paarth, currently majoring in data science and biology.
                    I like to write about topics that intrigue me.
                </small>
            </div>
            <div class = "profile-follow">
                <!-- Following Modal Button -->
                <b-button id = "follower-modal-button" 
                          v-b-modal.modal-followers>
                    <small style = "font-weight: bold;">30 Followers</small>
                </b-button>

                <!-- Follower Modal Button -->
                <b-button id = "following-modal-button" 
                          v-b-modal.modal-following>
                    <small style = "font-weight: bold;">30 Following</small>
                </b-button>
            </div>
    </MyBlogs>
    <!-- Modals -->
    <div>
        <!-- Following Modal -->
        <b-modal id="modal-followers" title="BootstrapVue">
            <p class="my-4">Hello from followers</p>
        </b-modal>
        <!-- Followers Modal -->
        <b-modal id="modal-following" title="BootstrapVue">
            <p class="my-4">Hello from following</p>
        </b-modal>
    </div>
</div>
</template>

<script>
import MyBlogs from "./user_blogs/MyBlogs.vue"
export default{
    name: "UserProfile",
    components: {
        MyBlogs
    },
    data() {
        return {
            user: ""
        }
    },
    created(){
        this.user = this.$route.params.username;
    }
}

</script>

<style scoped>
.profile-section{
    margin-left: 4%;
}

.profile-picture{
    float: left;
    width: 30%;
    height: 30%;
    margin-top: 20%;
    margin-left: 5%;
    border-radius: 50%;
}
.profile-username{
    float: left;
    margin-top: 18%;
    margin-left: 5%;
}
.profile-caption{
    float: left;
    margin-left: 5%;
    width: 250px;
}
.profile-follow{
    float: left;
    /* margin-top: 1%; */
    margin-left: 5%;
    width: 250px;
}
#follower-modal-button{
    width: 83px;
    height: 100%;
    border: 0px;
    padding: 0px;
    background-color: white;
    color: rgb(122, 120, 120);
    outline: none;
    box-shadow: none;
    
}

#following-modal-button{
    width: 119px;
    height: 100%;
    border: 0px;
    padding-left: 2%;
    background-color: white;
    color: rgb(122, 120, 120);
    outline: none;
    box-shadow: none;
}

#follower-modal-button:hover, #following-modal-button:hover{
    color: rgb(20, 20, 20);
}


























.dot {
    width: 3px;
    height: 3px;
    border-radius: 5px;
    margin-top: 0px;
    margin-left: 2px;
    margin-right: 2px;
    background-color: rgb(150, 147, 147);
}
</style>