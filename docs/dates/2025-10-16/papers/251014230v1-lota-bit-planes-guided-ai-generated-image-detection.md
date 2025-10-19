---
layout: default
title: LOTA: Bit-Planes Guided AI-Generated Image Detection
---

# LOTA: Bit-Planes Guided AI-Generated Image Detection
**arXiv**：[2510.14230v1](https://arxiv.org/abs/2510.14230) · [PDF](https://arxiv.org/pdf/2510.14230.pdf)  
**作者**：Hongsong Wang, Renxi Cheng, Yang Zhang, Chaolei Han, Jie Gui  

**一句话要点**：提出基于位平面引导的噪声提取方法以高效检测AI生成图像

**关键词**：AI生成图像检测, 位平面处理, 噪声提取, 梯度补丁选择, 轻量分类头

## 3 点简述
- 核心问题：现有方法计算成本高且难以捕捉原始图像中的固有噪声特征
- 方法要点：利用位平面处理提取噪声，设计最大梯度补丁选择以放大噪声信号
- 实验或效果：在GenImage基准上平均准确率达98.9%，检测速度提升近百倍

## 摘要（原文）

> The rapid advancement of GAN and Diffusion models makes it more difficult to
> distinguish AI-generated images from real ones. Recent studies often use
> image-based reconstruction errors as an important feature for determining
> whether an image is AI-generated. However, these approaches typically incur
> high computational costs and also fail to capture intrinsic noisy features
> present in the raw images. To solve these problems, we innovatively refine
> error extraction by using bit-plane-based image processing, as lower bit planes
> indeed represent noise patterns in images. We introduce an effective bit-planes
> guided noisy image generation and exploit various image normalization
> strategies, including scaling and thresholding. Then, to amplify the noise
> signal for easier AI-generated image detection, we design a maximum gradient
> patch selection that applies multi-directional gradients to compute the noise
> score and selects the region with the highest score. Finally, we propose a
> lightweight and effective classification head and explore two different
> structures: noise-based classifier and noise-guided classifier. Extensive
> experiments on the GenImage benchmark demonstrate the outstanding performance
> of our method, which achieves an average accuracy of \textbf{98.9\%}
> (\textbf{11.9}\%~$\uparrow$) and shows excellent cross-generator generalization
> capability. Particularly, our method achieves an accuracy of over 98.2\% from
> GAN to Diffusion and over 99.2\% from Diffusion to GAN. Moreover, it performs
> error extraction at the millisecond level, nearly a hundred times faster than
> existing methods. The code is at https://github.com/hongsong-wang/LOTA.

