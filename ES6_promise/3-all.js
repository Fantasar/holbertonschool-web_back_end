import { uploadPhoto, createUser } from './utils.js';

function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.all([
        uploadPhoto(fileName),
        createUser(firstName, lastName)
    ])
    .then(response => {
        const [photoResponse, userResponse] = response;
        console.log(photoResponse.body, userResponse.firstName, userResponse.lastName);
    })
    .catch(() => {
        console.log("Signup system offline");
    });
}
export default handleProfileSignup;