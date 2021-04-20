// CONVERT KERAS MODEL TO TENSORFLOW IN GIT BASH WINDOW USING THE FOLLOWING COMMAND
// tensorflowjs_converter --input_format keras ./static/js/Death_machine_1.h5 ./static/js/tfjs_dir

// import * as tf from '@tensorflow/tfjs';

// const model = await tf.loadLayersModel("{{ url_for('static', filename='js/tfjs_dir/model.json') }}");

// const model = await tf.loadLayersModel("static/js//tfjs_dir/model.json");

async function testModel() {
  const model = await tf.loadLayersModel("static/js//tfjs_dir/model.json");
  model.predict();
  
}
// testModel();

// const example = tf.fromPixels(webcamElement);  // for example
// const prediction = model.predict(example);


// let model = "{{ url_for('static', filename='js/Death_machine_1.h5') }}";
// console.log(model)

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
    // console.log(data.shape);
    // let input = nj.array(data).reshape(1, data.length)
    
    // let x_array = nj.array(data);
    // let input = x_array.reshape(1,(data.length));
    
    // let input = x_array.reshape((data.length), 1);

//     t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
// print(tf.shape(t).numpy())

// tf.reshape(t, [3, 3])

    let input = tf.tensor(data);



    // input = nj.array(data).reshape(1, data.length)
    // console.log(x_array);
    // console.log(x_array.shape);
    
    // let input = tf.tensor1d(data)
    
    console.log(input);
    console.log(input.shape);
    
    // let results = model.precdict(input);

    
    async function testModel(input) {
      const model = await tf.loadLayersModel("static/js//tfjs_dir/model.json");
      model.predict(input);
      
    }

    let results = testModel(input);

    for (i in results)
      {
      let x = i[0]
      let answer = round(x)
      print(answer)
    };

    console.log(answer)

    let list = d3.select(".results");

    // remove any children from the list to
    list.html("");

    // append stats to the list
    list.append("li").text(`Results`);
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

// Codes that got used
// icd_death_code
// C349    126123
// I219     92574
// G309     84389
// I500     59880
// I250     55043
// I48      19208
// W19      14784
// I350     12079


// icd_death_code
// I251    428754
// C349    126123
// J449     94129
// F03      92868
// G309     84389
// J189     36206
// A419     32554
// E149     25512
// G20      22682
// X44      19194
// N185     15933
// K746     15325
// W19      14784
// X74      12859
// V892     11247
// X95      11184