---
layout: default
title: Pretrained Battery Transformer (PBT): A battery life prediction foundation model
---

# Pretrained Battery Transformer (PBT): A battery life prediction foundation model
**arXiv**：[2512.16334v1](https://arxiv.org/abs/2512.16334) · [PDF](https://arxiv.org/pdf/2512.16334.pdf)  
**作者**：Ruifeng Tan, Weixiang Hong, Jia Li, Jiaqiang Huang, Tong-Yi Zhang  

**一句话要点**：提出预训练电池Transformer以解决电池寿命预测中的数据稀缺与异质性问题

**关键词**：电池寿命预测, 基础模型, Transformer, 迁移学习, 锂离子电池, 专家混合层

## 3 点简述
- 核心问题：电池寿命预测受数据稀缺和老化条件异质性阻碍，缺乏基础模型。
- 方法要点：基于领域知识编码的专家混合层，构建首个电池寿命预测基础模型PBT。
- 实验或效果：在15个数据集上通过迁移学习实现最优性能，平均提升19.8%。

## 摘要（原文）

> Early prediction of battery cycle life is essential for accelerating battery research, manufacturing, and deployment. Although machine learning methods have shown encouraging results, progress is hindered by data scarcity and heterogeneity arising from diverse aging conditions. In other fields, foundation models (FMs) trained on diverse datasets have achieved broad generalization through transfer learning, but no FMs have been reported for battery cycle life prediction yet. Here we present the Pretrained Battery Transformer (PBT), the first FM for battery life prediction, developed through domain-knowledge-encoded mixture-of-expert layers. Validated on the largest public battery life database, PBT learns transferable representations from 13 lithium-ion battery (LIB) datasets, outperforming existing models by an average of 19.8%. With transfer learning, PBT achieves state-of-the-art performance across 15 diverse datasets encompassing various operating conditions, formation protocols, and chemistries of LIBs. This work establishes a foundation model pathway for battery lifetime prediction, paving the way toward universal battery lifetime prediction systems.

