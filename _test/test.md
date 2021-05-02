# Python数据结构与算法

## 程序运行时间检测

一般来说解决同样的问题，可能有不同的实现方式。我们总是希望一个程序可以快速高效并且节省资源的完成正确的工作， 而同样问题的不同实现方法就会有优劣之分。

例如我们可以用`Python`的`time`模块来检测不同的累计求和算法的效率

### 循环求和

```python
def sumOfN(n):
  start = time.time()
  theSum = 0
  for i in range(1, n + 1):
    theSum = theSum + i
    
  end = time.time()
  return theSum, end - start


for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN(10000))
```

```python
Sum id 50005000 required 0.001001 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.001001 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.000999 seconds
```

看上去耗时很短， 但是如果需要求和的数量级继续增加

```python
for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN(10000))

for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN(100000))

for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN(1000000))
```

```python
Sum id 50005000 required 0.000999 seconds
Sum id 50005000 required 0.001002 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.001001 seconds
Sum id 50005000 required 0.000000 seconds


Sum id 5000050000 required 0.004997 seconds
Sum id 5000050000 required 0.006002 seconds
Sum id 5000050000 required 0.005001 seconds
Sum id 5000050000 required 0.006001 seconds
Sum id 5000050000 required 0.007997 seconds



Sum id 500000500000 required 0.063554 seconds
Sum id 500000500000 required 0.053955 seconds
Sum id 500000500000 required 0.056039 seconds
Sum id 500000500000 required 0.057961 seconds
Sum id 500000500000 required 0.059000 seconds
```

### 无迭代求和

```python
def sumOfN2(n):
  start = time.time()
  theSum = (n * (n + 1)) / 2
  end = time.time()
  return theSum, end - start
```

这时候我们再看不同数量级下的结果

```python
for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN2(10000))

for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN2(100000))

for i in range(5):
  print("Sum id %d required %f seconds" 
        % sumOfN2(1000000))
```

```python
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 50005000 required 0.000000 seconds
Sum id 5000050000 required 0.000000 seconds
Sum id 5000050000 required 0.000000 seconds
Sum id 5000050000 required 0.000000 seconds
Sum id 5000050000 required 0.000000 seconds
Sum id 5000050000 required 0.000000 seconds
Sum id 500000500000 required 0.000000 seconds
Sum id 500000500000 required 0.000000 seconds
Sum id 500000500000 required 0.000000 seconds
Sum id 500000500000 required 0.000000 seconds
Sum id 500000500000 required 0.000000 seconds
```

可以发现无迭代算法的运行时间和输入的数的大小并没有关系。

### 大O表示法

#### 算法时间度量指标

一个算法所实施的操作数量或者步骤数可作为独立于程序的度量指标。

一个程序中，控制流语句起到组织语句的作用，而赋值语句包含了计算和存储。所以多用赋值语句座位衡量算法的指标。

在一段程序中，赋值语句越多，运行时间就越长。例如

```python
def sumOfN(n):
    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + 1
    return theSum
```

这个函数中的赋值语句的数量为`T(n) = 1 + n`, 也就是函数赋值语句的执行的次数。

#### 时间复杂度

我们通常用`时间复杂度`来描述执行一个算法所消耗的时间。一个通用的方法就是**大O表示法**

如果用动态的眼光来看待上述`T(n)`， 当n无限大时，常量1对整个函数运行时间的影响可以忽略不计， 这时候占主导部分的是`n`

所以上述函数的运行时间的数量级就是`O(n)`， 而无迭代算法本身和输入数据的大小无关，赋值语句是个常量，这种算法时间复杂度就是`O(1)`。

常见的大O数量级函数

![](https://gitee.com/limbo1996/picgo/raw/master/png/20210422201628.png)

例如

```python
a = 5
b = 6
c = 10

for i in range(n):
  for j in range(n):
    x = i * j
    y = j * j
    z = i * i
```

上述代码的赋值语句有T(n) = 3 + 3n^2^。时间复杂度为O(n^2^)。

## 线性结构

线性结构指的是一种有序数据项的集合。几种基本的线性结构：

* 栈
* 队列
* 双端队列

### 栈

栈是一系列对象组成的集合，数据项的加入和移除都在同一端，遵循**后进先出**的原则。

在Python中可以用`list`十分容易的实现一个栈

#### 实现

1. 将list的末端作为栈顶

   ```python
   class Stack:
     def __init__(self):
       self.items = []
       
     def isEmpty(self):
       return self.items == []
   
     def push(self, item):
       self.items.append(item)
       
     def pop(self):
       return self.items.pop()
   
     def peek(self):
       return self.items[len(self.items) - 1]
   
     def size(self):
       return len(self.items)
   ```

2. 将list的首端(index = 0)作为栈顶

   ```python
   class Stack_list_index_0:
     def __init__(self):
       self.items = []
       
     def isEmpty(self):
       return self.items == []
   
     def push(self, item):
       self.items.insert(0, item)
       
     def pop(self):
       return self.items.pop(0)
   
     def peek(self):
       return self.items[0]
   
     def size(self):
       return len(self.items)
   ```

   

这两种实现方法的时间复杂度是不同的， 第二种的`push`和`pop`的复杂度都是`O(n)`, 第一种都是`O(1)`

#### 简单应用

##### 简单的括号匹配

正确的括号匹配是我们日常写代码中用到的一个基础功能， 这个功能可以通过一个栈来简单实现

> 从左到右扫描所有括号，最先出现的左括号，应该匹配最后遇见的右括号

```python
def parChecker(symbolstring):
  s = Stack()
  balanced = True
  index = 0
  while index < len(symbolstring) and balanced:
    symbol = symbolstring[index]
    if symbol == "(":
      s.push(symbol)
    else:
      if s.isEmpty():
        balanced = False
      else:
        s.pop()
    index = index + 1
  if balanced and s.isEmpty():
    return True
  else:
    return False
```

当然在写代码的过程中不止`()`一种括号，只要将上面代码修改一下， 就可以匹配所有括号

##### 十进制转化为二进制

十进制转化为二进制，一般用**除以2求余数**的方法
![](https://gitee.com/limbo1996/picgo/raw/master/png/20210317203056.png)


