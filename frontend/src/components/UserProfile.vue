<template>
<div>
    <MyBlogs :user="`${this.user}`" :isProfile="true" >
        <div class = "profile-section">
            <img v-if="user_details.pfp_link"
                 class = "profile-picture" 
                 :src = "`${user_details.pfp_link}`">
            <img v-else 
                 class = "profile-picture" 
                 src = "../assets/blankpropic.png">   
            <div class = "profile-username">
                <h4><b>{{ user_details.full_name }}</b></h4>
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
            <div v-else id="edit-profile" v-b-modal.edit-details>
                Edit Profile
            </div>
        </div>
    </MyBlogs>
    <!-- Modals -->
    <div>
        <!-- Following Modal -->
        <b-modal id="modal-followers" title="Followers">
            <div v-for="follower in user_details.followers" :key="follower.username">
                <p>{{ follower.username }}</p>
            </div>
        </b-modal>
        <!-- Followers Modal -->
        <b-modal id="modal-following" title="Following">
            <div v-for="following in user_details.following" :key="following.follows">
                <p>{{ following.follows }}</p>
            </div>
        </b-modal>
        <!-- EDIT DETAILS MODALS -->
        <b-modal id="edit-details" title="Edit Profile">
            <form id = "auth-form" @submit.prevent = "submitProfileChanges">
                    <div id = "new-bio-text-div">
                      <input type="text" 
                             placeholder = "Enter new bio text" 
                             v-model="new_bio_text"
                             autocomplete = "off"/>
                    </div>
                    <div id = "new-pfp-link-div">
                      <input placeholder = "Enter new profile picture link"
                             v-model="new_pfp_link"
                             autocomplete = "off"/>
                    </div>
                    <input id="save-button" type="submit" value="Save" />
                </form>
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
            new_bio_text: "",
            new_pfp_link: "",
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
        getProfileData: async function(){
            if(localStorage.currUser === this.user){
                // console.log("PROFILE CURR");
                this.is_curr = true;
                const profPath = `http://127.0.0.1:5000/api/${localStorage.currUser}/my-profile`;
                await fetch(profPath, {
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": localStorage.jwtToken
                    }
                })
                .then(reponse => reponse.json())
                .then(data => this.user_details = data)
                .then(data => this.followers_count = data.followers_count)
            }
            else{
                // console.log("PROFILE NOT CURR");
                const profPath = `http://127.0.0.1:5000/api/${this.user}/my-profile`;
                await fetch(profPath, {
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": localStorage.jwtToken
                    }
                })
                .then(reponse => reponse.json())
                .then(data => this.user_details = data)
                .then(data => this.followers_count = data.followers_count)
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
        },
        submitProfileChanges: function(){
            this.profileChanges(this.new_bio_text, this.new_pfp_link);
        },
        profileChanges: async function(new_bio, new_pfp){
            const path = `http://127.0.0.1:5000/api/profile_change/${localStorage.currUser}`;
            await fetch(path, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            "Authorization": localStorage.jwtToken,
                        },
                        body: JSON.stringify({
                            "new_bio": new_bio,
                            "new_pfp": new_pfp
                            })
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
            location.reload();
            
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

#edit-profile{
    float:left;
    margin-left: 6%;
    padding: 3px;
    font-size: small;
    color: rgb(77, 76, 76);
    font-weight: 500;
    border: 1px solid rgb(134, 134, 134);
    border-radius: 7%;
}
#edit-profile:hover{
    color: black;
    border: 1px solid black;
    cursor: pointer;
}

#new-bio-text-div input, #new-pfp-link-div input{
    margin-bottom: 10px;
    width: 80%;
    padding: 10px;
    font-size: 17px;
    border: 2px solid rgb(245, 243, 239);
    border-radius: 20px;
    outline: none;
    transition: background-color 0.2s ease-in-out;
}

#new-bio-text-div input:hover, #new-pfp-link-div input:hover{
    background-color: rgb(173, 171, 167);
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