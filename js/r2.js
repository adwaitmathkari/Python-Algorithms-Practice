
function a0() {

    let promise = new Promise(function (resolve, reject) {
        console.log("executing promise")
        setTimeout(() => {
            console.log("done")
            resolve(1)
        }, 3000);
    });



    let promise2 = new Promise(function (resolve, reject) {
        console.log("executing promise")
        setTimeout(() => {
            console.log("done")
            resolve(1)
        }, 1000);
    });


}
// promise.then("do something")

// console.log("async????")


// promise2.then(function (result) {
//     console.log('promies2', result); // 1
//     return result * 2;
// });

// promise.then(function (result) {
//     console.log(result); // 1
//     return result * 2;
// });

// promise.then(function (result) {
//     console.log(result); // 1
//     return result * 2;
// });



function a() {


    let p = new Promise(function (resolve, reject) {

        setTimeout(() => resolve(1), 1000);

    }).then(function (result) {

        console.log(result); // 1

        return new Promise((resolve, reject) => { // (*)
            setTimeout(() => resolve(result * 2), 1000);
        });

    }).then(function (result) { // (**)

        console.log(result); // 2

        return new Promise((resolve, reject) => {
            setTimeout(() => resolve(result * 2), 1000);
        });

    }).then(function (result) {

        console.log(result); // 4

    });





}

async function showAvatar() {

    // read our JSON
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            let a = 100;
            resolve(a)
        }, 5000);

    })

    let response = await promise;
    let user = await response.json();

    // read github user
    let githubResponse = await fetch(`https://api.github.com/users/${user.name}`);
    let githubUser = await githubResponse.json();

    console.log(githubUser)
    // show the avatar
    let img = document.createElement('img');
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.append(img);

    // wait 3 seconds
    await new Promise((resolve, reject) => setTimeout(resolve, 3000));

    img.remove();

    return githubUser;
}

// showAvatar();


const calculate = ( {price, discount} ) => {
    console.log(price)
    console.log(discount)
    return price - discount * price;
}

const payment = calculate(100, 0.1);
console.log(payment) // logs NaN

