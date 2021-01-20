class TreeNode {
  constructor(value) {
    this.value = value
    this.left = undefined
    this.right = undefined
    this.parent = undefined
  }

  append(node) {
    if (node.parent != undefined) throw 'E3'
    if (this.left != undefined && this.right != undefined) throw 'E1'
    if (this.left === undefined) {
      this.left = node
    } else if (this.right === undefined) {
      if (this.left.value < node.value) {
        this.right = node
      } else {
        this.right = this.left
        this.left = node
      }
    }
    node.parent = this
  }

  toExpression() {
    const left = this.left == undefined ? '' : `(${this.left.toExpression()})`
    const right = this.right == undefined ? '' : `(${this.right.toExpression()})`
    return `${this.value}${left}${right}`
  }
}

const nodes = [['A','B'], ['A','C'], ['B','G'], ['C','H'], ['E','F'], ['B','D'], ['C','E']]

const nodeComparer = (left, right) => {
  if (left[0] < right[0]) return -1
  if (left[0] > right[0]) return 1
  if (left[1] < right[1]) return -1
  if (left[1] > right[1]) return 1
  throw 'E2'
}

const isThisATree = (nodes) => {
  try {
    nodes.sort(nodeComparer)
    console.log(nodes)

    let treeNodes = []

    const findTreeNode = (value) => {
      for (let i = 0; i < treeNodes.length; i++) {
        if (treeNodes[i].value == value) return treeNodes[i]
      }
      const newNode = new TreeNode(value)
      treeNodes.push(newNode)
      return newNode
    }

    for (let i = 0; i < nodes.length; i++) {
      const node = nodes[i]
      const parent = findTreeNode(node[0])
      const child = findTreeNode(node[1])
      parent.append(child)
      console.log(i, node, treeNodes.length)
    }

    const roots = treeNodes.filter(a => a.parent === undefined)
    if (roots.length > 1) throw 'E4'
    const root = roots[0]

    return `(${root.toExpression()})`
    
  
  } catch (e) {
    return e
  }
}

console.log(isThisATree(nodes))