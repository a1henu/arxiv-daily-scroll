---
layout: default
title: Enhancing Spatial Understanding in Image Generation via Reward Modeling
---

# Enhancing Spatial Understanding in Image Generation via Reward Modeling
**arXiv**：[2602.24233v1](https://arxiv.org/abs/2602.24233) · [PDF](https://arxiv.org/pdf/2602.24233.pdf)  
**作者**：Zhenyu Tang, Chaoran Feng, Yufan Deng, Jie Wu, Xiaojie Li, Rui Wang, Yunpeng Chen, Daquan Zhou  

**一句话要点**：提出SpatialScore奖励模型以增强文本到图像生成中的空间关系理解

**关键词**：文本到图像生成, 空间关系理解, 奖励建模, 强化学习, 数据集构建

## 3 点简述
- 核心问题：文本到图像生成中复杂空间关系编码困难，需多次采样才能获得满意结果。
- 方法要点：构建SpatialReward-Dataset数据集，训练SpatialScore奖励模型评估空间关系准确性。
- 实验或效果：奖励模型性能超越领先专有模型，并通过在线强化学习显著提升空间生成能力。

## 摘要（原文）

> Recent progress in text-to-image generation has greatly advanced visual fidelity and creativity, but it has also imposed higher demands on prompt complexity-particularly in encoding intricate spatial relationships. In such cases, achieving satisfactory results often requires multiple sampling attempts. To address this challenge, we introduce a novel method that strengthens the spatial understanding of current image generation models. We first construct the SpatialReward-Dataset with over 80k preference pairs. Building on this dataset, we build SpatialScore, a reward model designed to evaluate the accuracy of spatial relationships in text-to-image generation, achieving performance that even surpasses leading proprietary models on spatial evaluation. We further demonstrate that this reward model effectively enables online reinforcement learning for the complex spatial generation. Extensive experiments across multiple benchmarks show that our specialized reward model yields significant and consistent gains in spatial understanding for image generation.

