let newobj = new Set();
newobj.add("any text addddd");
newobj.add("Price and Learning");
newobj.add("ddddddddddddddd").add("ddddd");

newobj.delete("Price and Learning");
newobj.forEach(function(item){
    console.log(item);
})
console.log(newobj);
console.log(newobj.size);