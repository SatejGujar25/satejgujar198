#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector <int> nums = {100,50,20,10};
    int n = nums.size();
    vector <int> ans;
    for(int j = 0; j<n; j++){
        int max = j;
        for(int k = j+1; k<n; k++){
            if(nums[max] < nums[k]){
                max = k;
            }
        }
        if(nums[j] >= nums[max]){
            ans.push_back(nums[j]);
        }
    }
    
    for(int val: ans){
        cout << val << " ";
    }
    
    return 0;
}
