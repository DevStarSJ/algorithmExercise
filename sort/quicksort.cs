using System;
using System.Collections.Generic;
using System.Linq;

namespace algorithm {
	class Program {

		public static IEnumerable<T> QuickSort<T>(IEnumerable<T> src) where T : IComparable
		{
			if (!src.Any())
				return src;

			T pivot = src.ElementAt(src.Count() / 2);

			var left = new List<T>();
			var right = new List<T>();
			var same = new List<T>();

			src.ToList().ForEach(x =>
			{
				int compareTo = x.CompareTo(pivot);
				if (compareTo < 0)
					left.Add(x);
				else if (compareTo > 0)
					right.Add(x);
				else
					same.Add(x);
			});

			return QuickSort(left).Concat(same).Concat(QuickSort(right));
		}

		static void Main(string[] args) {
			List<int> src = new List<int>() { 4, 7, 3, 2, 1, 9, 4, 7, 1, 2};
			var result = QuickSort(src);
			foreach (var e in result)
			{
				Console.Write($"{e}\t");
			}
			Console.WriteLine();

		}
	}
}
