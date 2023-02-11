<template>
<div>
    <div class = "div1">
        Box1
    </div>
    <div class = "div2">
        <img src = "..//../assets/picture1.jpg">
        <div class = "innerDiv2">
            <div class = "innerDiv3">
                
            </div>
        </div>
        <div class = "innerDiv4">
            innerBox3
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "AuthViews",
};
</script>

<style>
.div1{
    background-color: rgb(241, 247, 247);
    width: 50%;
    float:left;
    height: 100vh;
}
.div2{
    background-color: rgb(231, 201, 201);
    width: 50%;
    float: right;
    height: 100vh;
    border-left: 3px solid #1d1c1c;
}
.innerDiv2{
    background:rgb(157, 228, 184);
    height: 50vh;
    border-bottom: 3px solid #1d1c1c;
}
.innerDiv3{
    background:rgb(172, 137, 238);
    height: 50vh;
    width: 60vh;
    border-right: 3px solid #1d1c1c;
    border-bottom: 3px solid #1d1c1c;
}

.innerDiv4{
    background:rgb(240, 122, 214);
    height: 100vh;
    width: 30vh;
    border-right: 3px solid #1d1c1c;
    border-bottom: 3px solid #1d1c1c;
}
img{
    object-fit: cover;
}
</style>