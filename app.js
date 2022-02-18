
const json2md = require("json2md")
const fs = require('fs');
const lineReader = require('line-reader');

function readFiles(dirname, onFileContent, onError) {
    fs.readdir(dirname, function(err, filenames) {
      if (err) {
        onError(err);
        return;
      }
      filenames.forEach(function(filename) {
        fs.readFile(dirname + filename, 'utf-8', function(err, content) {
          if (err) {
            onError(err);
            return;
          }
          onFileContent(filename, content);
        });
      });
    });
  }

const webhook_time = new Date().toLocaleString("th-TH", { timeZone: "Asia/Bangkok" });
let yourDate = new Date().toISOString().split('T')[0]


lineReader.eachLine('no.txt', (line, last) => {
    console.log(line);


let rawdata = fs.readFileSync(line);
let podata = JSON.parse(rawdata);
let podata_t = podata.data.title.rendered;
let podata_e = podata.data.excerpt.rendered;
let podata_c = podata.data.content.rendered;
let regex = /https?.+?(jpe?g|gif|png)/g
let podata_com = podata_c.match(regex);

let podata_sl = podata.data.title.rendered.replace(/[^\p{Latin}\p{Thai}\d\w]/g,"");

let slname = (podata_t+podata_sl+podata_e).replace(/\s/g,"").substring(0, 25)

let jsda = {
    title: podata_t || podata_e,
    images: podata_com,
    excerpt: slname + podata_t + podata_e,
    first_name: "100เรื่อง "+podata_t,
    last_name: "PNCKDEVAPP"
}


let ttem =
`---
title: ${podata_t} ${podata_sl} ${podata_e}
subtitle: '100เรื่อง ${podata_t} ${podata_e}'
author: data/100warp/${slname}.json
excerpt: 100เรื่อง ${podata_t} ${podata_e} ${slname}
date: '${yourDate}'
thumb_image: ${podata_com[0]}
image: ${podata_com[0]}
layout: posted
depost: data/100warp/${slname}.json
---`

const mdpost = (json2md([
    [ttem]
    , { blockquote: "100เรื่อง "+ podata_e +" "+ podata_t +" "+ webhook_time }
    , {
        img: [
            { title: podata_t + podata_e, source: podata_com[0] }
        ]
    }
]))


fs.writeFile(`data/100warp/${slname}.json`,JSON.stringify(jsda), 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing JSON Object to File.");
        return console.log(err);
    }

    console.log("JSON file has been saved.");
});

fs.writeFile(`content/blog/100warp/${slname}.md`, mdpost, 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing JSON Object to File.");
        return console.log(err);
    }

    console.log("JSON file has been saved.");
});
});