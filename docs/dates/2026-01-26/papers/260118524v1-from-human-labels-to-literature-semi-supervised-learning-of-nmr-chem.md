---
layout: default
title: From Human Labels to Literature: Semi-Supervised Learning of NMR Chemical Shifts at Scale
---

# From Human Labels to Literature: Semi-Supervised Learning of NMR Chemical Shifts at Scale
**arXiv**：[2601.18524v1](https://arxiv.org/abs/2601.18524) · [PDF](https://arxiv.org/pdf/2601.18524.pdf)  
**作者**：Yongqi Jin, Yecheng Wang, Jun-jie Wang, Rong Zhu, Guolin Ke, Weinan E  

**一句话要点**：提出半监督框架，利用文献光谱大规模学习NMR化学位移，提升预测准确性和泛化能力。

**关键词**：NMR化学位移预测, 半监督学习, 文献数据挖掘, 排序损失函数, 溶剂效应建模

## 3 点简述
- 核心问题：现有NMR化学位移预测方法依赖有限标注数据，难以处理大规模分子数据集。
- 方法要点：通过排序损失函数处理无标注光谱，结合少量标注数据实现半监督学习。
- 实验或效果：模型在更大分子数据集上超越现有方法，首次捕获溶剂效应，验证文献数据有效性。

## 摘要（原文）

> Accurate prediction of nuclear magnetic resonance (NMR) chemical shifts is fundamental to spectral analysis and molecular structure elucidation, yet existing machine learning methods rely on limited, labor-intensive atom-assigned datasets. We propose a semi-supervised framework that learns NMR chemical shifts from millions of literature-extracted spectra without explicit atom-level assignments, integrating a small amount of labeled data with large-scale unassigned spectra. We formulate chemical shift prediction from literature spectra as a permutation-invariant set supervision problem, and show that under commonly satisfied conditions on the loss function, optimal bipartite matching reduces to a sorting-based loss, enabling stable large-scale semi-supervised training beyond traditional curated datasets. Our models achieve substantially improved accuracy and robustness over state-of-the-art methods and exhibit stronger generalization on significantly larger and more diverse molecular datasets. Moreover, by incorporating solvent information at scale, our approach captures systematic solvent effects across common NMR solvents for the first time. Overall, our results demonstrate that large-scale unlabeled spectra mined from the literature can serve as a practical and effective data source for training NMR shift models, suggesting a broader role of literature-derived, weakly structured data in data-centric AI for science.

