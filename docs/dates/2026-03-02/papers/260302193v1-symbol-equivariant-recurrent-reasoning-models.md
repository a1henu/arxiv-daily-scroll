---
layout: default
title: Symbol-Equivariant Recurrent Reasoning Models
---

# Symbol-Equivariant Recurrent Reasoning Models
**arXiv**：[2603.02193v1](https://arxiv.org/abs/2603.02193) · [PDF](https://arxiv.org/pdf/2603.02193.pdf)  
**作者**：Richard Freinschlag, Timo Bertram, Erich Kobler, Andreas Mayr, Günter Klambauer  

**一句话要点**：提出符号等变循环推理模型以提升神经推理的鲁棒性和可扩展性

**关键词**：符号等变性, 循环推理模型, 神经推理, 置换等变层, 数独求解, ARC-AGI

## 3 点简述
- 核心问题：现有循环推理模型处理符号对称性依赖数据增强，效率低且泛化能力有限。
- 方法要点：通过符号等变层在架构层面强制置换等变性，确保符号或颜色置换下解的一致性。
- 实验或效果：在9x9数独和ARC-AGI任务上优于先前模型，并实现从9x9到更大尺寸的泛化。

## 摘要（原文）

> Reasoning problems such as Sudoku and ARC-AGI remain challenging for neural networks. The structured problem solving architecture family of Recurrent Reasoning Models (RRMs), including Hierarchical Reasoning Model (HRM) and Tiny Recursive Model (TRM), offer a compact alternative to large language models, but currently handle symbol symmetries only implicitly via costly data augmentation. We introduce Symbol-Equivariant Recurrent Reasoning Models (SE-RRMs), which enforce permutation equivariance at the architectural level through symbol-equivariant layers, guaranteeing identical solutions under symbol or color permutations. SE-RRMs outperform prior RRMs on 9x9 Sudoku and generalize from just training on 9x9 to smaller 4x4 and larger 16x16 and 25x25 instances, to which existing RRMs cannot extrapolate. On ARC-AGI-1 and ARC-AGI-2, SE-RRMs achieve competitive performance with substantially less data augmentation and only 2 million parameters, demonstrating that explicitly encoding symmetry improves the robustness and scalability of neural reasoning. Code is available at https://github.com/ml-jku/SE-RRM.

