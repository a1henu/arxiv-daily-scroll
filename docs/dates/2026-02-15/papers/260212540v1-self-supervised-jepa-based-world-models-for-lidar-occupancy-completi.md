---
layout: default
title: Self-Supervised JEPA-based World Models for LiDAR Occupancy Completion and Forecasting
---

# Self-Supervised JEPA-based World Models for LiDAR Occupancy Completion and Forecasting
**arXiv**：[2602.12540v1](https://arxiv.org/abs/2602.12540) · [PDF](https://arxiv.org/pdf/2602.12540.pdf)  
**作者**：Haoran Zhu, Anna Choromanska  

**一句话要点**：提出AD-LiST-JEPA，基于JEPA的自监督世界模型，用于LiDAR占用完成与预测

**关键词**：自动驾驶, 自监督学习, 世界模型, LiDAR预测, 占用完成

## 3 点简述
- 核心问题：自动驾驶需构建自监督世界模型以捕捉环境时空演化，支持长期规划
- 方法要点：使用JEPA框架从LiDAR数据预测未来时空演化，无需昂贵人工标注
- 实验或效果：通过LiDAR占用完成与预测任务评估，预训练编码器在JEPA学习后表现更优

## 摘要（原文）

> Autonomous driving, as an agent operating in the physical world, requires the fundamental capability to build \textit{world models} that capture how the environment evolves spatiotemporally in order to support long-term planning. At the same time, scalability demands learning such models in a self-supervised manner; \textit{joint-embedding predictive architecture (JEPA)} enables learning world models via leveraging large volumes of unlabeled data without relying on expensive human annotations. In this paper, we propose \textbf{AD-LiST-JEPA}, a self-supervised world model for autonomous driving that predicts future spatiotemporal evolution from LiDAR data using a JEPA framework. We evaluate the quality of the learned representations through a downstream LiDAR-based occupancy completion and forecasting (OCF) task, which jointly assesses perception and prediction. Proof of concept experiments show better OCF performance with pretrained encoder after JEPA-based world model learning.

