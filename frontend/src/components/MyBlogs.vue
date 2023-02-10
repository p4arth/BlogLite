<template>
<div class="container" style = "min-height: 200%;!important">
        <div class = "row">
            <div class="col-md-1 col-lg-1 border " style = "padding-top:-10%;padding-bottom: 100%;">
                <NavBar />
            </div>
            <div class="col-7" style = "clear:both;float: left;padding-left: 6%;padding-top: 3%;">
                <h3 class="pb-3 mb-4 font-italic border-bottom">
                    Blogs published by You
                </h3>
                <div v-for="post in followerPosts" :key=post.id class="card mb-3" style="max-width: 210%;object-fit: contain">
                    <div class="row g-0">
                        <div class="col-md-8">
                            <div class="card-body">
                                <a :href="`./view/post_id=${post.id}`" style = "color: inherit;text-decoration:none;">
                                    <h5 class="card-title">{{ post.title }}</h5>
                                    <p class="card-text">{{ post.caption.slice(0, 50) }}...</p>
                                </a>
                                <!-- DROP DOWNS ARE NOT WORKING ANYWHERE -->
                                <div class="dropdown">
                                    <p class="card-text" style = "display: inline-block;">
                                        <small class="text-muted">
                                            Published by you on {{ post.timestamp }}
                                        </small>
                                    </p>
                                    <button class="btn btn-sm dropdown-toggle" type="button" id="dropdownBlogButton" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    </button>
                                    <div class="dropdown-menu" aria-labelledby="dropdownBlogButton">
                                        <a class="dropdown-item" :href="`./edit/post_id=${post.id}`">Edit</a>
                                        <a class="dropdown-item" href="#" data-bs-toggle="modal" :data-bs-target="`#deleteModal${post.id}`">
                                            Delete
                                        </a>
                                    </div>
                                </div>
                                <div class="modal fade" id="`#deleteModal${post.id}`" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="exampleModalLabel">Are you sure you want to delete this Blog?</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <div class="modal-body">
                                                <div style = "text-align: center;">
                                                    <button type="button" class="btn btn-success">
                                                    <a :href = "`./delete/post_id=${post.id}`" style="color: inherit;text-decoration: None;">
                                                        Yes
                                                    </a>
                                                    </button>
                                                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">No</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4" style = "text-align: center;">
                            <img v-if="post.image_url !== ''" :src="`${post.image_url}`" class="img-fluid rounded-start" alt="...">
                            <img v-else src="/static/A_black_image.jpg" class="img-fluid rounded-start" alt="...">
                        </div>
                    </div>
                </div>
            </div>
        </div>
</div>
</template>

<script>
import NavBar from "./NavBar.vue";
export default {
    extends: NavBar,
    components: {
        NavBar
    },
    data() {
        return {
            followerPosts: [],
            current_user: "",
        }
    },
    created(){
      // Get details about the current user.
      const userPath = `http://127.0.0.1:5000/api/${this.$route.params.username}`;
      fetch(userPath, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(reponse => reponse.json())
      .then(data => this.current_user = data);
    },
    mounted() {
      // Used to get blogs by the current user.
      const path1 = `http://127.0.0.1:5000/api/${this.$route.params.username}/my-blogs`;
      fetch(path1, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(response => response.json())
      .then(data => {
        this.followerPosts = data
      });
    },
}
</script>

<style>
  .dot {
  width:5px;
  height:5px;
  background-color:gray;
  border-radius:20%;
  margin:2px;
}
</style>