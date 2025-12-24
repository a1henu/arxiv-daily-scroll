---
layout: default
title: AMoE: Agglomerative Mixture-of-Experts Vision Foundation Model
---

# AMoE: Agglomerative Mixture-of-Experts Vision Foundation Model
**arXiv**：[2512.20157v1](https://arxiv.org/abs/2512.20157) · [PDF](https://arxiv.org/pdf/2512.20157.pdf)  
**作者**：Sofian Chaybouti, Sanath Narayan, Yasser Dahou, Phúc H. Lê Khac, Ankit Singh, Ngoc Dung Huynh, Wamiq Reyaz Para, Hilde Kuehne, Hakim Hacid  

**一句话要点**：提出AMoE视觉基础模型，通过多教师蒸馏降低计算成本并提升数据效率。

**关键词**：视觉基础模型, 多教师蒸馏, 专家混合, 知识蒸馏, 数据效率, 计算成本优化

## 3 点简述
- 研究多教师蒸馏学习动态与数据效率，识别降低计算成本的关键因素。
- 引入AMoE模型，同时从SigLIP2和DINOv3蒸馏知识到专家混合学生模型。
- 结合非对称关系知识蒸馏损失、令牌平衡批处理和分层聚类采样，构建高效数据集OpenLVD200M。

## 摘要（原文）

> Vision foundation models trained via multi-teacher distillation offer a promising path toward unified visual representations, yet the learning dynamics and data efficiency of such approaches remain underexplored. In this paper, we systematically study multi-teacher distillation for vision foundation models and identify key factors that enable training at lower computational cost. We introduce Agglomerative Mixture-of-Experts Vision Foundation Models (AMoE), which distill knowledge from SigLIP2 and DINOv3 simultaneously into a Mixture-of-Experts student. We show that (1) our Asymmetric Relation-Knowledge Distillation loss preserves the geometric properties of each teacher while enabling effective knowledge transfer, (2) token-balanced batching that packs varying-resolution images into sequences with uniform token budgets stabilizes representation learning across resolutions without sacrificing performance, and (3) hierarchical clustering and sampling of training data--typically reserved for self-supervised learning--substantially improves sample efficiency over random sampling for multi-teacher distillation. By combining these findings, we curate OpenLVD200M, a 200M-image corpus that demonstrates superior efficiency for multi-teacher distillation. Instantiated in a Mixture-of-Experts. We release OpenLVD200M and distilled models.

