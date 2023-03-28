<template>
    <div>
        Error {{ message }}
    </div>
</template>

<script>
export default {
    name: "ErrorPage",
    props: ["message"]
}
</script>