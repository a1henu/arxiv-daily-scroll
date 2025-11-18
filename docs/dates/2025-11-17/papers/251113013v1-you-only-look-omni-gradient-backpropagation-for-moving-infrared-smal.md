---
layout: default
title: You Only Look Omni Gradient Backpropagation for Moving Infrared Small Target Detection
---

# You Only Look Omni Gradient Backpropagation for Moving Infrared Small Target Detection
**arXiv**：[2511.13013v1](https://arxiv.org/abs/2511.13013) · [PDF](https://arxiv.org/pdf/2511.13013.pdf)  
**作者**：Guoyi Zhang, Guangsheng Xu, Siyang Chen, Han Wang, Xiaohu Zhang  

**一句话要点**：提出BP-FPN以解决移动红外小目标检测中的特征表示瓶颈问题

**关键词**：红外小目标检测, 特征金字塔网络, 梯度反向传播, 特征一致性, 目标-背景不平衡

## 3 点简述
- 核心问题：移动红外小目标检测因低信噪比和目标-背景不平衡导致特征表示模糊
- 方法要点：引入梯度隔离低层捷径和方向梯度正则化，提升特征学习效率
- 实验或效果：在多个公共数据集上实现新的最先进性能，计算开销可忽略

## 摘要（原文）

> Moving infrared small target detection is a key component of infrared search and tracking systems, yet it remains extremely challenging due to low signal-to-clutter ratios, severe target-background imbalance, and weak discriminative features. Existing deep learning methods primarily focus on spatio-temporal feature aggregation, but their gains are limited, revealing that the fundamental bottleneck lies in ambiguous per-frame feature representations rather than spatio-temporal modeling itself. Motivated by this insight, we propose BP-FPN, a backpropagation-driven feature pyramid architecture that fundamentally rethinks feature learning for small target. BP-FPN introduces Gradient-Isolated Low-Level Shortcut (GILS) to efficiently incorporate fine-grained target details without inducing shortcut learning, and Directional Gradient Regularization (DGR) to enforce hierarchical feature consistency during backpropagation. The design is theoretically grounded, introduces negligible computational overhead, and can be seamlessly integrated into existing frameworks. Extensive experiments on multiple public datasets show that BP-FPN consistently establishes new state-of-the-art performance. To the best of our knowledge, it is the first FPN designed for this task entirely from the backpropagation perspective.

