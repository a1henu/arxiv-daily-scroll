---
layout: default
title: Local-Global Multimodal Contrastive Learning for Molecular Property Prediction
---

# Local-Global Multimodal Contrastive Learning for Molecular Property Prediction
**arXiv**：[2601.22610v1](https://arxiv.org/abs/2601.22610) · [PDF](https://arxiv.org/pdf/2601.22610.pdf)  
**作者**：Xiayu Liu, Zhengyi Lu, Yunhong Liao, Chan Fan, Hou-biao Li  

**一句话要点**：提出LGM-CL框架，通过局部-全局多模态对比学习预测分子性质。

**关键词**：分子性质预测, 多模态学习, 对比学习, 图神经网络, 化学语义, 分子表示学习

## 3 点简述
- 核心问题：分子性质预测需整合结构信息与化学语义。
- 方法要点：使用AttentiveFP和Graph Transformer编码局部功能组与全局拓扑，并通过对比学习对齐。
- 实验或效果：在MoleculeNet基准测试中，分类和回归任务均表现优异。

## 摘要（原文）

> Accurate molecular property prediction requires integrating complementary information from molecular structure and chemical semantics. In this work, we propose LGM-CL, a local-global multimodal contrastive learning framework that jointly models molecular graphs and textual representations derived from SMILES and chemistry-aware augmented texts. Local functional group information and global molecular topology are captured using AttentiveFP and Graph Transformer encoders, respectively, and aligned through self-supervised contrastive learning. In addition, chemically enriched textual descriptions are contrasted with original SMILES to incorporate physicochemical semantics in a task-agnostic manner. During fine-tuning, molecular fingerprints are further integrated via Dual Cross-attention multimodal fusion. Extensive experiments on MoleculeNet benchmarks demonstrate that LGM-CL achieves consistent and competitive performance across both classification and regression tasks, validating the effectiveness of unified local-global and multimodal representation learning.

