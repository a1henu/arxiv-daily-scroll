---
layout: default
title: DexFormer: Cross-Embodied Dexterous Manipulation via History-Conditioned Transformer
---

# DexFormer: Cross-Embodied Dexterous Manipulation via History-Conditioned Transformer
**arXiv**：[2602.08278v1](https://arxiv.org/abs/2602.08278) · [PDF](https://arxiv.org/pdf/2602.08278.pdf)  
**作者**：Ke Zhang, Lixin Xu, Chengyi Song, Junzhe Xu, Xiaoyi Lin, Zeyu Jiang, Renjing Xu  

**一句话要点**：提出DexFormer，基于历史条件Transformer实现跨具身灵巧操作

**关键词**：跨具身操作, 灵巧操作, Transformer, 零样本泛化, 历史条件策略

## 3 点简述
- 核心问题：灵巧操作面临具身变异性，不同高自由度手部需单独训练策略。
- 方法要点：使用改进Transformer，通过历史观测推断形态和动力学，动态适应不同手部配置。
- 实验或效果：在多种手部资产上训练，零样本泛化至Leap、Allegro和Rapid Hand。

## 摘要（原文）

> Dexterous manipulation remains one of the most challenging problems in robotics, requiring coherent control of high-DoF hands and arms under complex, contact-rich dynamics. A major barrier is embodiment variability: different dexterous hands exhibit distinct kinematics and dynamics, forcing prior methods to train separate policies or rely on shared action spaces with per-embodiment decoder heads. We present DexFormer, an end-to-end, dynamics-aware cross-embodiment policy built on a modified transformer backbone that conditions on historical observations. By using temporal context to infer morphology and dynamics on the fly, DexFormer adapts to diverse hand configurations and produces embodiment-appropriate control actions. Trained over a variety of procedurally generated dexterous-hand assets, DexFormer acquires a generalizable manipulation prior and exhibits strong zero-shot transfer to Leap Hand, Allegro Hand, and Rapid Hand. Our results show that a single policy can generalize across heterogeneous hand embodiments, establishing a scalable foundation for cross-embodiment dexterous manipulation. Project website: https://davidlxu.github.io/DexFormer-web/.

