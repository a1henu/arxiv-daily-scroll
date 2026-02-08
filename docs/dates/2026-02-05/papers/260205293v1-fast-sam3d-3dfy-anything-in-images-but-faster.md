---
layout: default
title: Fast-SAM3D: 3Dfy Anything in Images but Faster
---

# Fast-SAM3D: 3Dfy Anything in Images but Faster
**arXiv**：[2602.05293v1](https://arxiv.org/abs/2602.05293) · [PDF](https://arxiv.org/pdf/2602.05293.pdf)  
**作者**：Weilun Feng, Mingqiang Wu, Zhiliang Chen, Chuanguang Yang, Haotong Qin, Yuqi Li, Xiaokun Liu, Guoxin Fan, Zhulin An, Libo Huang, Yulun Zhang, Michele Magno, Yongjun Xu  

**一句话要点**：提出Fast-SAM3D框架以加速SAM3D的3D重建，通过动态对齐计算与生成复杂度。

**关键词**：3D重建, 推理加速, 异构性感知, 单视图生成, 训练免费框架

## 3 点简述
- 核心问题：SAM3D的推理延迟高，通用加速策略因忽略多级异构性而失效。
- 方法要点：集成模态感知步缓存、联合时空令牌雕刻和频谱感知令牌聚合机制。
- 实验或效果：实现最高2.67倍端到端加速，保真度损失可忽略，建立高效单视图3D生成新帕累托前沿。

## 摘要（原文）

> SAM3D enables scalable, open-world 3D reconstruction from complex scenes, yet its deployment is hindered by prohibitive inference latency. In this work, we conduct the \textbf{first systematic investigation} into its inference dynamics, revealing that generic acceleration strategies are brittle in this context. We demonstrate that these failures stem from neglecting the pipeline's inherent multi-level \textbf{heterogeneity}: the kinematic distinctiveness between shape and layout, the intrinsic sparsity of texture refinement, and the spectral variance across geometries. To address this, we present \textbf{Fast-SAM3D}, a training-free framework that dynamically aligns computation with instantaneous generation complexity. Our approach integrates three heterogeneity-aware mechanisms: (1) \textit{Modality-Aware Step Caching} to decouple structural evolution from sensitive layout updates; (2) \textit{Joint Spatiotemporal Token Carving} to concentrate refinement on high-entropy regions; and (3) \textit{Spectral-Aware Token Aggregation} to adapt decoding resolution. Extensive experiments demonstrate that Fast-SAM3D delivers up to \textbf{2.67$\times$} end-to-end speedup with negligible fidelity loss, establishing a new Pareto frontier for efficient single-view 3D generation. Our code is released in https://github.com/wlfeng0509/Fast-SAM3D.

