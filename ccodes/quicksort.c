#include <stdio.h>

#define MAX 10000

int partition(int* A,int p,int r){
	int pivot=A[r],i=p-1,j,tmp;
	for(j=p;j<r;j++){
		if(A[j]<pivot){
			i++;
			tmp=A[i];A[i]=A[j];A[j]=tmp;
		}
	}
	i++;
	A[r]=A[i];A[i]=pivot;
	return i;
}

int quicksort(int* A,int p,int r){
	if(p<r){
		int q=partition(A,p,r);
		quicksort(A,p,q-1);
		quicksort(A,q+1,r);
	}
}

int main(){
	int A[MAX];
	int n;
	scanf("%d",&n);
	int i=0,j=0;
	while(i<n){
		scanf("%d",&A[i++]);
	}
	printf("array:[");
	for(j=0;j<n-1;j++)
		printf("%d,",A[j]);
	printf("%d]\n",A[n-1]);
	
	quicksort(A,0,n-1);

	printf("sort:[");
	for(j=0;j<n-1;j++)
		printf("%d,",A[j]);
	printf("%d]\n",A[n-1]);
}
