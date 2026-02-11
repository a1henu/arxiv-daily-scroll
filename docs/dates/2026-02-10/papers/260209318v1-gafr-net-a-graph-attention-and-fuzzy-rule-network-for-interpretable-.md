---
layout: default
title: GAFR-Net: A Graph Attention and Fuzzy-Rule Network for Interpretable Breast Cancer Image Classification
---

# GAFR-Net: A Graph Attention and Fuzzy-Rule Network for Interpretable Breast Cancer Image Classification
**arXiv**：[2602.09318v1](https://arxiv.org/abs/2602.09318) · [PDF](https://arxiv.org/pdf/2602.09318.pdf)  
**作者**：Lin-Guo Gao, Suxing Liu  

**一句话要点**：提出GAFR-Net，一种结合图注意力和模糊规则的网络，用于弱监督下可解释的乳腺癌病理图像分类。

**关键词**：乳腺癌病理图像分类, 图注意力网络, 模糊规则系统, 弱监督学习, 可解释人工智能, 医学图像分析

## 3 点简述
- 核心问题：乳腺癌病理图像分类在有限标注下性能下降且模型缺乏可解释性，阻碍临床应用。
- 方法要点：构建相似性驱动图表示，使用多头图注意力捕获组织关系，并集成可微分模糊规则模块生成透明诊断逻辑。
- 实验或效果：在多个基准数据集上优于现有方法，验证了其泛化能力和作为决策支持工具的实用性。

## 摘要（原文）

> Accurate classification of breast cancer histopathology images is pivotal for early oncological diagnosis and therapeutic intervention.However, conventional deep learning architectures often encounter performance degradation under limited annotations and suffer from a "blackbox" nature, hindering their clinical integration. To mitigate these limitations, we propose GAFRNet, a robust and interpretable Graph Attention and FuzzyRule Network specifically engineered for histopathology image classification with scarce supervision. GAFRNet constructs a similarity-driven graph representation to model intersample relationships and employs a multihead graph attention mechanism to capture complex relational features across heterogeneous tissue structures.Concurrently, a differentiable fuzzy-rule module encodes intrinsic topological descriptorsincluding node degree, clustering coefficient, and label consistencyinto explicit, human-understandable diagnostic logic. This design establishes transparent "IF-THEN" mappings that mimic the heuristic deduction process of medical experts, providing clear reasoning behind each prediction without relying on post-hoc attribution methods. Extensive evaluations on three benchmark datasets (BreakHis, Mini-DDSM, and ICIAR2018) demonstrate that GAFR-Net consistently outperforms various state-of-the-art methods across multiple magnifications and classification tasks. These results validate the superior generalization and practical utility of GAFR-Net as a reliable decision-support tool for weakly supervised medical image analysis.

