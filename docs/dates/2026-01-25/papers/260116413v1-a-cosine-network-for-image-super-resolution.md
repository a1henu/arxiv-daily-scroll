---
layout: default
title: A Cosine Network for Image Super-Resolution
---

# A Cosine Network for Image Super-Resolution
**arXiv**：[2601.16413v1](https://arxiv.org/abs/2601.16413) · [PDF](https://arxiv.org/pdf/2601.16413.pdf)  
**作者**：Chunwei Tian, Chengyuan Zhang, Bob Zhang, Zhiwu Li, C. L. Philip Chen, David Zhang  

**一句话要点**：提出余弦网络CSRNet以改进图像超分辨率，通过异构块和余弦退火优化训练。

**关键词**：图像超分辨率, 卷积神经网络, 异构块设计, 余弦退火, 结构信息提取

## 3 点简述
- 核心问题：图像超分辨率中需有效保留结构信息，避免同源信息不足。
- 方法要点：设计奇偶异构块提取互补结构信息，结合线性与非线性信息增强鲁棒性。
- 实验或效果：CSRNet在图像超分辨率任务中与先进方法竞争，实验验证其性能。

## 摘要（原文）

> Deep convolutional neural networks can use hierarchical information to progressively extract structural information to recover high-quality images. However, preserving the effectiveness of the obtained structural information is important in image super-resolution. In this paper, we propose a cosine network for image super-resolution (CSRNet) by improving a network architecture and optimizing the training strategy. To extract complementary homologous structural information, odd and even heterogeneous blocks are designed to enlarge the architectural differences and improve the performance of image super-resolution. Combining linear and non-linear structural information can overcome the drawback of homologous information and enhance the robustness of the obtained structural information in image super-resolution. Taking into account the local minimum of gradient descent, a cosine annealing mechanism is used to optimize the training procedure by performing warm restarts and adjusting the learning rate. Experimental results illustrate that the proposed CSRNet is competitive with state-of-the-art methods in image super-resolution.

