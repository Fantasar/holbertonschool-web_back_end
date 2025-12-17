function getFullResponseFromAPI(success) {
    return new Promise(function(resolve, reject) {
        if (success) {    
            const obj = {
                status: 200,
                body: 'Success'
            };
            resolve(obj);
        } else {
            reject(new Error("The fake API is not working currently"));
        }
    });
}

export default getFullResponseFromAPI;