
const json2md = require("json2md")
const fs = require('fs');
const lineReader = require('line-reader');
const textstats = require('./textstats.js');
const { forEach } = require("./textstats.js");

const webhook_time = new Date().toLocaleString("th-TH", { timeZone: "Asia/Bangkok" });
let yourDate = new Date().toISOString()

Array.prototype.randomElement = function () {
  return this[Math.floor(Math.random() * this.length)];
}

let rawdata = fs.readFileSync('img.json');
// let podata = JSON.parse(rawdata);
// let podata_t = podata.data.title.rendered;
// let podata_e = podata.data.excerpt.rendered;
// let podata_c = podata.data.content.rendered;
// let regex = /https?.+?(jpe?g|gif|png)/g
// let podata_com = podata_c.match(regex);
console.log(JSON.parse(rawdata[111]))
// let podata_sl = podata.data.title.rendered.replace(/[^\p{Latin}\p{Thai}\d\w]/g,"");

// let slname = (podata_t+podata_sl+podata_e).replace(/\s/g,"").substring(0, 25)
let pdata =[]


for (let i = 0; i < rawdata; i++) {
    
    
    console.log(rawdata[i])
    //pdata.push();
}
//console.log(num)

//console.log(pdata)
// let ttem =
// `---
// title: "100เรื่องพาดู ${datba[title]}"
// subtitle: "${datba[title]} ${textstats.randomElement()}"
// excerpt: "100เรื่อง ${datba[title]} ${textstats.randomElement()}"
// date: ${yourDate}
// thumb_image: ${datba[prev_url]}
// image: ${datba[prev_url]}
// Gimages: 
//   - ${datba[pack]}

// ---

// `
// const mdpost = (json2md([
//   [ttem]
//   , { blockquote: `100เรื่อง ${datba.title} ${textstats.randomElement()}`}
  
// ]))





// console.log(pdata);




// http://203.159.93.240:4040/raw/
// fs.writeFile(`data/100warp/${slname}.json`,JSON.stringify(jsda), 'utf8', function (err) {
//     if (err) {
//         console.log("An error occured while writing JSON Object to File.");
//         return console.log(err);
//     }

//     console.log("JSON file has been saved.");
// });

// fs.writeFile(`content/blog/100warp/${slname}.md`, mdpost, 'utf8', function (err) {
//     if (err) {
//         console.log("An error occured while writing JSON Object to File.");
//         return console.log(err);
//     }

//     console.log("JSON file has been saved.");
// });
// });