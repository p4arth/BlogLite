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
                    <small id="count-followers" 
                           style = "font-weight: bold;"
                           >
                           {{ followers_count }} Followers
                    </small>
                </b-button>

                <!-- Follower Modal Button -->
                <b-button id = "following-modal-button" 
                          v-b-modal.modal-following>
                    <small style = "font-weight: bold;">
                        {{ user_details.following_count }} Following
                    </small>
                </b-button>
            </div>
            <div v-if="!is_curr" id="follow-button-div" style="float:left;">
                <button v-if="!isFollowing" id="follow-button-prof"
                        class="follow-button"
                        @click="followClick">Follow</button>
                <button v-else id="follow-button-prof"
                        class="follow-button"
                        @click="followClick">Following</button>
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
            followers_count: "",
            isFollowing: false,
            follow_button_value: "Follow",
        }
    },
    created(){
        this.user = this.$route.params.username;
    },
    mounted(){
        this.getProfileData();
        this.getUserFollowers();
    },
    methods: {
        getProfileData: function(){
            if(localStorage.currUser === this.user){
                this.is_curr = true;
                const profPath = `http://127.0.0.1:5000/api/${this.user}/my-profile`;
                fetch(profPath, {
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": localStorage.jwtToken
                    }
                })
                .then(reponse => reponse.json())
                .then(data => this.user_details = data)
                .then(data => this.followers_count = data.followers_count);
            }
            else{
                const profPath = `http://127.0.0.1:5000/api/${this.user}/my-profile`;
                fetch(profPath, {
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": localStorage.jwtToken
                    }
                })
                .then(reponse => reponse.json())
                .then(data => this.user_details = data)
                .then(data => this.followers_count = data.followers_count);
                // If this is not the users profile I need to get the data about
                // The people this user user is following and need to update accordigly.
            }
        },
        getUserFollowers: function(){
            const path = `http://127.0.0.1:5000/api/get/${localStorage.currUser}/follows/${this.user}`;
            fetch(path, 
            {   
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(reponse => reponse.json())
            .then(data => this.user_details = data)
            .then((data) => {
                this.isFollowing = data.following;
            });
        },
        followClick: async function(){
            const followButton = document.getElementById("follow-button-prof");
            if(followButton.innerHTML === "Follow"){
                const path = `http://127.0.0.1:5000/api/${localStorage.currUser}/follow`
                await fetch(path, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                "Authorization": localStorage.jwtToken,
                            },
                            body: JSON.stringify({"has_to_follow": this.user})
                            })
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error('Network response was not ok');
                                }
                                return response.json();
                            })
                            .then(data => {
                                console.log(data);
                            })
                this.isFollowing = true;
                this.followers_count = this.followers_count + 1;
            }
            else{
                const path = `http://127.0.0.1:5000/api/${localStorage.currUser}/follow`
                await fetch(path, {
                            method: 'DELETE',
                            headers: {
                                'Content-Type': 'application/json',
                                "Authorization": localStorage.jwtToken,
                            },
                            body: JSON.stringify({"has_to_unfollow": this.user})
                            })
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error('Network response was not ok');
                                }
                                return response.json();
                            })
                            .then(data => {
                                console.log(data);
                            })
                this.isFollowing = false;
                this.followers_count = this.followers_count - 1;
            }
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

.follow-button {
  background-color: green;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 20px;
  cursor: pointer;
}

#follow-button-div{
    margin-left: 5%;
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