// Concept : Pushes the maximum to the last by adjacent swaps.
#include<stdio.h>
int main() {
    int arr[] = {13,46,24,52,20,9};
    int n = sizeof(arr)/sizeof(arr[0]);
    int i,j,swap;
    int flag=0; //will help in indicating if the array is sorted in the first iteration

    for(i=0; i<n; i++) {
        for(j=0; j<n-i-1; j++) {
            if(arr[j]>arr[j+1]) {
                swap = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = swap;
                flag=1;
            }
        }
        //if flag is 0 after first iteration, it indicates the array is already sorted, so we break & return
        if(flag==0) { printf("Array already sorted!\n"); break; } 
    }

    for(int i=0; i<n; i++) {
        printf("%d, ", arr[i]);
    }

    return 0;
}

//Complexity : Worst Case : O(n²), Best Case : O(n) [when already sorted, identified in 1st iteration]