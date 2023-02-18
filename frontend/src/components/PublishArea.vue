<template>
<div>
    <div class = "container">
        <div class = "publish-bar">
            <div style = "float: right;
                          padding-left: 1%;">
                DropDown
            </div>
            <div style = "float:right;padding-left: 1%;">   
                <button>
                    Publish
                </button>
            </div>
            
        </div>
        <textarea id = "title" placeholder="Title"></textarea>
        <textarea id = "content" placeholder="Write Something..."></textarea>
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
            console.log(this.scrollHeight);
            if(this.scrollHeight !== 40){
                this.style.height = 'auto';
                this.style.height = this.scrollHeight + 'px';
            }
            if(contentArea.value.trim() === ""){
                this.style.height = "40px";
            }
        });
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