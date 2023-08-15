#!/usr/bin/node
#!/usr/bin/node

const fs = require('fs');

const srcFile1 = process.argv[2]; 
const srcFile2 = process.argv[3];
const destFile = process.argv[4];

fs.writeFile(destFile, '', function (err) {
  if (err) throw err;

  fs.readFile(srcFile1, function (err, data) {
    if (err) throw err;

    fs.appendFile(destFile, data, function (err) {
      if (err) throw err;

      fs.readFile(srcFile2, function (err, data) {
        if (err) throw err;

        fs.appendFile(destFile, data, function (err) {
          if (err) throw err;
        }); 
      });
    });
  });
});
