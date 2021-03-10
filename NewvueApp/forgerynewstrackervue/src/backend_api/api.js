import axios from 'axios';

export default class Backendapi {
    getMessages(query){
        console.log(query);

        const path = 'http://localhost:5000/showinfo';
        return axios.post(path, {query}).then((res) => {
           return res.data

        })
        .catch((error) => {
            console.error(error);
        });
    }
} 