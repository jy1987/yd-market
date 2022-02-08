const select=document.querySelector(".js-select")
const selectAll=select.querySelectorAll("select")
const result=document.querySelector("#result")

fetch('http://192.168.1.14:5000/api', {
    method: 'POST',
    headers: {
        'Content-Type': 'text/html'
    },
    
    })


function handleTitleClick(){
    const clickedClass="clicked"
    title.classList.toggle(clickedClass)
}

function submitSelect(e){
    e.preventDefault()
    console.log(e)
    const input0=selectAll[0].value
    const input1=selectAll[1].value
    const input2=selectAll[2].value
    const input3=selectAll[3].value
    const input4=selectAll[4].value
    const input5=selectAll[5].value
    console.log(input0, input1, input2, input3, input4, input5)
    if(input0.length>0 &&input1.length>0&&input2.length>0&&input3.length>0&&input4.length>0&&input5.length>0){
        const inputArray={"arrival":input0, "destination":input1, "carrier":input2, "shipping":input3, "day1":input4, "day2":input5}
        console.log(inputArray)
        select.classList.add("hidden")
        displayResult(JSON.stringify(inputArray))
        localStorage.setItem("input",JSON.stringify(inputArray))   
    }else{
        alert("모든 항목을 선택해주세요")
    }
}

function displayResult(input){
    result.innerText=`you chose ${input}`
    result.classList.remove("hidden")
}

const savedInput=localStorage.getItem("input")

if(savedInput===null){
    select.classList.remove("hidden")
    select.addEventListener("submit", submitSelect)
}else{
    console.log(savedInput)
    displayResult(savedInput)
}

