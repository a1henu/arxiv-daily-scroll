---
layout: default
title: SOMtime the World Ain$'$t Fair: Violating Fairness Using Self-Organizing Maps
---

# SOMtime the World Ain$'$t Fair: Violating Fairness Using Self-Organizing Maps
**arXiv**：[2602.18201v1](https://arxiv.org/abs/2602.18201) · [PDF](https://arxiv.org/pdf/2602.18201.pdf)  
**作者**：Joseph Bingham, Netanel Arussy, Dvir Aran  

**一句话要点**：提出SOMtime方法，揭示无监督表示中敏感属性泄露的公平性风险

**关键词**：无监督表示学习, 公平性审计, 自组织映射, 敏感属性泄露, 机器学习管道

## 3 点简述
- 核心问题：无监督表示在训练中排除敏感属性时，仍可能泄露这些属性，挑战公平性假设
- 方法要点：基于高容量自组织映射的SOMtime方法，能恢复与敏感属性对齐的潜在轴
- 实验或效果：在真实数据集上，SOMtime的斯皮尔曼相关性高达0.85，远超PCA和UMAP等方法

## 摘要（原文）

> Unsupervised representations are widely assumed to be neutral with respect to sensitive attributes when those attributes are withheld from training. We show that this assumption is false. Using SOMtime, a topology-preserving representation method based on high-capacity Self-Organizing Maps, we demonstrate that sensitive attributes such as age and income emerge as dominant latent axes in purely unsupervised embeddings, even when explicitly excluded from the input. On two large-scale real-world datasets (the World Values Survey across five countries and the Census-Income dataset), SOMtime recovers monotonic orderings aligned with withheld sensitive attributes, achieving Spearman correlations of up to 0.85, whereas PCA and UMAP typically remain below 0.23 (with a single exception reaching 0.31), and against t-SNE and autoencoders which achieve at most 0.34. Furthermore, unsupervised segmentation of SOMtime embeddings produces demographically skewed clusters, demonstrating downstream fairness risks without any supervised task. These findings establish that \textit{fairness through unawareness} fails at the representation level for ordinal sensitive attributes and that fairness auditing must extend to unsupervised components of machine learning pipelines. We have made the code available at~ https://github.com/JosephBingham/SOMtime

