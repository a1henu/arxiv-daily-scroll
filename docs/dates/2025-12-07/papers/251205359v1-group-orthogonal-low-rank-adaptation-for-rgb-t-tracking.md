---
layout: default
title: Group Orthogonal Low-Rank Adaptation for RGB-T Tracking
---

# Group Orthogonal Low-Rank Adaptation for RGB-T Tracking
**arXiv**：[2512.05359v1](https://arxiv.org/abs/2512.05359) · [PDF](https://arxiv.org/pdf/2512.05359.pdf)  
**作者**：Zekai Shao, Yufan Hu, Jingyuan Liu, Bin Fan, Hongmin Liu  

**一句话要点**：提出组正交低秩适应框架以解决RGB-T跟踪中参数冗余问题

**关键词**：RGB-T跟踪, 参数高效微调, 低秩适应, 正交约束, 特征学习, 冗余减少

## 3 点简述
- 核心问题：低秩适应在RGB-T跟踪中存在显著参数冗余，限制模型学习多样性知识
- 方法要点：采用秩分解分区策略量化重要性，冻结关键秩，对冗余秩施加组间正交约束
- 实验或效果：在四个基准数据集上显著优于现有方法，验证了减少冗余和增强特征表示的有效性

## 摘要（原文）

> Parameter-efficient fine-tuning has emerged as a promising paradigm in RGB-T tracking, enabling downstream task adaptation by freezing pretrained parameters and fine-tuning only a small set of parameters. This set forms a rank space made up of multiple individual ranks, whose expressiveness directly shapes the model's adaptability. However, quantitative analysis reveals low-rank adaptation exhibits significant redundancy in the rank space, with many ranks contributing almost no practical information. This hinders the model's ability to learn more diverse knowledge to address the various challenges in RGB-T tracking. To address this issue, we propose the Group Orthogonal Low-Rank Adaptation (GOLA) framework for RGB-T tracking, which effectively leverages the rank space through structured parameter learning. Specifically, we adopt a rank decomposition partitioning strategy utilizing singular value decomposition to quantify rank importance, freeze crucial ranks to preserve the pretrained priors, and cluster the redundant ranks into groups to prepare for subsequent orthogonal constraints. We further design an inter-group orthogonal constraint strategy. This constraint enforces orthogonality between rank groups, compelling them to learn complementary features that target diverse challenges, thereby alleviating information redundancy. Experimental results demonstrate that GOLA effectively reduces parameter redundancy and enhances feature representation capabilities, significantly outperforming state-of-the-art methods across four benchmark datasets and validating its effectiveness in RGB-T tracking tasks.

