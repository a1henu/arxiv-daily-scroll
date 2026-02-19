---
layout: default
title: Factored Latent Action World Models
---

# Factored Latent Action World Models
**arXiv**：[2602.16229v1](https://arxiv.org/abs/2602.16229) · [PDF](https://arxiv.org/pdf/2602.16229.pdf)  
**作者**：Zizhao Wang, Chang Shi, Jiaheng Hu, Kevin Rohling, Roberto Martín-Martín, Amy Zhang, Peter Stone  

**一句话要点**：提出因子化潜在动作模型以解决多实体场景中动作建模的挑战

**关键词**：潜在动作学习, 因子化动力学, 无动作视频生成, 世界模型, 多实体建模

## 3 点简述
- 核心问题：现有方法使用单一潜在动作控制整个场景，在复杂多实体环境中建模困难
- 方法要点：将场景分解为独立因子，每个因子推断自身潜在动作并预测下一步值
- 实验或效果：在模拟和真实数据集上，FLAM在预测精度和表示质量上优于先前工作

## 摘要（原文）

> Learning latent actions from action-free video has emerged as a powerful paradigm for scaling up controllable world model learning. Latent actions provide a natural interface for users to iteratively generate and manipulate videos. However, most existing approaches rely on monolithic inverse and forward dynamics models that learn a single latent action to control the entire scene, and therefore struggle in complex environments where multiple entities act simultaneously. This paper introduces Factored Latent Action Model (FLAM), a factored dynamics framework that decomposes the scene into independent factors, each inferring its own latent action and predicting its own next-step factor value. This factorized structure enables more accurate modeling of complex multi-entity dynamics and improves video generation quality in action-free video settings compared to monolithic models. Based on experiments on both simulation and real-world multi-entity datasets, we find that FLAM outperforms prior work in prediction accuracy and representation quality, and facilitates downstream policy learning, demonstrating the benefits of factorized latent action models.

