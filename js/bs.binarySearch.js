// arr = [1, 2, 9, 78, 124]
// target = 9
// the return value should be 2

const bs = (array, target, start = undefined, end = undefined) => {
  if (start < 0 || end > array.length - 1) return undefined
  if (start === undefined) start = 0
  if (end === undefined) end = array.length - 1

  const center = parseInt((start + end) / 2)
  if (array[center] === target) return center

  if (array[center] < target) return bs(array, target, center + 1, end)
  return bs(array, target, start, center - 1)
}

const arr = [1, 2, 9, 78, 124]
const target = 78
console.log(bs(arr, target))