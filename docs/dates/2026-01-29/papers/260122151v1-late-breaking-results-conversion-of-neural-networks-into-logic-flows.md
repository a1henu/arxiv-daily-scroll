---
layout: default
title: Late Breaking Results: Conversion of Neural Networks into Logic Flows for Edge Computing
---

# Late Breaking Results: Conversion of Neural Networks into Logic Flows for Edge Computing
**arXiv**：[2601.22151v1](https://arxiv.org/abs/2601.22151) · [PDF](https://arxiv.org/pdf/2601.22151.pdf)  
**作者**：Daniel Stein, Shaoyi Huang, Rolf Drechsler, Bing Li, Grace Li Zhang  

**一句话要点**：提出将神经网络转换为逻辑流的方法，以提升CPU在边缘计算中的推理效率。

**关键词**：边缘计算, 神经网络转换, 逻辑流, CPU优化, 决策树压缩

## 3 点简述
- 核心问题：CPU不擅长大规模MAC操作，而边缘设备常依赖CPU，导致神经网络执行效率低。
- 方法要点：将神经网络转换为决策树，再压缩为基于if-else结构的逻辑流，减少MAC操作。
- 实验或效果：在模拟RISC-V CPU上，延迟降低最高14.9%，且无精度损失。

## 摘要（原文）

> Neural networks have been successfully applied in various resource-constrained edge devices, where usually central processing units (CPUs) instead of graphics processing units exist due to limited power availability. State-of-the-art research still focuses on efficiently executing enormous numbers of multiply-accumulate (MAC) operations. However, CPUs themselves are not good at executing such mathematical operations on a large scale, since they are more suited to execute control flow logic, i.e., computer algorithms. To enhance the computation efficiency of neural networks on CPUs, in this paper, we propose to convert them into logic flows for execution. Specifically, neural networks are first converted into equivalent decision trees, from which decision paths with constant leaves are then selected and compressed into logic flows. Such logic flows consist of if and else structures and a reduced number of MAC operations. Experimental results demonstrate that the latency can be reduced by up to 14.9 % on a simulated RISC-V CPU without any accuracy degradation.
>   The code is open source at https://github.com/TUDa-HWAI/NN2Logic

