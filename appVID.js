
const json2md = require("json2md")
const fs = require('fs');
const lineReader = require('line-reader');
const textstats = require('./textstats.js');



Array.prototype.randomElement = function () {
  return this[Math.floor(Math.random() * this.length)];
}

const webhook_time = new Date().toLocaleString("th-TH", { timeZone: "Asia/Bangkok" });
let yourDate = new Date().toISOString()


lineReader.eachLine('no.txt', (line, last) => {
    console.log(line);

let title_set = line.replace(/[^\w\s]/g,'').replace(/v_vide_/g,'100เรื่อง-น้องสาวเอเชีย_')

//let testFolder = "static/photo/"+line.split("/")[2]+"/"
//fs.readdir(testFolder, (err, files) => {
    //files.forEach(file => {
    //  console.log(file);
//    console.log(files.randomElement())
   
 
//let podata_sl = podata.data.title.rendered.replace(/[^\p{Latin}\p{Thai}\d\w]/g,"");

//let slname = (podata_t+podata_sl).replace(/\s/g,"").substring(0, 25)
//console.log("photo/"+line.split("/")[2]+"/")


let ttem =
`---
title: "${title_set.replace(/_/g,'')}"
subtitle: "${title_set.replace(/_/g,'')} ${textstats.randomElement()}"
description: "100เรื่อง ${textstats.randomElement()} ${title_set.replace(/_/g,'')} ${webhook_time}"
date: ${yourDate}
image: ""
type: "regular"
draft: false
---

![${title_set}](http://203.159.93.240:4040/raw/${line.replace("mp4","jpg")})

{{< video src="http://203.159.93.240:4040/raw/${line}" alt="${title_set} ${textstats.randomElement()}" >}}

`
//console.log(ttem);





const mdpost = (json2md([
    [ttem]
    , { blockquote: textstats.randomElement() + " "+ webhook_time }
    , { h2: title_set.replace(/_/g,'')}
]))


// fs.writeFile(`data/jav/${slname}.json`,JSON.stringify(jsda), 'utf8', function (err) {
//     if (err) {
//         console.log("An error occured while writing JSON Object to File.");
//         return console.log(err);
//     }

//     console.log("JSON file has been saved.");
// });

fs.writeFile(`content/english/blog/vidx/${title_set.replace(/_/g,'')}.md`, mdpost, 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing JSON Object to File.");
        return console.log(err);
    }

    console.log("JSON file has been saved.");
});
});
//});


