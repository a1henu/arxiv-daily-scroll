---
layout: default
title: Timely Parameter Updating in Over-the-Air Federated Learning
---

# Timely Parameter Updating in Over-the-Air Federated Learning
**arXiv**：[2512.19103v1](https://arxiv.org/abs/2512.19103) · [PDF](https://arxiv.org/pdf/2512.19103.pdf)  
**作者**：Jiaqi Zhu, Zhongyuan Zhao, Xiao Li, Ruihao Du, Shi Jin, Howard H. Yang  

**一句话要点**：提出FAIR-k算法以解决空中联邦学习中正交波形不足与高维模型不匹配的问题

**关键词**：空中联邦学习, 梯度选择算法, 参数更新及时性, 通信效率优化, 数据异构性建模

## 3 点简述
- 核心问题：空中联邦学习中正交波形数量有限，无法匹配深度学习模型的高维度梯度传输
- 方法要点：FAIR-k结合轮询和Top-k算法，平衡参数更新的及时性和重要性，选择关键梯度子集
- 实验或效果：分析显示FAIR-k加速收敛并提升通信效率，支持更长的本地训练周期

## 摘要（原文）

> Incorporating over-the-air computations (OAC) into the model training process of federated learning (FL) is an effective approach to alleviating the communication bottleneck in FL systems. Under OAC-FL, every client modulates its intermediate parameters, such as gradient, onto the same set of orthogonal waveforms and simultaneously transmits the radio signal to the edge server. By exploiting the superposition property of multiple-access channels, the edge server can obtain an automatically aggregated global gradient from the received signal. However, the limited number of orthogonal waveforms available in practical systems is fundamentally mismatched with the high dimensionality of modern deep learning models. To address this issue, we propose Freshness Freshness-mAgnItude awaRe top-k (FAIR-k), an algorithm that selects, in each communication round, the most impactful subset of gradients to be updated over the air. In essence, FAIR-k combines the complementary strengths of the Round-Robin and Top-k algorithms, striking a delicate balance between timeliness (freshness of parameter updates) and importance (gradient magnitude). Leveraging tools from Markov analysis, we characterize the distribution of parameter staleness under FAIR-k. Building on this, we establish the convergence rate of OAC-FL with FAIR-k, which discloses the joint effect of data heterogeneity, channel noise, and parameter staleness on the training efficiency. Notably, as opposed to conventional analyses that assume a universal Lipschitz constant across all the clients, our framework adopts a finer-grained model of the data heterogeneity. The analysis demonstrates that since FAIR-k promotes fresh (and fair) parameter updates, it not only accelerates convergence but also enhances communication efficiency by enabling an extended period of local training without significantly affecting overall training efficiency.

