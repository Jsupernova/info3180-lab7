
<template>
<UploadForm></UploadForm>
</template>
<script>
import UploadForm from '@/components/UploadForm.vue'
    export default{
        data(){
            return{ message: "This is the upload page"};
        },
        components: {UploadForm}
    }
</script>