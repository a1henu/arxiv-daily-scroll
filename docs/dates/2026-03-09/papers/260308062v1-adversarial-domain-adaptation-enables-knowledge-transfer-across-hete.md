---
layout: default
title: Adversarial Domain Adaptation Enables Knowledge Transfer Across Heterogeneous RNA-Seq Datasets
---

# Adversarial Domain Adaptation Enables Knowledge Transfer Across Heterogeneous RNA-Seq Datasets
**arXiv**：[2603.08062v1](https://arxiv.org/abs/2603.08062) · [PDF](https://arxiv.org/pdf/2603.08062.pdf)  
**作者**：Kevin Dradjat, Massinissa Hamidi, Blaise Hanczar  

**一句话要点**：提出基于对抗域适应的深度学习框架，实现跨异构RNA-Seq数据集的知识迁移以提升癌症分类准确性。

**关键词**：域适应, RNA-Seq分析, 深度学习, 知识迁移, 癌症分类, 对抗训练

## 3 点简述
- 核心问题：RNA-Seq数据集中样本有限且预处理异构，导致深度学习模型过拟合和泛化能力差。
- 方法要点：通过联合优化分类和域对齐目标，学习域不变潜在空间，采用对抗训练和正则化确保稳定性。
- 实验或效果：在TCGA、ARCHS4、GTEx数据集上评估，相比非自适应基线，癌症和组织类型分类准确性显著提升，尤其在低数据场景下。

## 摘要（原文）

> Accurate phenotype prediction from RNA sequencing (RNA-seq) data is essential for diagnosis, biomarker discovery, and personalized medicine. Deep learning models have demonstrated strong potential to outperform classical machine learning approaches, but their performance relies on large, well-annotated datasets. In transcriptomics, such datasets are frequently limited, leading to over-fitting and poor generalization. Knowledge transfer from larger, more general datasets can alleviate this issue. However, transferring information across RNA-seq datasets remains challenging due to heterogeneous preprocessing pipelines and differences in target phenotypes. In this study, we propose a deep learning-based domain adaptation framework that enables effective knowledge transfer from a large general dataset to a smaller one for cancer type classification. The method learns a domain-invariant latent space by jointly optimizing classification and domain alignment objectives. To ensure stable training and robustness in data-scarce scenarios, the framework is trained with an adversarial approach with appropriate regularization. Both supervised and unsupervised approach variants are explored, leveraging labeled or unlabeled target samples. The framework is evaluated on three large-scale transcriptomic datasets (TCGA, ARCHS4, GTEx) to assess its ability to transfer knowledge across cohorts. Experimental results demonstrate consistent improvements in cancer and tissue type classification accuracy compared to non-adaptive baselines, particularly in low-data scenarios. Overall, this work highlights domain adaptation as a powerful strategy for data-efficient knowledge transfer in transcriptomics, enabling robust phenotype prediction under constrained data conditions.

