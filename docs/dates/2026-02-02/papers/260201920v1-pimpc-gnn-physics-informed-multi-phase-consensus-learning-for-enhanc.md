---
layout: default
title: PIMPC-GNN: Physics-Informed Multi-Phase Consensus Learning for Enhancing Imbalanced Node Classification in Graph Neural Networks
---

# PIMPC-GNN: Physics-Informed Multi-Phase Consensus Learning for Enhancing Imbalanced Node Classification in Graph Neural Networks
**arXiv**：[2602.01920v1](https://arxiv.org/abs/2602.01920) · [PDF](https://arxiv.org/pdf/2602.01920.pdf)  
**作者**：Abdul Joseph Fofanah, Lian Wen, David Chen  

**一句话要点**：提出PIMPC-GNN框架，通过物理启发的多阶段共识学习增强图神经网络中的不平衡节点分类。

**关键词**：图神经网络, 不平衡节点分类, 物理启发学习, 多阶段共识, 热力学扩散, Kuramoto同步

## 3 点简述
- 核心问题：图神经网络在类别不平衡设置中表现不佳，少数类预测偏向多数类。
- 方法要点：整合热力学扩散、Kuramoto同步和谱嵌入，结合类自适应集成权重和失衡感知损失。
- 实验或效果：在五个基准数据集上优于16个基线，少数类召回率提升最高达12.7%。

## 摘要（原文）

> Graph neural networks (GNNs) often struggle in class-imbalanced settings, where minority classes are under-represented and predictions are biased toward majorities. We propose \textbf{PIMPC-GNN}, a physics-informed multi-phase consensus framework for imbalanced node classification. Our method integrates three complementary dynamics: (i) thermodynamic diffusion, which spreads minority labels to capture long-range dependencies, (ii) Kuramoto synchronisation, which aligns minority nodes through oscillatory consensus, and (iii) spectral embedding, which separates classes via structural regularisation. These perspectives are combined through class-adaptive ensemble weighting and trained with an imbalance-aware loss that couples balanced cross-entropy with physics-based constraints. Across five benchmark datasets and imbalance ratios from 5-100, PIMPC-GNN outperforms 16 state-of-the-art baselines, achieving notable gains in minority-class recall (up to +12.7\%) and balanced accuracy (up to +8.3\%). Beyond empirical improvements, the framework also provides interpretable insights into consensus dynamics in graph learning. The code is available at \texttt{https://github.com/afofanah/PIMPC-GNN}.

