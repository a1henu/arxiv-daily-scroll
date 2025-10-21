---
layout: default
title: Joint Multi-Condition Representation Modelling via Matrix Factorisation for Visual Place Recognition
---

# Joint Multi-Condition Representation Modelling via Matrix Factorisation for Visual Place Recognition
**arXiv**：[2510.17739v1](https://arxiv.org/abs/2510.17739) · [PDF](https://arxiv.org/pdf/2510.17739.pdf)  
**作者**：Timur Ismagilov, Shakaiba Majeed, Michael Milford, Tan Viet Tuyen Nguyen, Sarvapali D. Ramchurn, Shoaib Ehsan  

**一句话要点**：提出基于矩阵分解的多条件联合建模方法以提升视觉地点识别性能

**关键词**：视觉地点识别, 矩阵分解, 多条件建模, 无训练方法, 残差匹配, 基准数据集

## 3 点简述
- 多参考视觉地点识别中，数据多样性和模型复杂性导致高计算成本
- 采用无训练、描述符无关的矩阵分解方法，分解为基表示并实现残差匹配
- 在SotonMV基准上，Recall@1提升达18%，泛化性强且保持轻量级

## 摘要（原文）

> We address multi-reference visual place recognition (VPR), where reference
> sets captured under varying conditions are used to improve localisation
> performance. While deep learning with large-scale training improves robustness,
> increasing data diversity and model complexity incur extensive computational
> cost during training and deployment. Descriptor-level fusion via voting or
> aggregation avoids training, but often targets multi-sensor setups or relies on
> heuristics with limited gains under appearance and viewpoint change. We propose
> a training-free, descriptor-agnostic approach that jointly models places using
> multiple reference descriptors via matrix decomposition into basis
> representations, enabling projection-based residual matching. We also introduce
> SotonMV, a structured benchmark for multi-viewpoint VPR. On multi-appearance
> data, our method improves Recall@1 by up to ~18% over single-reference and
> outperforms multi-reference baselines across appearance and viewpoint changes,
> with gains of ~5% on unstructured data, demonstrating strong generalisation
> while remaining lightweight.

