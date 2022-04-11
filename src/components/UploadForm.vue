<template>
    <div>
         <form @submit.prevent="uploadPhoto" enctype="multipart/form-data" id="uploadForm">
            <div class="alert alert-success" role="alert" v-if="on && success" v-for="message in messages">
                {{message}}
            </div>
            <div class="alert alert-danger" role="alert"  v-if="on && !success" >
                <div v-for="message in messages">
                    <li> {{message}}</li>
                </div>
            </div>
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
            return{
                        on: false,
                        success: false,
                        messages: []
                }
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
                    //undefined - no erros
                    console.log(data.errors);
                    if(data.errors!=undefined){
                        console.log(data)
                        let nextjson=data.errors.replace("['", "");
                        nextjson=nextjson.replace("']", "");
                        nextjson=nextjson.replace("'", "");
                        nextjson=nextjson.replace("'E", "E");
                        self.messages=nextjson.split(",");
                        self.on=true;
                        self.success=false;
                        console.log('hello');
                        console.log(self.messages);
                    }else{
                        console.log(data)
                        self.messages=[data.message];
                        self.on=true;
                        self.success=true;
                    }
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