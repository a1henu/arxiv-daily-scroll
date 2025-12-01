---
layout: default
title: Flow Straighter and Faster: Efficient One-Step Generative Modeling via MeanFlow on Rectified Trajectories
---

# Flow Straighter and Faster: Efficient One-Step Generative Modeling via MeanFlow on Rectified Trajectories
**arXiv**：[2511.23342v1](https://arxiv.org/abs/2511.23342) · [PDF](https://arxiv.org/pdf/2511.23342.pdf)  
**作者**：Xinxi Zhang, Shiwei Tan, Quang Nguyen, Quan Dao, Ligong Han, Xiaoxiao He, Tunyu Zhang, Alen Mrdovic, Dimitris Metaxas  

**一句话要点**：提出Rectified MeanFlow以在整流轨迹上高效实现一步生成建模

**关键词**：生成建模, 整流流, 一步采样, 平均速度场, 训练效率, 图像生成

## 3 点简述
- 核心问题：基于流的生成模型采样依赖昂贵ODE积分，一步采样方法如Rectified Flow需多步迭代，MeanFlow在弯曲流上训练慢且噪声大。
- 方法要点：Rectified MeanFlow在整流轨迹上建模平均速度场，仅需单步reflow，无需完美直线化，并引入截断启发式减少曲率。
- 实验或效果：在ImageNet多分辨率上，Re-MeanFlow在样本质量和训练效率上优于先前一步流蒸馏和Rectified Flow方法。

## 摘要（原文）

> Flow-based generative models have recently demonstrated strong performance, yet sampling typically relies on expensive numerical integration of ordinary differential equations (ODEs). Rectified Flow enables one-step sampling by learning nearly straight probability paths, but achieving such straightness requires multiple computationally intensive reflow iterations. MeanFlow achieves one-step generation by directly modeling the average velocity over time; however, when trained on highly curved flows, it suffers from slow convergence and noisy supervision. To address these limitations, we propose Rectified MeanFlow, a framework that models the mean velocity field along the rectified trajectory using only a single reflow step. This eliminates the need for perfectly straightened trajectories while enabling efficient training. Furthermore, we introduce a simple yet effective truncation heuristic that aims to reduce residual curvature and further improve performance. Extensive experiments on ImageNet at 64, 256, and 512 resolutions show that Re-MeanFlow consistently outperforms prior one-step flow distillation and Rectified Flow methods in both sample quality and training efficiency. Code is available at https://github.com/Xinxi-Zhang/Re-MeanFlow.

