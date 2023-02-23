<template>
    <div>
        <PublishArea isEditMode="true" 
                     title="post" />
    </div>
</template>

<script>
import PublishArea from "./PublishArea.vue";
export default{
    name: "EditBlog",
    components: { PublishArea }, 
}
</script>

