---
layout: default
title: Training deep physical neural networks with local physical information bottleneck
---

# Training deep physical neural networks with local physical information bottleneck
**arXiv**：[2602.09569v1](https://arxiv.org/abs/2602.09569) · [PDF](https://arxiv.org/pdf/2602.09569.pdf)  
**作者**：Hao Wang, Ziao Wang, Xiangpeng Liang, Han Zhao, Jianqi Hu, Junjie Jiang, Xing Fu, Jianshi Tang, Huaqiang Wu, Sylvain Gigan, Qiang Liu  

**一句话要点**：提出物理信息瓶颈框架，以通用高效训练深度物理神经网络，适应任意物理动力学。

**关键词**：物理神经网络, 信息瓶颈, 局部学习, 硬件适应性, 分布式训练, 光学计算

## 3 点简述
- 核心问题：深度物理神经网络缺乏通用训练方法，受限于物理复杂性和硬件约束。
- 方法要点：基于信息理论，分配矩阵式信息瓶颈至每个单元，实现局部学习，无需辅助数字模型。
- 实验或效果：在电子忆阻芯片和光学计算平台上验证监督、无监督和强化学习，适应硬件故障和分布式训练。

## 摘要（原文）

> Deep learning has revolutionized modern society but faces growing energy and latency constraints. Deep physical neural networks (PNNs) are interconnected computing systems that directly exploit analog dynamics for energy-efficient, ultrafast AI execution. Realizing this potential, however, requires universal training methods tailored to physical intricacies. Here, we present the Physical Information Bottleneck (PIB), a general and efficient framework that integrates information theory and local learning, enabling deep PNNs to learn under arbitrary physical dynamics. By allocating matrix-based information bottlenecks to each unit, we demonstrate supervised, unsupervised, and reinforcement learning across electronic memristive chips and optical computing platforms. PIB also adapts to severe hardware faults and allows for parallel training via geographically distributed resources. Bypassing auxiliary digital models and contrastive measurements, PIB recasts PNN training as an intrinsic, scalable information-theoretic process compatible with diverse physical substrates.

