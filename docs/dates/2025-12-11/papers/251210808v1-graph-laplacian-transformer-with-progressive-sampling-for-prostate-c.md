---
layout: default
title: Graph Laplacian Transformer with Progressive Sampling for Prostate Cancer Grading
---

# Graph Laplacian Transformer with Progressive Sampling for Prostate Cancer Grading
**arXiv**：[2512.10808v1](https://arxiv.org/abs/2512.10808) · [PDF](https://arxiv.org/pdf/2512.10808.pdf)  
**作者**：Masum Shah Junayed, John Derek Van Vessem, Qian Wan, Gahie Nam, Sheida Nabavi  

**一句话要点**：提出图拉普拉斯注意力Transformer与迭代精炼模块，以提升前列腺癌分级性能与空间一致性。

**关键词**：前列腺癌分级, 全切片图像分析, 图神经网络, Transformer模型, 迭代精炼, 空间一致性

## 3 点简述
- 核心问题：全切片图像规模大、组织异质性强，现有方法因冗余区域选择导致性能下降。
- 方法要点：集成迭代精炼模块动态选择相关区域，图拉普拉斯Transformer建模组织连通性增强特征学习。
- 实验或效果：在多个数据集上超越先进方法，实现更高性能、空间一致性和计算效率。

## 摘要（原文）

> Prostate cancer grading from whole-slide images (WSIs) remains a challenging task due to the large-scale nature of WSIs, the presence of heterogeneous tissue structures, and difficulty of selecting diagnostically relevant regions. Existing approaches often rely on random or static patch selection, leading to the inclusion of redundant or non-informative regions that degrade performance. To address this, we propose a Graph Laplacian Attention-Based Transformer (GLAT) integrated with an Iterative Refinement Module (IRM) to enhance both feature learning and spatial consistency. The IRM iteratively refines patch selection by leveraging a pretrained ResNet50 for local feature extraction and a foundation model in no-gradient mode for importance scoring, ensuring only the most relevant tissue regions are preserved. The GLAT models tissue-level connectivity by constructing a graph where patches serve as nodes, ensuring spatial consistency through graph Laplacian constraints and refining feature representations via a learnable filtering mechanism that enhances discriminative histological structures. Additionally, a convex aggregation mechanism dynamically adjusts patch importance to generate a robust WSI-level representation. Extensive experiments on five public and one private dataset demonstrate that our model outperforms state-of-the-art methods, achieving higher performance and spatial consistency while maintaining computational efficiency.

