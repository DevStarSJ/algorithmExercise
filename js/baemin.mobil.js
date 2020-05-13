const _ = require('lodash');
const Mocha = require('mocha')
const assert = require('assert')
const mocha = new Mocha()

class Mobil {
  constructor(value, count) {
    this.value = value;
    this.count = count;
  }
  
  merge(right) {
    this.value += right.value
    this.count += right.count
  }
}

function t1(arr) {

}

function countmap(arr) {
  let cm = {}
  arr.forEach(e => cm[e] = cm[e] ? cm[e] + 1 : 1)
  return cm
}

function toMobils(arr) {
  return arr.map(e => new Mobil(e, 1))
}

function toArr(mobilArr) {
  return mobilArr.map(m => m.value)
}

function step(mobilArr) {
  const arr = toArr(mobilArr)
  const cm = countmap(arr)
  const valuesMoreThanTwo = Object.keys(cm).map(key => cm[key] >= 2 ? key : null).filter(e => e > 0)
  
  if (valuesMoreThanTwo.length === 0) return false
  
  const minValueMoreTwo = Math.min(...valuesMoreThanTwo)
  const doubleMinValue = minValueMoreTwo * 2
  
  const moreBiggerThanDoubleMinValueAndHasTwoOrMoreKeys = valuesMoreThanTwo.filter(e => e < doubleMinValue)
  
  moreBiggerThanDoubleMinValueAndHasTwoOrMoreKeys.forEach(value => {
    while (true) {
      const first = popBestMobilOfThisValue(mobilArr, value)
      const second = popBestMobilOfThisValue(mobilArr, value)
      
      if (first === undefined || second === undefined) break;
      
      first.merge(second)
      mobilArr.push(first)
    }
  })
  
  return true
}

function run(arr) {
  const mobilArr = toMobils(arr);
  while (step(mobilArr)) { }
  
  return Math.max(...mobilArr.map(m => m.count)) || 1
}


function popBestMobilOfThisValue(mobilArr, value) {
  let selected = undefined;
  let bestCount = -1;
  mobilArr.forEach( (m, index) => {
    if (m.value != value) return;
    if (m.count > bestCount) {
      bestCount = m.count
      selected = index
    }
  })
  
  if (selected === undefined) return undefined;
  
  const popedMobil = mobilArr[selected]
  mobilArr.splice(selected, 1)
  
  return popedMobil
}

const q1 = [2,2,2,2,3,3,5,6];
const q2 = [3,3,3,3,3,3,12];
const q3 = [16,16,16,16,16,16,16,16,11,2,4,4]
const q4 = [1]

console.log(run(q1))
console.log(run(q2))
console.log(run(q3))
console.log(run(q4))


// Bit of a hack, sorry!
mocha.suite.emit('pre-require', this, 'solution', mocha)

describe('Test suite', function() {
  // it('popBestMobilOfThisValue', function() {
  //   assert(run(q1) === 4)
  //   assert(run(q2) === 5)
  // })
})

mocha.run()
