package practproj1;

public class mergeSort {
	public static void main(String[] args) {
		int[] arr={22,21,19,18,15,14,9,7,5};
        sort(arr);
        
        for(int x:arr) {
        	System.out.printf("%d, ", x);
        }
		
	}
	
	public static void sort(int[] arr) {
		if(arr.length < 2)
			return;
		
		int mid = arr.length/2;
		int[] left = new int[mid];
		int[] right = new int[arr.length - mid];
		
		for(int i=0; i<mid; i++) {
			left[i] = arr[i];
		}
		
		for(int i=mid; i<arr.length; i++) {
			right[i-mid] = arr[i];
		}
		
		sort(left);
		sort(right);
		merge(left, right, arr);
	}
	
	public static void merge(int[] left, int[] right, int[] array) {
		int leftSize = left.length;
		int rightSize = right.length;
		int i = 0, j = 0, k = 0;
		
		while(i<leftSize & j<rightSize) {
			if(left[i] <= right[j]) {
				array[k] = left[i];
				i++;
				k++;
			}else{
				array[k] = right[j];
				j++;
				k++;
			}
		}
		 while (i < leftSize) {
	            array[k] = left[i];
	            k++;
	            i++;
	        }
	        while (j < leftSize) {
	            array[k] = right[j];
	            k++;
	            j++;
	        }
		
	}
}
