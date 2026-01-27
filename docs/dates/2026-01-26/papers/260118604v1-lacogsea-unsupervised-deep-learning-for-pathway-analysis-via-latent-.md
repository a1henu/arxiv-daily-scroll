---
layout: default
title: LaCoGSEA: Unsupervised deep learning for pathway analysis via latent correlation
---

# LaCoGSEA: Unsupervised deep learning for pathway analysis via latent correlation
**arXiv**：[2601.18604v1](https://arxiv.org/abs/2601.18604) · [PDF](https://arxiv.org/pdf/2601.18604.pdf)  
**作者**：Zhiwei Zheng, Kevin Bryson  

**一句话要点**：提出LaCoGSEA框架，通过潜在相关性和自编码器实现无监督通路富集分析。

**关键词**：无监督学习, 通路富集分析, 自编码器, 基因表达数据, 潜在相关性, 深度学习

## 3 点简述
- 核心问题：现有无监督通路分析方法依赖线性关系或通用XAI，难以捕获非线性结构和基因-通路关联。
- 方法要点：使用自编码器学习非线性流形，基于基因-潜在相关性生成无标签的基因排名，用于通路富集。
- 实验或效果：在癌症亚型聚类中优于基线，恢复更多生物相关通路，且在不同数据集上保持稳健性。

## 摘要（原文）

> Motivation: Pathway enrichment analysis is widely used to interpret gene expression data. Standard approaches, such as GSEA, rely on predefined phenotypic labels and pairwise comparisons, which limits their applicability in unsupervised settings. Existing unsupervised extensions, including single-sample methods, provide pathway-level summaries but primarily capture linear relationships and do not explicitly model gene-pathway associations. More recently, deep learning models have been explored to capture non-linear transcriptomic structure. However, their interpretation has typically relied on generic explainable AI (XAI) techniques designed for feature-level attribution. As these methods are not designed for pathway-level interpretation in unsupervised transcriptomic analyses, their effectiveness in this setting remains limited.
>   Results: To bridge this gap, we introduce LaCoGSEA (Latent Correlation GSEA), an unsupervised framework that integrates deep representation learning with robust pathway statistics. LaCoGSEA employs an autoencoder to capture non-linear manifolds and proposes a global gene-latent correlation metric as a proxy for differential expression, generating dense gene rankings without prior labels. We demonstrate that LaCoGSEA offers three key advantages: (i) it achieves improved clustering performance in distinguishing cancer subtypes compared to existing unsupervised baselines; (ii) it recovers a broader range of biologically meaningful pathways at higher ranks compared with linear dimensionality reduction and gradient-based XAI methods; and (iii) it maintains high robustness and consistency across varying experimental protocols and dataset sizes. Overall, LaCoGSEA provides state-of-the-art performance in unsupervised pathway enrichment analysis.
>   Availability and implementation: https://github.com/willyzzz/LaCoGSEA

