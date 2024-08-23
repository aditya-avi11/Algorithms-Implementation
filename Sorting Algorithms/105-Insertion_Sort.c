//Insertion Sort: "Builds the sorted array one element at a time by 
// repeatedly inserting elements into their correct position."

#include<stdio.h>
int main() {
    int arr[] = {13,46,24,52,20,9};
    int n = sizeof(arr)/sizeof(arr[0]);

    for(int i=0; i<=n; i++) {
        int j=i;
        //keep on checking with previous elements and swap if needed
        while(j>0 && arr[j-1]>arr[j]) {
            int swap = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = swap;
            j--;
        }
    }

    //Displaying the sorted array
    for(int i=0; i<n; i++) {
        printf("%d, ", arr[i]);
    }

    return 0;
}

//Complexity : Worst, Average Case : O(n²), Best Case : O(n) [when already sorted]