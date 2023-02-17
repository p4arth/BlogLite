<template>
<div>
    <MyBlogs :user="`${this.user}`" :isProfile="true" >
        <div class = "profile-section">
            <img v-if="user_details.pfp_link !== 'nan'" 
                 class = "profile-picture" 
                 :src = "`${user_details.pfp_link}`">
            <img v-else 
                 class = "profile-picture" 
                 src = "../assets/blankpropic.png">   
            <div class = "profile-username">
                <h4><b>Paarth Bhatnagar</b></h4>
            </div>
            <div class = "profile-caption">
                <small>
                    {{ user_details.biotext }}
                </small>
            </div>
            <div class = "profile-follow">
                <!-- Following Modal Button -->
                <b-button id = "follower-modal-button" 
                          v-b-modal.modal-followers>
                    <small style = "font-weight: bold;">{{ user_details.followers_count }} Followers</small>
                </b-button>

                <!-- Follower Modal Button -->
                <b-button id = "following-modal-button" 
                          v-b-modal.modal-following>
                    <small style = "font-weight: bold;">{{ user_details.following_count }} Following</small>
                </b-button>
            </div>
        </div>
    </MyBlogs>
    <!-- Modals -->
    <div>
        <!-- Following Modal -->
        <b-modal id="modal-followers" title="BootstrapVue">
            <div v-for="follower in user_details.followers" :key="follower.username">
                <p>{{ follower.username }}</p>
            </div>
        </b-modal>
        <!-- Followers Modal -->
        <b-modal id="modal-following" title="BootstrapVue">
            <div v-for="following in user_details.following" :key="following.follows">
                <p>{{ following.follows }}</p>
            </div>
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
            user: "",
            user_details: "",
            is_curr: false,
        }
    },
    created(){
        this.user = this.$route.params.username;
    },
    mounted(){
        if(localStorage.currUser === this.user){
            this.is_curr = true;
            const profPath = `http://127.0.0.1:5000/api/${this.user}/my-profile`;
            fetch(profPath, {
                headers: {"Authorization": localStorage.jwtToken}
            })
            .then(reponse => reponse.json())
            .then(data => this.user_details = data);
        }
        else{
            const profPath = `http://127.0.0.1:5000/api/${this.user}/my-profile`;
            fetch(profPath, {
                headers: {"Authorization": localStorage.jwtToken}
            })
            .then(reponse => reponse.json())
            .then(data => this.user_details = data);
        }
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