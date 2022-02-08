const time=document.querySelector(".js-time")

function getClock(){
    const date=new Date()
    let month=date.getMonth()
    if (month<12){
        month=month+1
    }
    const date1=String(date.getDate()).padStart(2,"0")
    const hours=String(date.getHours()).padStart(2,"0")
    const minutes=String(date.getMinutes()).padStart(2,"0")
    const seconds=String(date.getSeconds()).padStart(2,"0")
    time.innerText=`${month}/${date1}, ${hours}:${minutes}:${seconds}`
}

getClock()
setInterval(getClock, 1000);