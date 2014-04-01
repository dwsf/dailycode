#include <stdio.h>

#define MAX 10000

void insort(int *a,int n){
	int i,j,t;
	for(i=1;i<n;i++){
		t=a[i];
		for(j=i-1;j>=0;j--){
			if(a[j]>t)
				a[j+1]=a[j];
			else
				break;
		}
		a[++j]=t;
	}
}

void mergeL(){
	int i=0;
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
	
	insort(A,n);

	printf("sort:[");
	for(j=0;j<n-1;j++)
		printf("%d,",A[j]);
	printf("%d]\n",A[n-1]);
}
