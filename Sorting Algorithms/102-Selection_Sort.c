//Concept : Find minimum and plcae it in the begining
#include<stdio.h>
int main() {
    int arr[] = {13,46,24,52,20,9};
    int n = sizeof(arr)/sizeof(arr[0]);
    int min, swap;

    for(int i=0; i<n-1; i++) {
        min = i;
        for(int j=i+1; j<n; j++) {
            if(arr[j]<arr[min]) {
                min = j;
            }
        }
        swap = arr[min];
        arr[min] = arr[i];
        arr[i] = swap;
    }

    //Displaying the sorted array
    for(int i=0; i<n; i++) {
        printf("%d, ", arr[i]);
    }

    return 0;
}

//Complexity : Worst, Best, Average Case : O(n²)
//Better than Bubble Sort since Swaps are Linear in this while Bubble Sort has Quadratic swaps.