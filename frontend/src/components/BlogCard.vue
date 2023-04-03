<template>
<div class = "card" :id="post.id">
    <div class="container" style="padding:0">
        <div class = "author-information">
            <div class = "author-profile-picture">
                <img id="profile-pic" v-if="pfp_link" :src="pfp_link">
                <img id="profile-pic" v-else src="../assets/blankpropic.png">
            </div>
            <div class="dot"></div>
            <div v-if="!publisher" class = "author-name">
                <a :href="`http://127.0.0.1:8080/${post.username}/profile`"
                    style="color:inherit;">{{ post.username }}</a>
            </div>
            <div v-else class = "author-name">You</div>
            <div class="dot"></div>
            <div class = "published-date" >
                {{ post.timestamp }}
            </div>
            <div v-if="is_logged_in">
                <b-dropdown text=":"  variant = "none" size = "sm">
                    <b-dropdown-item v-if="is_logged_in" 
                                     :href="`./edit/post/${post.id}`">
                                     Edit
                    </b-dropdown-item>
                    <b-dropdown-item v-if="is_logged_in"
                                     @click="delete_article">
                                     Delete
                    </b-dropdown-item>
                    <b-dropdown-item v-if="is_logged_in"
                                     @click="exportBlog"
                                     id="export-blog-button">
                                     Export
                    </b-dropdown-item>
                </b-dropdown>
            </div>
        </div>
        <div class = "blog-body">
                <div class = "main-title">
                    <h4><b>
                        <a style="color:inherit;
                                  text-decoration: none;"
                           :href="`../${this.post.username}/blog/${this.post.id}`">
                            {{ post.title }}
                        </a>
                    </b></h4>
                </div>
            <div class = "preview-content">
                <p>{{ post.caption.slice(0, 200) }}...</p>
        </div>
        </div>
        <div class = "blog-image" :style="`background-image: url(${post.image_url})`"></div>
    </div>
</div>
</template>

<script>
export default {
    name: "BlogCard",
    props: ["post", "publisher", "is_logged_in"],
    data() {
        return {
            "pfp_link": "",
        }
    },
    mounted(){
        this.get_user_picture();
    },
    methods: {
        get_user_picture: async function(){
            const path = `http://127.0.0.1:5000//api/get/profile_picture/${this.post.username}`;
            await fetch(path, {
                methods: "GET",
            })
            .then(response => response.json())
            .then(data => this.pfp_link = data.link);

        },
        delete_article: function(){
            const path = `http://127.0.0.1:5000/api/${this.$route.params.username}/delete_post`;
            const post_id = this.post.id;
            fetch(path, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    "Authorization": localStorage.jwtToken,
                },
                body: JSON.stringify({"post_id": post_id})
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
            })
        },
        exportBlog: async function(){
            let path = `http://127.0.0.1:5000/api/get/blog/${this.$route.params.username}`
            let queryString = "?post_id=" + encodeURIComponent(this.post.id);
            let fUrl = path + queryString;
            await fetch(fUrl, {
                methods: "GET",
                headers: {
                    'Authorization': localStorage.jwtToken,
                },
            })
            .then(response => response.blob())
            .then(blob => this.convertBlobCsv(blob));
        },
        convertBlobCsv: function(blob){
            const reader = new FileReader();
            reader.onload = (event) => {
                const csvString = event.target.result;
                const csvBlob = new Blob([csvString], { type: 'text/csv' });
                const url = window.URL.createObjectURL(csvBlob);
                const link = document.createElement('a');
                const fileName = `blog_${this.post.id}.csv`
                link.href = url;
                link.setAttribute('download', fileName);
                document.body.appendChild(link);
                link.click();
            };
            reader.readAsText(blob);
        },
    }
}
</script>

<style scoped>
.card{
    font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
    border-radius: 0%;
    padding-bottom: 2%;
    border: none;
    border-bottom:  2px solid #e0dcdc;
}
.author-information{
    display: flex;
    margin-top: 2%;
    align-items: center;
    /* justify-content: center; */
}
.blog-manager{
    float: right;
}
.published-date{
    margin-top: 3px;
}
.blog-body{
    float:left;
}
#profile-pic{
    width:30px;
    height: 30px;
    border-radius: 50%;
}
.main-title{
    padding-top: 10px;
    width: 500px;
}

.preview-content{
    width: 500px;
}

.blog-image{
    float: right;
    width: 112px;
    height: 112px;
    margin-top: 1%;
    overflow-x: hidden;
    overflow-y: hidden;
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 200%;
}

.dot {
    width: 3px;
    height: 3px;
    border-radius: 5px;
    /* margin-top: 12px; */
    margin-left: 5px;
    margin-right: 5px;
    background-color: rgb(150, 147, 147);
}

.dot-edit {
    width: 4px;
    height: 4px;
    border-radius: 4px;
    margin-top: 2px;
    margin-left: 5px;
    margin-right: 5px;
    margin-bottom: 1.5px;
    background-color: rgb(114, 111, 111);
}
.blog-manager:hover .dot-edit{
    background-color:black;
}
.blog-manager:hover {
    cursor: pointer;
}
.my-custom-class {
  background-color: red;
  color: white;
  border-radius: 5px;
}
</style>