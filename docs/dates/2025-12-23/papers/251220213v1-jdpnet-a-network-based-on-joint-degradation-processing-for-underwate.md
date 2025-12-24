---
layout: default
title: JDPNet: A Network Based on Joint Degradation Processing for Underwater Image Enhancement
---

# JDPNet: A Network Based on Joint Degradation Processing for Underwater Image Enhancement
**arXiv**：[2512.20213v1](https://arxiv.org/abs/2512.20213) · [PDF](https://arxiv.org/pdf/2512.20213.pdf)  
**作者**：Tao Ye, Hongbin Ren, Chongbing Zhang, Haoran Chen, Xiaosong Li  

**一句话要点**：提出JDPNet以解决水下图像中非线性耦合退化的增强问题

**关键词**：水下图像增强, 退化耦合处理, 联合特征挖掘, AquaBalanceLoss, 深度学习网络

## 3 点简述
- 核心问题：水下图像退化呈现非线性耦合，现有方法难以有效处理耦合信息
- 方法要点：引入联合特征挖掘模块和概率引导分布策略，统一调整耦合退化特征
- 实验或效果：在多个数据集上实现先进性能，平衡性能、参数和计算成本

## 摘要（原文）

> Given the complexity of underwater environments and the variability of water as a medium, underwater images are inevitably subject to various types of degradation. The degradations present nonlinear coupling rather than simple superposition, which renders the effective processing of such coupled degradations particularly challenging. Most existing methods focus on designing specific branches, modules, or strategies for specific degradations, with little attention paid to the potential information embedded in their coupling. Consequently, they struggle to effectively capture and process the nonlinear interactions of multiple degradations from a bottom-up perspective. To address this issue, we propose JDPNet, a joint degradation processing network, that mines and unifies the potential information inherent in coupled degradations within a unified framework. Specifically, we introduce a joint feature-mining module, along with a probabilistic bootstrap distribution strategy, to facilitate effective mining and unified adjustment of coupled degradation features. Furthermore, to balance color, clarity, and contrast, we design a novel AquaBalanceLoss to guide the network in learning from multiple coupled degradation losses. Experiments on six publicly available underwater datasets, as well as two new datasets constructed in this study, show that JDPNet exhibits state-of-the-art performance while offering a better tradeoff between performance, parameter size, and computational cost.

