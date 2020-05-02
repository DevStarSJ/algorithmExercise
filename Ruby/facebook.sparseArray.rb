require 'rspec/autorun'

class SparseArray
  def initialize(arr, size)
    raise 'SizeOfInitialArrayIsGreaterThanSize' if arr.size > size
   
    @size = size
    @values = {}
    extract_values(arr)
  end
    
  def set(i, val)
    raise 'OutOfIndexRange' if i >= @size
    @values[i] = val unless val == 0
    self
  end
  
  def get(i)
    raise 'OutOfIndexRange' if i >= @size
    @values[i] || 0
  end
  
  def values()
    @values
  end
  
  private
  
  def extract_values(arr)
    arr.each_with_index { |value, i| 
      @values[i] = value unless value == 0
    }
  end
end

RSpec.describe SparseArray do
  let (:initialize_error) { SparseArray.new([1,2,3], 2) }
  let (:initial_array) { [1,2,0,6,7] }
  let (:initial_values_without_zero) { 
    { 
      0 => 1,
      1 => 2,
      3 => 6,
      4 => 7
    }
  }
  
  let (:sa) { SparseArray.new(initial_array, 10) }

  it 'error case' do
    expect { initialize_error }.to \
      raise_error('SizeOfInitialArrayIsGreaterThanSize')
  end
  
  it 'normal case' do
    expect(sa.values).to eq(initial_values_without_zero)
    
    expect(sa.set(7, 10000).get(7)).to eq(10000)
    
    expect { sa.set(10, 1) }.to raise_error('OutOfIndexRange')
    expect { sa.get(10) }.to raise_error('OutOfIndexRange')
  end
end
