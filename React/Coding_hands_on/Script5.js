let cats =["one Value","Two Value"];
let anyname =["Hello","World"];
//let newMovie =["sss","Hello","neee",cats,anyname];
let newMovie =["sss","Hello","neee",...cats,...anyname];
console.log(newMovie);