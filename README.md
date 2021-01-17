
# 前言

**整理资料和实例，着实不容易，后续经常分享实用干货知识。希望各位路过的朋友点赞、关注、转发。**

**这是一个OpenCV-Python的入门教程，也可用作api速查表。OpenCV本身就是一款致力于开源免费的、实现跨平台计算机视觉和机器学习、标准化api的软件库，是从事图像领域不可跨过的一门必修课。最好的教程当时还是官方的api，但是考虑到科学上网、阅读外文的麻烦，还是把我自己19年整理的这些干货分享给大家。**

>这个教程的目标受众，针的读者是高校学生，科研工作者，图像处理爱好者。对于这些人群，他们往往是带着具体的问题，在苦苦寻找解决方案。为了一个小问题就让他们去学习 C++ 这么深奥的语言几乎是不可能的。而 Python 的悄然兴起给他们带来的希望，如果说 C++ 是 latex 的话，那 Python 的易用性相当于 word。他们可以很快的看懂本书的所有代码，并可以学着使用它们来解决自己的问题，同时也能拓展自己的视野。别人经常说 Python 不够快，但是对于上面的这些读者，我相信这不是问题，现在我们日常使用的PC 机已经无比强大了，而且绝大多数情况下不会用到实时处理，更不会在嵌入式设备上使用。因此这不是问题。

# 说明
因为链接中的段兄于2014年翻译的opencv3官方API(参见官方链接 2.中文版教程)是较老的版本并且使用的是PYTHON2，但是随着opencv源代码的不打断迭代，有些api已经不再是原来的接口和用法，鄙人不才，现与2019年末重新整理了一下相关的官方API。具体版本如下：

	opencv：3.4.2.16（高于此版本，例如新出的4.x版本，有些接口已经开始收费，所以默认为这是免费版本的最高稳定版了）
	python: 3.7

为了方便大家自行阅读和查找，我整理了：

- [Jupyter notebook版本](https://github.com/ztfmars/OpenCV_Python_Tutorial/blob/main/jupyter_version/opencv-python%20API%E6%95%B4%E7%90%86.ipynb)， 主要是详细说明api的各项含义/具体用法/基本演示example
- [py版本](https://github.com/ztfmars/OpenCV_Python_Tutorial/tree/main/py_examples)， 一些接口实例使用方法，可以马上跑起来
- html版本，主要是用于api速查

# 官方链接

- OpenCV官方教程：https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
- 中文版教程，注意是python2：
链接: https://pan.baidu.com/s/1brvNxngMSPvLk8fvzYjLKw 提取码: q587

# 如何安装opencv？

- [win10安装和常用使用方法总结](https://blog.csdn.net/weixin_42237113/article/details/104366282)

- [安装opencv不同版本的方法](https://blog.csdn.net/weixin_42237113/article/details/109165372)

# 关于后续

这些基本的api大家可以保留常用，我也给大家提供了jupyter, .py, .html的版本，方便大家后续使用，因为时间匆忙，难免有些纰漏，还望各位高手斧正。

当然如果你还是想要进一步学习**传统的图像处理**相关技术的话，我个人觉得还是需要把一些基础的理论知识补上，同时为了提高性能和长远发展的话C++还是避免不了，所以还是推荐大家一下基本书籍，以便于进一步精进：

- <数字图像处理（第三版）>
- <C++ Primer Plus>
- <OpenCV3编程入门 > -  毛星云编著(c++接口版本)

**tips:**
（1）如何结合<数字图像处理>和opencv相关知识点， 请结合博客（内附下载书籍pdf地址） -[【Python - OpenCV】图像和视频处理 - 基础理论知识梳理](https://blog.csdn.net/weixin_42237113/article/details/104500993)

（2）之后，**机器学习**入门的话，参见[一周高效入门机器学习](https://blog.csdn.net/weixin_42237113/article/details/104973498) , 另外强烈推荐

- <统计学习方法> - 李航，必看的理论知识入门
- <机器学习> - 周志华，全而广的涉猎工具书



（3）**深度学习，强化学习**的话, 推荐吴恩达老师的课程

（4）相关的资料链接和其他课程汇总的话，参见博客 - [最全面的AI学习路线和资源整理](https://blog.csdn.net/weixin_42237113/article/details/104456142)
