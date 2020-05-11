=begin
주어진 배열 arr에 n개의 정수 타입 숫자들이 정렬 되어 들어가 있다. 여기서 임의의 숫자 target가 그 배열의 몇 번 째에 있는지 반환하는 함수를 구현하라.

arr = [1, 2, 9, 78, 124]
target = 9

the return value should be 2

=end

require 'rspec/autorun'

def find_index(arr, target)
  return binary_search(0, arr, target)
end

def binary_search(index, arr, target)
  arr_size = arr.size
  center = arr_size / 2
  
  return center + index if arr[center] == target
  return binary_search(index + center, arr[center..], target) if arr[center-1] < target
  return binary_search(index, arr[0..center - 1], target)
end


RSpec.describe 'binary_search' do
  let (:arr) { [1, 2, 9, 78, 124] }
  let (:target) { 9 }
  it 'initialize' do
    expect(find_index(arr, 9)).to eq (2)
  end
  
  let (:arr1) { [1, 2, 9, 78, 124] }
  let (:target1) { 78 }
  it 'initialize' do
    expect(find_index(arr1, target1)).to eq (3)
  end
end
