require 'rspec/autorun'

class TreeNode
  attr_reader :value, :left, :right
  
  def initialize(value, left, right)
    @value = value
    @left = left
    @right = right
  end
  
  def minimum_path()      
    [ value ] + minimum_child_path
  end
  
  def minimum_path_and_sum()
    mp = minimum_path
    {
      path: mp,
      sum: mp.sum
    }
  end
  
  def minimum_child_path()
    lmp = left_minimum_path
    rmp = right_minimum_path
    
    return rmp if lmp.nil?
    return lmp if rmp.nil?
    return lmp.sum < rmp.sum ? lmp : rmp
  end
  
  def left_minimum_path()
    return nil if left.nil?
    
    left.is_a?(TreeNode) ? left.minimum_path : [ left ]
  end
  
  def right_minimum_path()
    return nil if right.nil?
    
    right.is_a?(TreeNode) ? right.minimum_path : [ right ]
  end
end


RSpec.describe TreeNode do
  let (:single_node) { TreeNode.new(1, 2, 3) }
  let (:simple_tree) { TreeNode.new(1, 2, single_node) }
  let (:simple_tree2) { TreeNode.new(1, 7, single_node) }

  it 'initialize' do
    expect(single_node.value).to eq (1)
    expect(single_node.left).to eq (2)
    expect(single_node.right).to eq (3)
    expect(simple_tree.right.value).to eq (single_node.value)
  end
  
  it 'minimum_path' do
    expect(single_node.minimum_path_and_sum[:sum]).to eq (3)
    expect(single_node.minimum_path_and_sum[:sum]).to eq (3)
    expect(simple_tree2.minimum_path_and_sum[:path]).to eq ([1,1,2])
    expect(simple_tree2.minimum_path_and_sum[:sum]).to eq (4)
  end
  
  let (:t1) { TreeNode.new(10, TreeNode.new(5, nil, 2), TreeNode.new(5, nil, TreeNode.new(1, -1, nil))) }
  
  it 'minimum_path' do
    expect(t1.minimum_path_and_sum[:sum]).to eq (15)
    expect(t1.minimum_path_and_sum[:path]).to eq ([10, 5, 1, -1])
  end
end
