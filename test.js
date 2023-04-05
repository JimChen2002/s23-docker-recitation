module.paths.push('/Users/jimchen/.nvm/versions/node/v16.15.1/lib/node_modules');
// const fetch = require("node-fetch");
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

function trigger(){
    console.log("connecting");
    fetch('https://red-haze-9902.fly.dev/predict', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            student_id: 1,
            major: "Statistics and Machine Learning",
            age: 21,
            gender: "M",
            gpa: "4.00",
            extra_curricular: "Sorority",
            num_programming_languages: 10,
            num_past_internships: 10,
        })
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}

trigger()