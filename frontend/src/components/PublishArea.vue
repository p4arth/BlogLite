<template>
<div>
    <div class = "container">
        <div class = "publish-bar">
            <div style = "float: right;padding-left: 1%;">
                DropDown
            </div>
            <div style = "float:right;padding-left: 1%;">   
                <button v-if="!isEditMode" @click="publish">Publish</button>
                <button v-else @click="edit">Publish</button>
            </div>
            
        </div>
        <textarea v-if="!isEditMode" id = "title" placeholder="Title"></textarea>
        <textarea v-else id = "title" placeholder="Title" v-model="post.title"></textarea>
        <textarea v-if="!isEditMode" id = "content" placeholder="Write Something..."></textarea>
        <textarea v-else 
                  id = "content" 
                  placeholder="Write Something..."
                  v-model="post.caption">
                </textarea>
        <textarea v-if="!isEditMode" id = "image" placeholder="Enter image url"></textarea>
        <textarea v-else 
                  id = "image" 
                  placeholder="Enter image url"
                  v-model="post.image_url">
                </textarea>
    </div>
</div>
</template>

<script>
export default {
    name: "PublishArea",
    props: ["isEditMode"],
    data() {
        return {
            post: "",
        };
    },
    created(){
        if(this.isEditMode){
            const path = `http://127.0.0.1:5000/api/get/post/${this.$route.params.post_id}`;
            const response = fetch(path, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            const postData = async () => {
                this.post = await response;
                console.log(this.post);
            }
            postData();
            
        }
    },
    mounted() {
        console.log(this.post);
        const textArea = document.getElementById('title');
        textArea.addEventListener('input', function() {
            if(this.scrollHeight !== 54){
                this.style.height = 'auto';
                this.style.height = this.scrollHeight + 'px';
            }
            if(textArea.value.trim() === ""){
                this.style.height = "54px";
            }
        });
        const contentArea = document.getElementById('content');
        contentArea.addEventListener('input', function() {
            if(this.scrollHeight !== 40){
                this.style.height = 'auto';
                this.style.height = this.scrollHeight + 'px';
            }
            if(contentArea.value.trim() === ""){
                this.style.height = "40px";
            }

        });
    },
    methods: {
        publish: function() {
            const title = document.getElementById("title").value;
            const content = document.getElementById("content").value;
            const image = document.getElementById("image").value;
            const path = `http://127.0.0.1:5000/api/${localStorage.currUser}/publish_new_article`;
            fetch(path, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': localStorage.jwtToken
                },
                body: JSON.stringify({
                    'title': title,
                    'caption': content,
                    'image-link': image,
                })
            }).then(response => {
                if (response.ok) {
                    console.log(response.json());
                } else {
                    throw new Error('API respone was not OK');
                }
            })
        },
        edit: function(){
            const title = document.getElementById("title").value;
            const content = document.getElementById("content").value;
            const image = document.getElementById("image").value;
            const path = `http://127.0.0.1:5000/api/${localStorage.currUser}/edit/post`;
            fetch(path, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': localStorage.jwtToken
                },
                body: JSON.stringify({
                    'post_id': this.post.id,
                    'title': title,
                    'caption': content,
                    'image-link': image,
                })
            }).then(response => {
                if (response.ok) {
                    console.log(response.json());
                } else {
                    throw new Error('API respone was not OK');
                }
            })
        }
    }

}
</script>

<style scoped>
.container{
    margin-top: 0.5%;
}
button {
  background-color: green;
  color: white;
  border: none;
  border-radius: 20px;
  padding: 10px 20px;
  margin-bottom: 10px;
  font-size: 14px;
}


/* .publish-bar{
    float:right;
} */
#title{
    resize: none;
    overflow: hidden;
    background-color: rgb(250, 247, 247);
    border-top: none;
    border-bottom: none;
    border-right: none;
    border-left: 5px solid rgb(181, 184, 184);
    width: 100%;
    height: 54px;
    outline: none;
    font-size: xx-large;
    margin-bottom: 1%;
}
#content{
    resize: none;
    overflow: hidden;
    background-color: rgb(250, 247, 247);
    border-top: none;
    border-bottom: none;
    border-right: none;
    border-left: 5px solid rgb(181, 184, 184);
    width: 100%;
    height: 40px;
    outline: none;
    font-size: x-large;
}
#title:focus, #content:focus{
    background-color: rgb(214, 219, 219);
}
</style>