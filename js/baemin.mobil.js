const Mocha = require('mocha')
const assert = require('assert')
const mocha = new Mocha()
const _ = require('functional-ts')

class Mobile {
  constructor(value, count) {
    this.value = value;
    this.count = count;
  }
  
  merge(right) {
    this.value += right.value
    this.count += right.count
  }
}

function countmap(numbers) {
  let cm = {}
  numbers.forEach(e => cm[e] = cm[e] ? cm[e] + 1 : 1)
  return cm
}

const toMobiles = numbers => numbers.map(e => new Mobile(e, 1))
const toNumbers = mobiles => mobiles.map(m => m.value)
const doubleMinValueOf = values => Math.min(...values) * 2
const findBestCountOf = mobiles => Math.max(...mobiles.map(m => m.count)) || 1
const getMoreThanTwoCountsOf = countMap => Object.keys(countMap)
  .map(key => countMap[key] >= 2 ? key : null)
  .filter(e => e > 0)

function valuesOfMoreThanDoubleMin(values) {
  const doubleMinValue = doubleMinValueOf(values)
  return values.filter(e => e < doubleMinValue)
}

function run(numbers) {
  const mobiles = toMobiles(numbers);
  while (step(mobiles)) { }
  return findBestCountOf(mobiles)
}

function step(mobiles) {
  const cm = _.go(mobiles, toNumbers, countmap)
  const valuesOfMoreThanTwoCounts =getMoreThanTwoCountsOf(cm)

  if (valuesOfMoreThanTwoCounts.length === 0) return false
  
  valuesOfMoreThanDoubleMin(valuesOfMoreThanTwoCounts).forEach(value => {
    while (mergeMobilesLessThan(mobiles, value)) { }
  })
  
  return true
}

function mergeMobilesLessThan(mobiles, value) {
  const first = popBestMobileOfValue(mobiles, value)
  const second = popBestMobileOfValue(mobiles, value)
  
  if (first === undefined || second === undefined) return false;
  
  first.merge(second)
  mobiles.push(first)

  return true;
}

function popBestMobileOfValue(mobiles, value) {
  const selected = findBestMobileOfValue(mobiles, value);
  
  if (selected === undefined) return undefined;
  
  const popedMobile = mobiles[selected]
  mobiles.splice(selected, 1)
  
  return popedMobile
}

function findBestMobileOfValue(mobiles, value) {
  let selected = undefined;
  let bestCount = -1;
  mobiles.forEach((mobile, index) => {
    if (mobile.value != value)
      return;
    if (mobile.count > bestCount) {
      bestCount = mobile.count;
      selected = index;
    }
  });
  return selected;
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
// mocha.suite.emit('pre-require', this, 'solution', mocha)

// describe('Test suite', function() {
//   // it('popBestMobileOfValue', function() {
//   //   assert(run(q1) === 4)
//   //   assert(run(q2) === 5)
//   // })
// })

// mocha.run()
