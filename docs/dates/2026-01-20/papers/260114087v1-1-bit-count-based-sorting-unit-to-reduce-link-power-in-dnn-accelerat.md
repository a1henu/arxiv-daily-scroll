---
layout: default
title: '1'-bit Count-based Sorting Unit to Reduce Link Power in DNN Accelerators
---

# '1'-bit Count-based Sorting Unit to Reduce Link Power in DNN Accelerators
**arXiv**：[2601.14087v1](https://arxiv.org/abs/2601.14087) · [PDF](https://arxiv.org/pdf/2601.14087.pdf)  
**作者**：Ruichi Han, Yizhi Chen, Tong Lei, Jordi Altayo Gonzalez, Ahmed Hemani  

**一句话要点**：提出基于'1'位计数的近似排序单元以减少DNN加速器中的链路功耗

**关键词**：DNN加速器, 链路功耗优化, 近似计算, 硬件排序单元, 卷积神经网络

## 3 点简述
- 核心问题：DNN加速器中互连功耗是瓶颈，数据排序可降低切换活动但硬件实现不足
- 方法要点：设计免比较排序单元，利用近似计算将人口计数分组为粗粒度桶以优化硬件面积
- 实验或效果：在CNN中实现，面积减少达35.4%，链路功耗降低19.50%，接近精确实现的20.42%

## 摘要（原文）

> Interconnect power consumption remains a bottleneck in Deep Neural Network (DNN) accelerators. While ordering data based on '1'-bit counts can mitigate this via reduced switching activity, practical hardware sorting implementations remain underexplored. This work proposes the hardware implementation of a comparison-free sorting unit optimized for Convolutional Neural Networks (CNN). By leveraging approximate computing to group population counts into coarse-grained buckets, our design achieves hardware area reductions while preserving the link power benefits of data reordering. Our approximate sorting unit achieves up to 35.4% area reduction while maintaining 19.50\% BT reduction compared to 20.42% of precise implementation.

