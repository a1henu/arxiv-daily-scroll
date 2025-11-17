---
layout: default
title: Disentangling Emotional Bases and Transient Fluctuations: A Low-Rank Sparse Decomposition Approach for Video Affective Analysis
---

# Disentangling Emotional Bases and Transient Fluctuations: A Low-Rank Sparse Decomposition Approach for Video Affective Analysis
**arXiv**：[2511.11406v1](https://arxiv.org/abs/2511.11406) · [PDF](https://arxiv.org/pdf/2511.11406.pdf)  
**作者**：Feng-Qi Cui, Jinyang Huang, Ziyu Jia, Xinyu Li, Xin Yan, Xiaokang Zhou, Meng Wang  

**一句话要点**：提出低秩稀疏情感理解框架以解决视频情感分析中的动态分解问题

**关键词**：视频情感计算, 低秩稀疏分解, 情感基提取, 瞬态波动分离, 层次建模, 鲁棒性优化

## 3 点简述
- 核心问题：视频情感计算因复杂动态导致模型不稳定和表示退化，缺乏层次结构机制
- 方法要点：使用低秩稀疏原理分解情感基和瞬态波动，通过三个模块实现层次建模
- 实验或效果：多数据集实验验证框架提升鲁棒性和动态辨别力，证明方法有效性

## 摘要（原文）

> Video-based Affective Computing (VAC), vital for emotion analysis and human-computer interaction, suffers from model instability and representational degradation due to complex emotional dynamics. Since the meaning of different emotional fluctuations may differ under different emotional contexts, the core limitation is the lack of a hierarchical structural mechanism to disentangle distinct affective components, i.e., emotional bases (the long-term emotional tone), and transient fluctuations (the short-term emotional fluctuations). To address this, we propose the Low-Rank Sparse Emotion Understanding Framework (LSEF), a unified model grounded in the Low-Rank Sparse Principle, which theoretically reframes affective dynamics as a hierarchical low-rank sparse compositional process. LSEF employs three plug-and-play modules, i.e., the Stability Encoding Module (SEM) captures low-rank emotional bases; the Dynamic Decoupling Module (DDM) isolates sparse transient signals; and the Consistency Integration Module (CIM) reconstructs multi-scale stability and reactivity coherence. This framework is optimized by a Rank Aware Optimization (RAO) strategy that adaptively balances gradient smoothness and sensitivity. Extensive experiments across multiple datasets confirm that LSEF significantly enhances robustness and dynamic discrimination, which further validates the effectiveness and generality of hierarchical low-rank sparse modeling for understanding affective dynamics.

