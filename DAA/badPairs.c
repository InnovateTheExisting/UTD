/* C program for Merge Sort */
#include<stdlib.h>
#include<stdio.h>
int count=0;

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
	int i, j, k;
	int n1 = m - l + 1;
	int n2 = r - m;

	/* create temp arrays */
	int L[n1], R[n2];

	/* Copy data to temp arrays L[] and R[] */
	//printf("L[i]");
	for (i = 0; i < n1; i++){
		L[i] = arr[l + i];
		//printf("%d ",L[i]);
	}
	//printf("\n");
	//printf("R[j]");
	for (j = 0; j < n2; j++){
		R[j] = arr[m + 1+ j];
		//printf("%d ",R[j]);
	}

	/* Merge the temp arrays back into arr[l..r]*/
	i = 0; // Initial index of first subarray
	j = 0; // Initial index of second subarray
	k = l; // Initial index of merged subarray
	while (i < n1 && j < n2)
	{
		if (L[i] > R[j]+10)	count++;
		if(j+1<n2){j++;}
		else if(j+1==n2){j=0;i++;}

	}

	/* Copy the remaining elements of L[], if there
	are any
	while (i < n1)
	{
		arr[k] = L[i];
		i++;
		k++;
	}

	/* Copy the remaining elements of R[], if there
	are any
	while (j < n2)
	{
		arr[k] = R[j];
		j++;
		k++;
	} */
}

/* l is for left index and r is right index of the
sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
	if (l < r)
	{
		// Same as (l+r)/2, but avoids overflow for
		// large l and h
		int m = l+(r-l)/2;

		// Sort first and second halves
		mergeSort(arr, l, m);
		mergeSort(arr, m+1, r);

		merge(arr, l, m, r);
	}
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray()
{
		printf("%d",count);
	printf("\n");
}

/* Driver program to test above functions */
int main()
{
	int arr[] = {90,80,30,50,20,10,60,40,70};
	int arr_size = sizeof(arr)/sizeof(arr[0]);

	printf("Bad Pairs: ");
	//printArray();

	mergeSort(arr, 0, arr_size - 1);

	printArray();
	return 0;
}
