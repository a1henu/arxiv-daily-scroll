---
layout: default
title: The Weight of a Bit: EMFI Sensitivity Analysis of Embedded Deep Learning Models
---

# The Weight of a Bit: EMFI Sensitivity Analysis of Embedded Deep Learning Models
**arXiv**：[2602.16309v1](https://arxiv.org/abs/2602.16309) · [PDF](https://arxiv.org/pdf/2602.16309.pdf)  
**作者**：Jakub Breier, Štefan Kučerák, Xiaolu Hou  

**一句话要点**：评估嵌入式深度学习模型参数表示对电磁故障注入攻击的敏感性

**关键词**：电磁故障注入, 嵌入式神经网络, 数值表示, 模型鲁棒性, 图像分类

## 3 点简述
- 核心问题：缺乏不同数值表示对嵌入式神经网络模型电磁故障注入攻击影响的全面研究
- 方法要点：比较32位和16位浮点与8位和4位整数表示在攻击下的模型表现
- 实验或效果：浮点表示在单次攻击后精度大幅下降，整数表示尤其是8位在VGG-11上保持较高准确率

## 摘要（原文）

> Fault injection attacks on embedded neural network models have been shown as a potent threat. Numerous works studied resilience of models from various points of view. As of now, there is no comprehensive study that would evaluate the influence of number representations used for model parameters against electromagnetic fault injection (EMFI) attacks.
>   In this paper, we investigate how four different number representations influence the success of an EMFI attack on embedded neural network models. We chose two common floating-point representations (32-bit, and 16-bit), and two integer representations (8-bit, and 4-bit). We deployed four common image classifiers, ResNet-18, ResNet-34, ResNet-50, and VGG-11, on an embedded memory chip, and utilized a low-cost EMFI platform to trigger faults. Our results show that while floating-point representations exhibit almost a complete degradation in accuracy (Top-1 and Top-5) after a single fault injection, integer representations offer better resistance overall. Especially, when considering the the 8-bit representation on a relatively large network (VGG-11), the Top-1 accuracies stay at around 70% and the Top-5 at around 90%.

