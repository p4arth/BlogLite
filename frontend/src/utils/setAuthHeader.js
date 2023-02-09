import axios from "axios";

const setAuthHeader = (token) => {
    if (token){
        axios.defaults.headers = {
            Authorization: token,
        };
    }
    else{
        delete axios.defaults.headers.Authorization;
    }
};

export default setAuthHeader;