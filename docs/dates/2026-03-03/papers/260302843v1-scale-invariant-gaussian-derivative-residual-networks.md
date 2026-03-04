---
layout: default
title: Scale-invariant Gaussian derivative residual networks
---

# Scale-invariant Gaussian derivative residual networks
**arXiv**：[2603.02843v1](https://arxiv.org/abs/2603.02843) · [PDF](https://arxiv.org/pdf/2603.02843.pdf)  
**作者**：Andrzej Perzanowski, Tony Lindeberg  

**一句话要点**：提出高斯导数残差网络以解决深度网络跨尺度泛化问题

**关键词**：尺度不变性, 高斯导数网络, 残差连接, 深度可分离卷积, 跨尺度泛化, 分布外问题

## 3 点简述
- 核心问题：深度网络在处理训练未见尺度图像时泛化能力差，即分布外问题。
- 方法要点：构建尺度协变高斯导数残差块，通过残差连接提升深度网络精度，同时保持尺度不变性。
- 实验或效果：在STL-10、Fashion-MNIST和CIFAR-10重缩放数据集上验证了强尺度泛化和选择能力。

## 摘要（原文）

> Generalisation across image scales remains a fundamental challenge for deep networks, which often fail to handle images at scales not seen during training (the out-of-distribution problem). In this paper, we present provably scale-invariant Gaussian derivative residual networks (GaussDerResNets), constructed out of scale-covariant Gaussian derivative residual blocks coupled in cascade, aimed at addressing this problem.
>   By adding residual skip connections to the previous notion of Gaussian derivative layers, deeper networks with substantially increased accuracy can be constructed, while preserving very good scale generalisation properties at the higher level of accuracy. Explicit proofs are provided regarding the underlying scale-covariant and scale-invariant properties in arbitrary dimensions.
>   To analyse the ability of GaussDerResNets to generalise to new scales, we apply them on the new rescaled version of the STL-10 dataset, where training is done at a single fixed scale and evaluation is performed on multiple copies of the test set, each rescaled to a single distinct spatial scale, with scale factors extending over a range of 4. We also conduct similar systematic experiments on the rescaled versions of Fashion-MNIST and CIFAR-10 datasets.
>   Experimentally, we demonstrate that the GaussDerResNets have strong scale generalisation and scale selection properties on all the three rescaled datasets. In our ablation studies, we investigate different architectural variants of GaussDerResNets, demonstrating that basing the architecture on depthwise-separable convolutions allows for decreasing both the number of parameters and the amount of computations, with reasonably maintained accuracy and scale generalisation.

