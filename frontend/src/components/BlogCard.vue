<template>
<div class = "card" :id="post.id">
    <div class="container">
        <div class = "author-information">
            <div class = "author-profile-picture">
                IMG
            </div>
            <div class="dot"></div>
            <div v-if="!publisher" class = "author-name">{{ post.username }}</div>
            <div v-else class = "author-name">You</div>
            <div class="dot"></div>
            <div class = "published-date">{{ post.timestamp }}</div>
            <div v-if="publisher">
                <b-dropdown text=":"  variant = "none" size = "sm">
                    <b-dropdown-item href="#">Edit</b-dropdown-item>
                    <b-dropdown-item @click="delete_article">Delete</b-dropdown-item>
                </b-dropdown>
            </div>
        </div>
        
        <div class = "blog-body">
            <div class = "main-title"><h4><b>{{ post.title }}</b></h4>
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
    props: ["post", "publisher"],
    methods: {
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
                this.$emit('post-deletion');
            })
        }
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
}
.blog-manager{
    float: right;
}
.author-name, .published-date{
    margin-left: 0%;
}
.blog-body{
    float:left;
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
    margin-top: 12px;
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