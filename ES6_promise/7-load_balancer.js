export default function loadBalancer(chinaDownload, USDownload) {
    return Promise.race([chinaDownload, USDownload])
        .then(result => {
            return result;
        })
        .catch(error => {
            throw new Error("Une erreur est survenue : " + error.message);
        });
}