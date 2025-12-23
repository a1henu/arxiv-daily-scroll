---
layout: default
title: Efficient Spike-driven Transformer for High-performance Drone-View Geo-Localization
---

# Efficient Spike-driven Transformer for High-performance Drone-View Geo-Localization
**arXiv**：[2512.19365v1](https://arxiv.org/abs/2512.19365) · [PDF](https://arxiv.org/pdf/2512.19365.pdf)  
**作者**：Zhongwei Chen, Hai-Jun Rong, Zhao-Xu Yang, Guoqi Li  

**一句话要点**：提出SpikeViMFormer以解决无人机视角地理定位中脉冲神经网络的信息损失和长程依赖学习问题

**关键词**：无人机视角地理定位, 脉冲神经网络, Transformer, 选择性注意力, 状态空间模型, 轻量级推理

## 3 点简述
- 传统人工神经网络方法功耗高，脉冲神经网络在无人机视角地理定位中潜力未充分探索，面临信息损失和长程依赖学习困难
- 采用轻量级脉冲驱动Transformer骨干，设计SSA块选择性增强特征，引入SHS块学习长程依赖，推理阶段仅用骨干以降低计算成本
- 实验表明SpikeViMFormer优于现有脉冲神经网络，与先进人工神经网络性能相当，代码已开源

## 摘要（原文）

> Traditional drone-view geo-localization (DVGL) methods based on artificial neural networks (ANNs) have achieved remarkable performance. However, ANNs rely on dense computation, which results in high power consumption. In contrast, spiking neural networks (SNNs), which benefit from spike-driven computation, inherently provide low power consumption. Regrettably, the potential of SNNs for DVGL has yet to be thoroughly investigated. Meanwhile, the inherent sparsity of spike-driven computation for representation learning scenarios also results in loss of critical information and difficulties in learning long-range dependencies when aligning heterogeneous visual data sources. To address these, we propose SpikeViMFormer, the first SNN framework designed for DVGL. In this framework, a lightweight spike-driven transformer backbone is adopted to extract coarse-grained features. To mitigate the loss of critical information, the spike-driven selective attention (SSA) block is designed, which uses a spike-driven gating mechanism to achieve selective feature enhancement and highlight discriminative regions. Furthermore, a spike-driven hybrid state space (SHS) block is introduced to learn long-range dependencies using a hybrid state space. Moreover, only the backbone is utilized during the inference stage to reduce computational cost. To ensure backbone effectiveness, a novel hierarchical re-ranking alignment learning (HRAL) strategy is proposed. It refines features via neighborhood re-ranking and maintains cross-batch consistency to directly optimize the backbone. Experimental results demonstrate that SpikeViMFormer outperforms state-of-the-art SNNs. Compared with advanced ANNs, it also achieves competitive performance.Our code is available at https://github.com/ISChenawei/SpikeViMFormer

