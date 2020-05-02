require 'rspec/autorun'

def get_overlapping_intervals(intervals)
  intervals = sort_by_first_element_asc(intervals)
  intervals = merge_intervals(intervals)
end

def sort_by_first_element_asc(intervals)
  intervals.sort_by {|interval| interval[0]}
end

def merge_intervals(intervals)
  result = []
  intervals.each { |interval| 
    result << interval if result.size == 0
    
    if interval[0] < result[-1][1]
      left = result.pop
      interval = [[interval[0], left[0]].min, [interval[1], left[1]].max]
    end
    
    result << interval
  }
  result
end

RSpec.describe [[1, 3], [5, 8], [4, 10], [20, 25]] do
  let(:intervals) { [[1, 3], [5, 8], [4, 10], [20, 25]] }
  let(:expected_sorted_intervals) { [[1, 3], [4, 10], [5, 8], [20, 25]] }
  let(:expected_mergerd_intervals) { [[1, 3], [4, 10], [20, 25]] }
  
  it 'sort_by_first_element_asc' do
    expect(sort_by_first_element_asc(intervals)).to eq(expected_sorted_intervals)
  end
  it 'Check Result' do
    expect(get_overlapping_intervals(intervals)).to eq(expected_mergerd_intervals)
  end
end

RSpec.describe [[1, 3], [2, 4], [3, 10], [20, 30], [10, 20]] do
  let(:intervals) { [[1, 3], [2, 4], [3, 10], [20, 30], [10, 20]] }
  let(:expected_sorted_intervals) { [[1, 3], [2, 4], [3, 10], [10, 20], [20, 30]] }
  let(:expected_mergerd_intervals) { [[1, 10], [10, 20], [20, 30]] }
  
  it 'sort_by_first_element_asc' do
    expect(sort_by_first_element_asc(intervals)).to eq(expected_sorted_intervals)
  end
  it 'Check Result' do
    expect(get_overlapping_intervals(intervals)).to eq(expected_mergerd_intervals)
  end
end
