---
layout: default
title: EdgeMask-DG*: Learning Domain-Invariant Graph Structures via Adversarial Edge Masking
---

# EdgeMask-DG*: Learning Domain-Invariant Graph Structures via Adversarial Edge Masking
**arXiv**：[2602.05571v1](https://arxiv.org/abs/2602.05571) · [PDF](https://arxiv.org/pdf/2602.05571.pdf)  
**作者**：Rishabh Bhattacharya, Naresh Manwani  

**一句话要点**：提出EdgeMask-DG*，通过对抗性边掩码学习领域不变图结构以解决图结构偏移问题。

**关键词**：图神经网络, 领域泛化, 对抗性学习, 图结构学习, 特征增强

## 3 点简述
- 核心问题：图结构偏移挑战图神经网络，现有方法难以识别领域不变边。
- 方法要点：结合对抗性边掩码与特征增强图，自适应搜索领域不变结构。
- 实验或效果：在多个基准测试中达到新SOTA，Cora OOD准确率提升至78.0%。

## 摘要（原文）

> Structural shifts pose a significant challenge for graph neural networks, as graph topology acts as a covariate that can vary across domains. Existing domain generalization methods rely on fixed structural augmentations or training on globally perturbed graphs, mechanisms that do not pinpoint which specific edges encode domain-invariant information. We argue that domain-invariant structural information is not rigidly tied to a single topology but resides in the consensus across multiple graph structures derived from topology and feature similarity. To capture this, we first propose EdgeMask-DG, a novel min-max algorithm where an edge masker learns to find worst-case continuous masks subject to a sparsity constraint, compelling a task GNN to perform effectively under these adversarial structural perturbations. Building upon this, we introduce EdgeMask-DG*, an extension that applies this adversarial masking principle to an enriched graph. This enriched graph combines the original topology with feature-derived edges, allowing the model to discover invariances even when the original topology is noisy or domain-specific. EdgeMask-DG* is the first to systematically combine adaptive adversarial topology search with feature-enriched graphs. We provide a formal justification for our approach from a robust optimization perspective. We demonstrate that EdgeMask-DG* achieves new state-of-the-art performance on diverse graph domain generalization benchmarks, including citation networks, social networks, and temporal graphs. Notably, on the Cora OOD benchmark, EdgeMask-DG* lifts the worst-case domain accuracy to 78.0\%, a +3.8 pp improvement over the prior state of the art (74.2\%). The source code for our experiments can be found here: https://anonymous.4open.science/r/TMLR-EAEF/

