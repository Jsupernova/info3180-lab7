<template>
    <div>
         <form @submit.prevent="uploadPhoto" enctype="multipart/form-data" id="uploadForm">
            <div class="form-group">
                <label for="description">Description</label>
                <textarea class="form-control" name="description" id="description" placeholder="Enter description here"></textarea>
            </div>
            <div class="form-group">
                <label for="photo">Photo</label>
                <input name="photo" id="photo" type="file">
            </div>
             <button type=submit class="btn btn-primary" > Submit </button>
        </form>
    </div>
</template>

<script>
    export default {
        data(){
            csrf_token: ''
            return{uploadForm:{
                description:'',
                image:''
            }};
        },
        methods:{
            uploadPhoto()
            {
                self=this;
                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm);
               
                fetch("/api/upload", {
                    method: 'POST',
                    body: form_data,
                    headers: {
                        'X-CSRFToken': this.csrf_token
                        }
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    // display a success message
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            getCsrfToken()
            {
            let self = this;
                fetch('/api/csrf-token')
                    .then((response) => response.json())
                    .then((data) => {
                        console.log(data);
                        self.csrf_token = data.csrf_token;
                })
            }
        },
        created() {
            this.getCsrfToken();
        },
        
    }
</script>

<style>
    .textar textarea{
        width: 90%;
    }

    button{
        background: rgb(0, 81, 255);
        color: aliceblue;
        text-align: center;
    }
</style>