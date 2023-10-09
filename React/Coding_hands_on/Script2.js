const id = Symbol();
const courseInfo ={
    title:"Javascript",
    topics:["String2","Arrays","Objects"],
    id:"Js-course"
};
courseInfo[id] =41234;
console.log(courseInfo)