# include<stdio.h>
int second_largest(int arr[], int n){
    int largest = INT_MIN;
    int second_largest = INT_MIN;
    if(arr[n] =0){
        return 0;
    }
    for(int i=0; i<n; i++){
        if(i>largest){
            second_largest = largest;
            largest = i;
        }
        else if(i<largest && i>second_largest){
            second_largest = i;
        }
    }
    return second_largest;
    int main(){
        int arr[5] = {1,2,3,4,5};
        int result = second_largest(int arr[], int 5);
        printf("%d is the second largest in array.", result);
    }


}