---
layout: default
title: Clustering-Guided Spatial-Spectral Mamba for Hyperspectral Image Classification
---

# Clustering-Guided Spatial-Spectral Mamba for Hyperspectral Image Classification
**arXiv**：[2601.16098v1](https://arxiv.org/abs/2601.16098) · [PDF](https://arxiv.org/pdf/2601.16098.pdf)  
**作者**：Zack Dewis, Yimin Zhu, Zhengsen Xu, Mabel Heffring, Saeid Taleghanidoozdoozan, Quinn Ledingham, Lincoln Linlin Xu  

**一句话要点**：提出聚类引导的空间-光谱Mamba框架以提升高光谱图像分类性能

**关键词**：高光谱图像分类, Mamba模型, 聚类引导, 空间-光谱融合, 注意力机制

## 3 点简述
- 核心问题：Mamba模型在高光谱图像分类中面临序列定义效率低和适应性差的挑战。
- 方法要点：集成聚类机制到空间Mamba架构，结合光谱Mamba模块，并引入注意力驱动令牌选择机制。
- 实验或效果：在多个数据集上验证，相比现有方法实现更高准确率和更好边界保持。

## 摘要（原文）

> Although Mamba models greatly improve Hyperspectral Image (HSI) classification, they have critical challenges in terms defining efficient and adaptive token sequences for improve performance. This paper therefore presents CSSMamba (Clustering-guided Spatial-Spectral Mamba) framework to better address the challenges, with the following contributions. First, to achieve efficient and adaptive token sequences for improved Mamba performance, we integrate the clustering mechanism into a spatial Mamba architecture, leading to a cluster-guided spatial Mamba module (CSpaMamba) that reduces the Mamba sequence length and improves Mamba feature learning capability. Second, to improve the learning of both spatial and spectral information, we integrate the CSpaMamba module with a spectral mamba module (SpeMamba), leading to a complete clustering-guided spatial-spectral Mamba framework. Third, to further improve feature learning capability, we introduce an Attention-Driven Token Selection mechanism to optimize Mamba token sequencing. Last, to seamlessly integrate clustering into the Mamba model in a coherent manner, we design a Learnable Clustering Module that learns the cluster memberships in an adaptive manner. Experiments on the Pavia University, Indian Pines, and Liao-Ning 01 datasets demonstrate that CSSMamba achieves higher accuracy and better boundary preservation compared to state-of-the-art CNN, Transformer, and Mamba-based methods.

