#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const file1Content = fs.readFileSync(sourceFile1, 'utf-8');
const file2Content = fs.readFileSync(sourceFile2, 'utf-8');

const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Files ${sourceFile1} and ${sourceFile2} have been concatenated into ${destinationFile}`);
