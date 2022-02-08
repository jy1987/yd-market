const body=document.querySelector("body")

let factor=Date.now()

function getRandom(){
    const random=Math.floor(Math.random(factor)*4)
    return random    
}

function addRandomBg(){ 
    const number=getRandom()
    const newClassName=`hello${number}`
    const oldClassName=body.classList[3]
    
    localStorage.setItem("number",newClassName)
    body.classList.replace(oldClassName,newClassName)
}

function removeRandomBg(){
    const preClassName=localStorage.getItem("number")
    console.log(preClassName)
    body.classList.remove(preClassName)
}

setTimeout(body.classList.add(`hello${getRandom()}`), 0);
setInterval(addRandomBg, 3000);



