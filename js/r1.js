// function loadScript(src, callback) {
//   let script = document.createElement('script');
//   script.src = src;
//   script.onload = () => callback(script);
//   document.head.append(script);
// }

// loadScript('https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.2.0/lodash.js', script => {
//   alert(`Cool, the script ${script.src} is loaded`);
//   alert( _ ); // function declared in the loaded script
// });
function addition(){

  for (i=0; i<100; i++){
    let a = i*i;
    let b = i*i*i;
    
    setTimeout(()=> {
      console.log("---")
      console.log(a+b);
    }, 20)

  }
}


function addition2(){

  for (i=0; i<100; i++){
    let a = 1;
    let b = i*i*i;
    console.log("***")
    console.log(a+b);

  }
}


// addition() 
// addition2()
// addition2()
item = {
  "a":1,
  "b":2,
  "c":3
}

console.log(item)

it2 = {
  ...item,
  "id":1234
}
console.log(it2)








