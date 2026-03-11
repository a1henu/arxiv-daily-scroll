---
layout: default
title: Task Aware Modulation Using Representation Learning for Upsaling of Terrestrial Carbon Fluxes
---

# Task Aware Modulation Using Representation Learning for Upsaling of Terrestrial Carbon Fluxes
**arXiv**：[2603.09974v1](https://arxiv.org/abs/2603.09974) · [PDF](https://arxiv.org/pdf/2603.09974.pdf)  
**作者**：Aleksei Rozanov, Arvind Renganathan, Vipin Kumar  

**一句话要点**：提出任务感知调制与表征学习框架以提升陆地碳通量上采样精度

**关键词**：碳通量上采样, 表征学习, 任务感知调制, 知识引导架构, 时空建模, 地球系统科学

## 3 点简述
- 核心问题：陆地碳通量上采样因地面测量稀疏和区域偏差而难以泛化，导致系统偏差和高不确定性。
- 方法要点：结合时空表征学习与基于碳平衡方程的知识引导编码器-解码器架构和损失函数。
- 实验或效果：在150多个通量塔站点上，相比现有方法，RMSE降低8-9.6%，解释方差从19.4%提升至43.8%。

## 摘要（原文）

> Accurately upscaling terrestrial carbon fluxes is central to estimating the global carbon budget, yet remains challenging due to the sparse and regionally biased distribution of ground measurements. Existing data-driven upscaling products often fail to generalize beyond observed domains, leading to systematic regional biases and high predictive uncertainty. We introduce Task-Aware Modulation with Representation Learning (TAM-RL), a framework that couples spatio-temporal representation learning with knowledge-guided encoder-decoder architecture and loss function derived from the carbon balance equation. Across 150+ flux tower sites representing diverse biomes and climate regimes, TAM-RL improves predictive performance relative to existing state-of-the-art datasets, reducing RMSE by 8-9.6% and increasing explained variance ($R^2$) from 19.4% to 43.8%, depending on the target flux. These results demonstrate that integrating physically grounded constraints with adaptive representation learning can substantially enhance the robustness and transferability of global carbon flux estimates.

