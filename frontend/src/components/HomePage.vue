<template>
  <div class="container" style = "min-height: 200%;!important">
    <div class = "row">
      <div class="col-md-1 col-lg-1 border " style = "padding-top:-10%;padding-bottom: 100%;">
        <NavBar />
      </div>
      <div class="col-7" style = "clear:both;float: left;padding-left: 6%;padding-top: 3%;">
        
        <h3 class="pb-3 mb-4 font-italic border-bottom">
            Blogs from people you follow
        </h3>
        <h4>
        </h4>
        <div v-if="current_user.follower_count > 0">
          <div  v-for="item in followerBlogs" :key="item.id" class="card mb-3 w-100" style="max-width: 200%;object-fit: contain">
            <div class="row g-0">
              <div class="col-md-8">
                <div class="card-body">
                  <a :href="`./view/writer_name={{ item.username }}&post_id={{ item.id }}`" style = "color: inherit;text-decoration:none;">
                    <h5 class="card-title">{{ item.title }}</h5>
                    <p class="card-text text-truncate">{{ item.caption }}...</p>
                  </a>
                  <p class="card-text" style="display: inline-block; margin-right: 0px;">
                    <small class="text-muted">Published by </small>
                  </p>
                  <p class="card-text" style="display: inline-block; margin-right: 0px;">
                    <small  class="text-muted">
                      <a :href="`./profile/{{ item.username }}`"  style = "color: inherit;">
                        {{ item.username }}
                      </a>
                    </small>
                  </p>
                  <p class="card-text" style="display: inline-block; margin-right: 0px;">
                    <small class="text-muted"> on {{ item.timestamp }}</small>
                  </p>
                </div>
              </div>
              <div class="col-md-4">
                <img v-if="item.image_url" :src="`${item.image_url}`" class="img-fluid rounded-start" style = "max-width: 100%; max-height: 100%;">
                <img v-else src="../assets/A_black_image.jpg" class="img-fluid rounded-start">
              </div>
            </div>
          </div>
        </div>
        <div v-else style="max-width: 200%;object-fit: contain">
          <h3>
            Mhm... Why such empty? 
            <img src = "../assets/beebee.png" width = 40 height = 30>
          </h3>
          <h4>
            Follow a few people to get some suggestions.
          </h4>
          <div class = "card" style = "margin-right: 50%;">
            <div class="card-body">
              <div v-for="user in userSuggestions" :key="user.username" class="card card-sm">
                <div class="card-body">
                  <div class = "row">
                    <div class = "col-7">
                      <h5>
                        {{ user.username }}
                      </h5>
                    </div>
                    <div class = "col">
                      <a :href="`/${current_user.username}/profile/${user.username}`" style = "color:inherit;text-decoration:none">
                        <button type="button" class="btn btn-success btn-sm">Visit Profile</button>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
    
    <!-- <div class="col-7" style = "clear:both;float: left;padding-left: 6%;padding-top: 3%;">
      <h3 class="pb-3 mb-4 font-italic border-bottom">
        Blogs from people you follow
      </h3>
      {% if recent_feed_data | length == 0 %}
        <p>
          <h3>
            Mhm... Why such empty? 
            <img src = "/static/beebee.png" width = 40 height = 30>
          </h3>
        </p>
        <h4>
          Follow a few people to get some suggestions.
        </h4>
        <div class = "card" style = "margin-right: 50%;">
          <div class="card-body">
            {% for user in some_users %}
              <div class="card card-sm">
                <div class="card-body">
                  <div class = "row">
                    <div class = "col-7">
                      <h5>
                        {{ user.username }}
                      </h5>
                    </div>
                    <div class = "col">
                      <a href="/{{ username }}/profile/{{ user.username }}" style = "color:inherit;text-decoration:none">
                        <button type="button" class="btn btn-success btn-sm">Visit Profile</button>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
           {% endfor %}
          </div>
        </div>
      {% else %}
        {% for post in recent_feed_data %}
        <div class="card mb-3 w-100" style="max-width: 200%;object-fit: contain">
          <div class="row g-0">
            <div class="col-md-8">
              <div class="card-body">
                <a href="./view/writer_name={{ post.username }}&post_id={{ post.id }}" style = "color: inherit;text-decoration:none;">
                  <h5 class="card-title">{{ post.title }}</h5>
                  <p class="card-text text-truncate">{{ post.caption }}...</p>
                </a>
                <p class="card-text" style="display: inline-block; margin-right: 0px;">
                  <small class="text-muted">Published by </small>
                </p>
                <p class="card-text" style="display: inline-block; margin-right: 0px;">
                  <small  class="text-muted">
                    <a href = "./profile/{{ post.username }}"  style = "color: inherit;">
                      {{ post.username }}
                    </a>
                  </small>
                </p>
                <p class="card-text" style="display: inline-block; margin-right: 0px;">
                  <small class="text-muted"> on {{ post.timestamp[:-9] }}</small>
                </p>
              </div>
            </div>
            <div class="col-md-4">
              {% if post.image_url != "" and post.image_url is not none %}
              <img src="{{ post.image_url }}" class="img-fluid rounded-start" style = "max-width: 100%; max-height: 100%;">
              {% else %}
              <img src="/static/A_black_image.jpg" class="img-fluid rounded-start">
              {% endif %}
            </div>
          </div>
        </div>
        {% endfor %}
      {% endif %}
    </div>
    <div class="col-3" style = "padding-top: 3.8%;">
      <form action = "./homepage/search/" class="d-flex" style = "position: fixed">
        <input name = "searched_username" class="form-control me-2" type="search" placeholder="Search" aria-label="Search" autocomplete="off">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
      <br>
      <div style = "position: fixed">
        <br>
        <p>
          <h4 class="pb-2 mb-4 font-italic border-bottom" style="max-width: 42%;object-fit: contain;">
            For you
            <img src = "/static/for_you_sparkle.png" width = 30 height = 25>
          </h4>
        </p>
          {% for post in recommended_posts %}
          <div class="card mb-3 w-100" style="max-width: 42%;object-fit: contain;">
            <div class="row g-0">
              <div class="col-md-8">
                <div class="card-body">
                  <a href="./view/writer_name={{ post.username }}&post_id={{ post.id }}" style = "color: inherit;text-decoration:none;">
                    <h5 class="card-title">{{ post.title }}</h5>
                  </a>
                </div>
              </div>
              <div class="col-md-4">
                {% if post.image_url != "" and post.image_url is not none %}
                <img src="{{ post.image_url }}" class="img-fluid rounded-start" style = "max-width: 100%; max-height: 100%;">
                {% else %}
                <img src="/static/A_black_image.jpg" class="img-fluid rounded-start">
                {% endif %}
              </div>
            </div>
          </div>
          {% endfor %}
      </div>
    </div>
{% endblock %} -->
</template>

<script>
// NEED TO DESTROY THE TOKEN WHEN A USER LOGS OUTTTTTTT.
import NavBar from "./NavBar.vue";
export default {
    extends: NavBar,
    components: {
      NavBar
    },
    data() {
        return {
            followerBlogs: [],
            userSuggestions: [],
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
      // Used if user has followers.
      console.log(this.current_user);
      console.log(this.current_user);
      const path1 = `http://127.0.0.1:5000/api/${this.$route.params.username}/homepage`;
      fetch(path1, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(response => response.json())
      .then(data => {
        this.followerBlogs = data
      });

      // Used if user has no followers.
      const path2 = `http://127.0.0.1:5000/api/${this.$route.params.username}/homepage`;
      fetch(path2, {
        headers: {"Authorization": localStorage.jwtToken}
      })
      .then(response => response.json())
      .then(data => {
        this.userSuggestions = data
      });
    },
}

</script>