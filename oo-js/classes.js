// Javascript OO

function Building(floors) {
  this.type = "building";
  this.floors = floors;
}

// Adding a static method to the Building class
Building.prototype.countFloors = function() {
  console.log('I have ', this.floors, ' floors');
};

// Not using new will polute the global scope
// const dasIstNichtMeinHaus = Building(4);

const meinHaus = new Building(4);
// console.log('this is undefined...', dasIstNichtMeinHaus);
console.log(meinHaus);

// console.log('the global object was contaminated', window.type, window.floors);

meinHaus.countFloors();

