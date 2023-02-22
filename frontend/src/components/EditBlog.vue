<template>
    <div>
        <PublishArea isEditMode="true" 
                     title="post.title" />
    </div>
</template>

<script>
import PublishArea from "./PublishArea.vue";
export default{
    name: "EditBlog",
    components: { PublishArea },
    data() {
        return {
            post: "",
        }
    },
    mounted(){
        const path = `http://127.0.0.1:5000/api/get/post/${this.$route.params.post_id}`;
        fetch(path, {
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
        .then(data => {
            this.post = data;
        })
        console.log(this.post);
    }
}
</script>

