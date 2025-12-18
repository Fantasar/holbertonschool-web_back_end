import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.all([
        uploadPhoto(),
        createUser()
    ])
    .then(response => {
        const [photoResponse, userResponse] = response;
        console.log(photoResponse.body, userResponse.firstName, userResponse.lastName);
    })
    .catch(() => {
        console.log("Signup system offline");
    });
}