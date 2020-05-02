const expect = require('chai').expect

class SparseArray {
  constructor(arr, size) {
    if (arr.length > size)
      throw new Error('SizeOfInitialArrayIsGreaterThanSize')
    this.size = size
    this.values = this.getValuesMap(arr)
  }

  getValuesMap(arr) {
    let values = {}
    arr.forEach((value, i) => {
      if (value === 0) return
      values[i] = value
    })
    return values
  }

  set(i, val) {
    if (i >= this.size) throw new Error('IndexOutOfRange')
    this.values[i] = val
  }

  get(i) {
    if (i >= this.size) throw new Error('IndexOutOfRange')
    return this.values[i] || 0
  }
}

const s = new SparseArray([1, 2, 0, 3], 10)

console.log(s.values)

expect(s.get(5) === 0).to.be.true
expect(s.get(2) === 0).to.be.true

s.set(9, 10000)
expect(s.get(9) === 10000)

function expectException(func, message) {
  try {
    func()
  } catch (error) {
    expect(error.message === message).to.be.true
  }
}

expectException(
  () => new SparseArray([1, 2, 0, 3], 2),
  'SizeOfInitialArrayIsGreaterThanSize'
)
expectException(() => s.get(11), 'IndexOutOfRange')
