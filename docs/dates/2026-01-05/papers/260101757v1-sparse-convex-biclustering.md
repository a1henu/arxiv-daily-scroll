---
layout: default
title: Sparse Convex Biclustering
---

# Sparse Convex Biclustering
**arXiv**：[2601.01757v1](https://arxiv.org/abs/2601.01757) · [PDF](https://arxiv.org/pdf/2601.01757.pdf)  
**作者**：Jiakun Jiang, Dewei Xiang, Chenliang Gu, Wei Liu, Binhuan Wang  

**一句话要点**：提出Sparse Convex Biclustering以解决高维大规模数据双聚类中的噪声累积和非凸优化问题。

**关键词**：双聚类, 凸优化, 稀疏性, 高维数据, 稳定性调优, 大规模数据集

## 3 点简述
- 核心问题：现有双聚类方法在高维大规模数据中面临噪声累积、非凸优化限制和计算复杂度高，导致准确性和稳定性下降。
- 方法要点：采用凸优化框架，通过惩罚噪声和基于稳定性的调优准则，平衡聚类保真度和稀疏性。
- 实验或效果：数值模拟和鼠嗅球数据应用显示，SpaCoBi在准确性上显著优于现有方法，适用于高维大规模数据集。

## 摘要（原文）

> Biclustering is an essential unsupervised machine learning technique for simultaneously clustering rows and columns of a data matrix, with widespread applications in genomics, transcriptomics, and other high-dimensional omics data. Despite its importance, existing biclustering methods struggle to meet the demands of modern large-scale datasets. The challenges stem from the accumulation of noise in high-dimensional features, the limitations of non-convex optimization formulations, and the computational complexity of identifying meaningful biclusters. These issues often result in reduced accuracy and stability as the size of the dataset increases. To overcome these challenges, we propose Sparse Convex Biclustering (SpaCoBi), a novel method that penalizes noise during the biclustering process to improve both accuracy and robustness. By adopting a convex optimization framework and introducing a stability-based tuning criterion, SpaCoBi achieves an optimal balance between cluster fidelity and sparsity. Comprehensive numerical studies, including simulations and an application to mouse olfactory bulb data, demonstrate that SpaCoBi significantly outperforms state-of-the-art methods in accuracy. These results highlight SpaCoBi as a robust and efficient solution for biclustering in high-dimensional and large-scale datasets.

