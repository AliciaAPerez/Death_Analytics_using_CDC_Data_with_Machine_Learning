let model;

const modelURL = 'http://localhost:5000/model';


// Select the button
let button = d3.select("#button");
// Create event handlers 
button.on("click", runEnter);

// Complete the event handler function for the form
function runEnter() {

  // Prevent the page from refreshing
    d3.event.preventDefault();

  // Select the input element and get the raw HTML node
    let inputElement1 = d3.select("#education");
    let inputElement2 = d3.select("#gender");
    let inputElement3 = d3.select("#age");
    let inputElement4 = d3.select("#marital");
    let inputElement5 = d3.select("#race");
    let inputElement6 = d3.select("#hispanic");

  // Get the value property of the input element
    let inputValue1 = inputElement1.property("value");
    let inputValue2 = inputElement2.property("value");
    let inputValue3 = inputElement3.property("value");
    let inputValue4 = inputElement4.property("value");
    let inputValue5 = inputElement5.property("value");
    let inputValue6 = inputElement6.property("value");

    let a = parseInt(inputValue1);
    let b = parseInt(inputValue2);
    let c = parseInt(inputValue3);
    let d = parseInt(inputValue4);
    let e = parseInt(inputValue5);
    let f = parseInt(inputValue6);

    let data = [a,b,c,d,e,f];
    console.log(data);
    // let input = (data, axis = 0)
    let answer = model.precdict(data)


    let list = d3.select(".results");

    // remove any children from the list to
    list.html("");

    // append stats to the list
    list.append("li").text(`You are going to die by Code: ${answer}`);
    list.append("li").text("Key:");
    list.append("li").text("Code 1: Heart Failure, Heart Attack, Heart Disease");
    list.append("li").text("Code 2: Cancer");
    list.append("li").text("Code 3: COPD");
    list.append("li").text("Code 4: Alzheimer's Disease");
    list.append("li").text("Code 5: Dementia");
    list.append("li").text("Code 6: Pneumonia or other Lung Disease");
    list.append("li").text("Code 7: Sepsis");
    list.append("li").text("Code 8: Diabetes");
    list.append("li").text("Code 9: Parkinson's Disease");
    list.append("li").text("Code 10: Accidental Poisoning By and Exposure to Drugs and Other Biological Substances");
    list.append("li").text("Code 11: Kidney Disease/Failure");
    list.append("li").text("Code 12: Cirrhosis of the Liver");
    list.append("li").text("Code 13: Slipping, Tripping, or Falling");
    list.append("li").text("Code 14: Self-Harm");
    list.append("li").text("Code 15: Auto Accident");

};
