---
layout: default
title: Refinement Contrastive Learning of Cell-Gene Associations for Unsupervised Cell Type Identification
---

# Refinement Contrastive Learning of Cell-Gene Associations for Unsupervised Cell Type Identification
**arXiv**：[2512.10640v1](https://arxiv.org/abs/2512.10640) · [PDF](https://arxiv.org/pdf/2512.10640.pdf)  
**作者**：Liang Peng, Haopeng Liu, Yixuan Ye, Cheng Liu, Wenjun Shen, Si Wu, Hau-San Wong  

**一句话要点**：提出scRCL框架，通过细胞-基因关联对比学习解决无监督细胞类型识别中紧密相关类型区分难题。

**关键词**：无监督细胞类型识别, 对比学习, 细胞-基因关联, 单细胞RNA-seq, 空间转录组学, 表示学习

## 3 点简述
- 核心问题：现有聚类方法忽略细胞-基因关联，难以区分紧密相关细胞类型。
- 方法要点：结合细胞-细胞结构对比分布对齐和基因相关性学习模块，增强细胞表示。
- 实验或效果：在单细胞RNA-seq和空间转录组数据集上优于基线，验证生物相关性。

## 摘要（原文）

> Unsupervised cell type identification is crucial for uncovering and characterizing heterogeneous populations in single cell omics studies. Although a range of clustering methods have been developed, most focus exclusively on intrinsic cellular structure and ignore the pivotal role of cell-gene associations, which limits their ability to distinguish closely related cell types. To this end, we propose a Refinement Contrastive Learning framework (scRCL) that explicitly incorporates cell-gene interactions to derive more informative representations. Specifically, we introduce two contrastive distribution alignment components that reveal reliable intrinsic cellular structures by effectively exploiting cell-cell structural relationships. Additionally, we develop a refinement module that integrates gene-correlation structure learning to enhance cell embeddings by capturing underlying cell-gene associations. This module strengthens connections between cells and their associated genes, refining the representation learning to exploiting biologically meaningful relationships. Extensive experiments on several single-cell RNA-seq and spatial transcriptomics benchmark datasets demonstrate that our method consistently outperforms state-of-the-art baselines in cell-type identification accuracy. Moreover, downstream biological analyses confirm that the recovered cell populations exhibit coherent gene-expression signatures, further validating the biological relevance of our approach. The code is available at https://github.com/THPengL/scRCL.

