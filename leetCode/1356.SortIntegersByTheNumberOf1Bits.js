/**
 * @param {number[]} arr
 * @return {number[]}
 */

 const toBinary = (num) => {
  let binary = ''
  let rest = num

  while (rest > 0) {
    binary = `${(rest % 2)}${binary}`
    rest = parseInt(rest/2)
  }
  return binary
 }

const getCardinality = (binary) => binary.split('1').length - 1

const sortByCardinality = (a,b) => {
  const cardinality = a.cardinality - b.cardinality
  if (cardinality !== 0) return cardinality
  return a.value - b.value
}

const sortByBits = (arr) => {
  const cardinalities = arr.map(toBinary).map(getCardinality)
  const arrayWithCardinality = arr.map((value, index) => ({ value, cardinality: cardinalities[index]}))

  return arrayWithCardinality.sort(sortByCardinality).map(a => a.value)
}

const arr = [0,1,2,3,4,5,6,7,8]


console.log(sortByBits(arr))