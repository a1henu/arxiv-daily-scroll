---
layout: default
title: MSP-ReID: Hairstyle-Robust Cloth-Changing Person Re-Identification
---

# MSP-ReID: Hairstyle-Robust Cloth-Changing Person Re-Identification
**arXiv**：[2603.01640v1](https://arxiv.org/abs/2603.01640) · [PDF](https://arxiv.org/pdf/2603.01640.pdf)  
**作者**：Xiangyang He, Lin Wan  

**一句话要点**：提出MSP框架以解决换装行人重识别中发型变化导致的性能下降问题

**关键词**：换装行人重识别, 发型鲁棒性, 数据增强, 注意力机制, 结构保留

## 3 点简述
- 核心问题：现有方法整体处理头部，过度依赖易变的发型线索，在发型变化时性能下降
- 方法要点：引入发型导向增强、衣物保留随机擦除和基于区域解析注意力，减少发型依赖并保留结构信息
- 实验或效果：在多个CC-ReID基准测试中达到最先进性能，提供鲁棒解决方案

## 摘要（原文）

> Cloth-Changing Person Re-Identification (CC-ReID) aims to match the same individual across cameras under varying clothing conditions. Existing approaches often remove apparel and focus on the head region to reduce clothing bias. However, treating the head holistically without distinguishing between face and hair leads to over-reliance on volatile hairstyle cues, causing performance degradation under hairstyle changes. To address this issue, we propose the Mitigating Hairstyle Distraction and Structural Preservation (MSP) framework. Specifically, MSP introduces Hairstyle-Oriented Augmentation (HSOA), which generates intra-identity hairstyle diversity to reduce hairstyle dependence and enhance attention to stable facial and body cues. To prevent the loss of structural information, we design Cloth-Preserved Random Erasing (CPRE), which performs ratio-controlled erasing within clothing regions to suppress texture bias while retaining body shape and context. Furthermore, we employ Region-based Parsing Attention (RPA) to incorporate parsing-guided priors that highlight face and limb regions while suppressing hair features. Extensive experiments on multiple CC-ReID benchmarks demonstrate that MSP achieves state-of-the-art performance, providing a robust and practical solution for long-term person re-identification.

