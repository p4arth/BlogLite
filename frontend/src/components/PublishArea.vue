<template>
<div>
    <div class = "container">
        <div class = "publish-bar">
            <div style = "float: right;padding-left: 1%;">
                DropDown
            </div>
            <div style = "float:right;padding-left: 1%;">   
                <button @click="publish">
                    Publish
                </button>
            </div>
            
        </div>
        <textarea id = "title" placeholder="Title"></textarea>
        <textarea id = "content" placeholder="Write Something..."></textarea>
        <textarea id = "image" placeholder="Enter image url"></textarea>
    </div>
</div>
</template>

<script>
export default {
    name: "PublishArea",
    mounted() {
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
            // console.log(this.scrollHeight);
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