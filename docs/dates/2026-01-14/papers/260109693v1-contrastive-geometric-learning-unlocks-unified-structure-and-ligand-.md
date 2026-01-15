---
layout: default
title: Contrastive Geometric Learning Unlocks Unified Structure- and Ligand-Based Drug Design
---

# Contrastive Geometric Learning Unlocks Unified Structure- and Ligand-Based Drug Design
**arXiv**：[2601.09693v1](https://arxiv.org/abs/2601.09693) · [PDF](https://arxiv.org/pdf/2601.09693.pdf)  
**作者**：Lisa Schneckenreiter, Sohvi Luukkonen, Lukas Friedrich, Daniel Kuhn, Günter Klambauer  

**一句话要点**：提出对比几何学习模型ConGLUDe，统一结构和配体数据以解决药物设计中的分割问题。

**关键词**：对比学习, 几何深度学习, 药物设计, 虚拟筛选, 目标钓鱼, 蛋白质配体对齐

## 3 点简述
- 传统药物设计依赖分割的数据源和模型假设，限制了联合应用。
- ConGLUDe通过对比学习对齐配体与蛋白质全局表示和候选结合位点，无需预定义口袋。
- 在零样本虚拟筛选中达到最先进性能，并在目标钓鱼任务中显著优于现有方法。

## 摘要（原文）

> Structure-based and ligand-based computational drug design have traditionally relied on disjoint data sources and modeling assumptions, limiting their joint use at scale. In this work, we introduce Contrastive Geometric Learning for Unified Computational Drug Design (ConGLUDe), a single contrastive geometric model that unifies structure- and ligand-based training. ConGLUDe couples a geometric protein encoder that produces whole-protein representations and implicit embeddings of predicted binding sites with a fast ligand encoder, removing the need for pre-defined pockets. By aligning ligands with both global protein representations and multiple candidate binding sites through contrastive learning, ConGLUDe supports ligand-conditioned pocket prediction in addition to virtual screening and target fishing, while being trained jointly on protein-ligand complexes and large-scale bioactivity data. Across diverse benchmarks, ConGLUDe achieves state-of-the-art zero-shot virtual screening performance in settings where no binding pocket information is provided as input, substantially outperforms existing methods on a challenging target fishing task, and demonstrates competitive ligand-conditioned pocket selection. These results highlight the advantages of unified structure-ligand training and position ConGLUDe as a step toward general-purpose foundation models for drug discovery.

