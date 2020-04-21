#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric> 
#include <cmath>
//for accumulate(v.begin(),v.end(),0)

using namespace std;
int main()
{
int64_t n,t,i,j,k,l,flag,c,s,m,p,l1,r1;
//long n;
cin>>t;
while(t>0){
	    cin>>n;
	    cin>>l;
        int64_t a[n],b[l];
	    for(i=0;i<n;i++){
	        cin>>a[i];
	    }
	    sort(a,a+n);
		s=0;
	    for(i=1;i<l-1;i++){
			k=floor((a[n-1]-a[s]+1)/(l-1));
	    	p=a[s]+k;
	    	l1=s;
			r1=n-1;
	    	while(l1<r1){
	    		m=(l1+r1)/2;
	    		if(p<a[m]){
	    			r1=m-1;
	    		}
	    		else if(p>a[m]){
	    			l1=m+1;
	    		}
	    		else{
	    			break;
	    		}
	    	}
	    	c=m;
	    	j=abs(p-a[m]);
	    	if(m-1>=0){
	    		if(j>abs(p-a[m-1])){
	    			c=m-1;
	    		}
	    	}
	    	if(m+1<=n-1){
	    		if(j>abs(p-a[m+1])){
	    			c=m+1;
	    		}
	    	}
	    	// j=abs(a[0]-a[c]);
	    	// if(j<abs(a[n-1]-a[c])){
	    	// 	j=abs(a[n-1]-a[c]);
	    	// }
			b[i]=a[c];
			// cout<<"\n"<<a[c]<<"\n";
			s=c+1;
	    	//cout<<j<<"\n";
	    }
	    b[0]=a[0];
		b[l-1]=a[n-1];
		j=abs(b[0]-b[1]);
		// cout<<"\n";
		for(i=0;i<l-1;i++){
			// cout<<b[i]<<" ";
			if(j>abs(b[i]-b[i+1])){
	    		j=abs(b[i]-b[i+1]);
	    	}
		}
		// cout<<b[l-1]<<"\n";
		cout<<j<<"\n";
	     //vector<int64_t> v(a,a+n);
        t--;
	}
return 0;
}

