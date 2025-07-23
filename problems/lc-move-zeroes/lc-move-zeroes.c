void moveZeroes(int* nums, int numsSize) {
    int c=0,i;
    int d=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]!=0)
            nums[c++]=nums[i];
        else
            d++;
    }
    for(i=0;i<d;i++){
        nums[c++]=0;
    }
}