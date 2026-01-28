---
layout: default
title: PCEvo: Path-Consistent Molecular Representation via Virtual Evolutionary
---

# PCEvo: Path-Consistent Molecular Representation via Virtual Evolutionary
**arXiv**：[2601.19257v1](https://arxiv.org/abs/2601.19257) · [PDF](https://arxiv.org/pdf/2601.19257.pdf)  
**作者**：Kun Li, Longtao Hu, Yida Xiong, Jiajun Yu, Hongzhi Zhang, Jiameng Chen, Xiantao Cai, Jia Wu, Wenbin Hu  

**一句话要点**：提出PCEvo方法，通过虚拟进化路径增强分子表示，以解决少样本学习中的泛化问题。

**关键词**：分子表示学习, 少样本学习, 虚拟进化路径, 路径一致性, 化学编辑路径

## 3 点简述
- 核心问题：少样本分子表示学习中，监督数据稀缺导致模型泛化能力差。
- 方法要点：枚举化学可行编辑路径，引入路径一致性目标，利用虚拟进化路径进行逐步监督。
- 实验或效果：在QM9和MoleculeNet数据集上，PCEvo显著提升少样本泛化性能。

## 摘要（原文）

> Molecular representation learning aims to learn vector embeddings that capture molecular structure and geometry, thereby enabling property prediction and downstream scientific applications. In many AI for science tasks, labeled data are expensive to obtain and therefore limited in availability. Under the few-shot setting, models trained with scarce supervision often learn brittle structure-property relationships, resulting in substantially higher prediction errors and reduced generalization to unseen molecules. To address this limitation, we propose PCEvo, a path-consistent representation method that learns from virtual paths through dynamic structural evolution. PCEvo enumerates multiple chemically feasible edit paths between retrieved similar molecular pairs under topological dependency constraints. It transforms the labels of the two molecules into stepwise supervision along each virtual evolutionary path. It introduces a path-consistency objective that enforces prediction invariance across alternative paths connecting the same two molecules. Comprehensive experiments on the QM9 and MoleculeNet datasets demonstrate that PCEvo substantially improves the few-shot generalization performance of baseline methods. The code is available at https://anonymous.4open.science/r/PCEvo-4BF2.

