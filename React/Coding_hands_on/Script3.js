let course = new Map();
course.set("react", { description: "hello" });
course.set("Jest", { description: "testing" });
console.log(course);
console.log(course.react);
console.log(course.get("react"));

let details = new Map([
    [new Date(), "today"],
    [2, { javascript: ["js", "node", "react"] }],
    ["items", [2, 3]],
    ["items2222", [3, 3]]

])
details.forEach(function (item) {
    console.log(item);
});

console.log(details.size)