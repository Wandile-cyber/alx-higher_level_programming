#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};

for (const key in dict) {
  const occurrence = dict[key];
  if (occurrence in sortedDict) {
    sortedDict[occurrence].push(key);
  } else {
    sortedDict[occurrence] = [key];
  }
}

console.log(sortedDict);
