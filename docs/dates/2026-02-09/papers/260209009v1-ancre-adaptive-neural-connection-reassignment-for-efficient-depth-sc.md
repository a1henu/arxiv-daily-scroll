---
layout: default
title: ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling
---

# ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling
**arXiv**：[2602.09009v1](https://arxiv.org/abs/2602.09009) · [PDF](https://arxiv.org/pdf/2602.09009.pdf)  
**作者**：Yilang Zhang, Bingcong Li, Niao He, Georgios B. Giannakis  

**一句话要点**：提出自适应神经连接重分配框架以优化深度网络收敛与效率

**关键词**：残差连接优化, 深度网络收敛, 自适应学习, 计算效率, 模型预训练

## 3 点简述
- 核心问题：深度网络残差连接布局影响收敛，导致层利用不足
- 方法要点：参数化学习残差连接性，自适应重分配连接，计算开销低
- 实验或效果：在大型语言模型、扩散模型和ResNet中加速收敛并提升性能

## 摘要（原文）

> Scaling network depth has been a central driver behind the success of modern foundation models, yet recent investigations suggest that deep layers are often underutilized. This paper revisits the default mechanism for deepening neural networks, namely residual connections, from an optimization perspective. Rigorous analysis proves that the layout of residual connections can fundamentally shape convergence behavior, and even induces an exponential gap in convergence rates. Prompted by this insight, we introduce adaptive neural connection reassignment (ANCRe), a principled and lightweight framework that parameterizes and learns residual connectivities from the data. ANCRe adaptively reassigns residual connections with negligible computational and memory overhead ($<1\%$), while enabling more effective utilization of network depth. Extensive numerical tests across pre-training of large language models, diffusion models, and deep ResNets demonstrate consistently accelerated convergence, boosted performance, and enhanced depth efficiency over conventional residual connections.

