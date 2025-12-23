---
layout: default
title: Efficient Personalization of Generative Models via Optimal Experimental Design
---

# Efficient Personalization of Generative Models via Optimal Experimental Design
**arXiv**：[2512.19057v1](https://arxiv.org/abs/2512.19057) · [PDF](https://arxiv.org/pdf/2512.19057.pdf)  
**作者**：Guy Schacht, Ziyad Sheebaelhamd, Riccardo De Santi, Mojmír Mutný, Andreas Krause  

**一句话要点**：提出基于最优实验设计的偏好查询方法，高效个性化生成模型

**关键词**：偏好学习, 最优实验设计, 生成模型个性化, 数据高效查询, 凸优化

## 3 点简述
- 核心问题：人类反馈获取成本高，需数据高效的查询选择方法以学习用户偏好
- 方法要点：将偏好查询选择建模为最大化潜在偏好模型信息的凸优化问题，提出ED-PBRL算法
- 实验或效果：在文本到图像生成模型个性化中，相比随机查询，减少所需偏好查询数量

## 摘要（原文）

> Preference learning from human feedback has the ability to align generative models with the needs of end-users. Human feedback is costly and time-consuming to obtain, which creates demand for data-efficient query selection methods. This work presents a novel approach that leverages optimal experimental design to ask humans the most informative preference queries, from which we can elucidate the latent reward function modeling user preferences efficiently. We formulate the problem of preference query selection as the one that maximizes the information about the underlying latent preference model. We show that this problem has a convex optimization formulation, and introduce a statistically and computationally efficient algorithm ED-PBRL that is supported by theoretical guarantees and can efficiently construct structured queries such as images or text. We empirically present the proposed framework by personalizing a text-to-image generative model to user-specific styles, showing that it requires less preference queries compared to random query selection.

