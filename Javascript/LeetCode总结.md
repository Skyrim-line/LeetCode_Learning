# [3146. 两个字符串的排列差](https://leetcode.cn/problems/permutation-difference-between-two-strings/)

思路：

hash表存储s中每个字母的index，第二个表计算s和t对应的index绝对值



# [2908. 元素和最小的山形三元组 I](https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/)

思路：

### 方法1： 枚举

三层for循环最内层直接计算result，此方法方便理解便于快速解题；第一层循环代表遍历整个数组，第二层是机遇当前位置往后遍历，第三次类似，在最能层计算result，逐渐更新result的值直到第一层循环结束则返回最小的result.

### 方法2: 左右遍历数组

初始化一个result=MAX，和一个right_min数组长度和nums一样，内容全部fill为MAX

```js
let result=MAX;
const right_min=new Array(num.length).fill(MAX);
```

从右边倒数第二个值开始向左边遍历，遇到比right小的更新right_min[i]的值；从左边第二个值向右边遍历，遇到`left<nums[i]`则更新result，否则更新left指针为当前 nums[i]	

```js
let right=nums[n-2];
for...{
	if (right<nums[i]){
		right_min[i]=right;
	}
	else{ right=nums[i]; } 
}
//update left-min
let left=nums[0];
for...{
	if(left<nums[i]){
		result=Math.min(result,left+nums[i]+right_min[i]);
	}
	else{
		left=nums[i];
	}
}
return result<MAX? result : -1;// 如果小于MAX返回result否则返回-1
```

