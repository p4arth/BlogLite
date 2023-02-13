<template>
<div class = "card">
    <div class="container">
        <div class = "author-information">
            <div class = "author-profile-picture">
                IMG
            </div>
            <div class="dot"></div>
            <div class = "author-name">{{ post.username }}</div>
            <div class="dot"></div>
            <div class = "published-date">{{ post.timestamp }}</div>
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
    props: ["post"],
}
</script>

<style scoped>
.card{
    width: 65%;
    border-radius: 0%;
    padding-bottom: 2%;
    border: none;
    border-bottom:  2px solid #e0dcdc;
}
.author-information{
    display: flex;
    margin-top: 2%;
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
    margin-top: 2%;
    margin-right: 10%;
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

</style>