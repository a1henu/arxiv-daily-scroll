---
layout: default
title: MMPG: MoE-based Adaptive Multi-Perspective Graph Fusion for Protein Representation Learning
---

# MMPG: MoE-based Adaptive Multi-Perspective Graph Fusion for Protein Representation Learning
**arXiv**：[2601.10157v1](https://arxiv.org/abs/2601.10157) · [PDF](https://arxiv.org/pdf/2601.10157.pdf)  
**作者**：Yusong Wang, Jialun Shen, Zhihao Wu, Yicheng Xu, Shiyin Tan, Mingkun Xu, Changshuo Wang, Zixing Song, Prayag Tiwari  

**一句话要点**：提出MMPG框架，通过多视角图构建与MoE自适应融合解决蛋白质表示学习中的单视角限制问题。

**关键词**：蛋白质表示学习, 图神经网络, 多视角图融合, 专家混合, 残基相互作用, 自适应学习

## 3 点简述
- 核心问题：现有GNN方法依赖单视角图构建，导致蛋白质表示不完整。
- 方法要点：从物理、化学和几何视角构建图，并利用MoE模块自适应融合多视角特征。
- 实验或效果：在四个下游蛋白质任务上验证了MMPG的先进性能，提升了表示质量。

## 摘要（原文）

> Graph Neural Networks (GNNs) have been widely adopted for Protein Representation Learning (PRL), as residue interaction networks can be naturally represented as graphs. Current GNN-based PRL methods typically rely on single-perspective graph construction strategies, which capture partial properties of residue interactions, resulting in incomplete protein representations. To address this limitation, we propose MMPG, a framework that constructs protein graphs from multiple perspectives and adaptively fuses them via Mixture of Experts (MoE) for PRL. MMPG constructs graphs from physical, chemical, and geometric perspectives to characterize different properties of residue interactions. To capture both perspective-specific features and their synergies, we develop an MoE module, which dynamically routes perspectives to specialized experts, where experts learn intrinsic features and cross-perspective interactions. We quantitatively verify that MoE automatically specializes experts in modeling distinct levels of interaction from individual representations, to pairwise inter-perspective synergies, and ultimately to a global consensus across all perspectives. Through integrating this multi-level information, MMPG produces superior protein representations and achieves advanced performance on four different downstream protein tasks.

