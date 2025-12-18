import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup (firstName, lastName, fileName) {
    return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)
    ])
    .then(values => {
        return values.map(value => ({
            status: 'resolved',
            value: value
        }));
    })
    .catch(err => {
        return [
            {
                status: 'rejected',
                value: err.message
            }
        ];
    });
}