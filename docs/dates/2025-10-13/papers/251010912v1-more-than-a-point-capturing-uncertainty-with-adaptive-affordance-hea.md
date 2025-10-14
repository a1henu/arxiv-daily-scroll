---
layout: default
title: More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks
---

# More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks
**arXiv**：[2510.10912v1](https://arxiv.org/abs/2510.10912) · [PDF](https://arxiv.org/pdf/2510.10912.pdf)  
**作者**：Xinyu Shao, Yanzhe Tang, Pengwei Xie, Kaiwen Zhou, Yuzheng Zhuang, Xingyue Quan, Jianye Hao, Long Zeng, Xiu Li  

**一句话要点**：提出RoboMAP框架，使用自适应功能热图解决机器人空间接地中的不确定性问题

**关键词**：空间接地, 功能热图, 机器人任务, 不确定性建模, 零样本泛化

## 3 点简述
- 核心问题：语言引导机器人系统依赖离散点进行空间推理，易受感知噪声和语义模糊影响
- 方法要点：采用连续自适应功能热图表示空间目标，捕捉不确定性并提供丰富信息
- 实验或效果：在基准测试中超越SOTA，速度提升50倍，真实世界操作成功率82%

## 摘要（原文）

> Many language-guided robotic systems rely on collapsing spatial reasoning
> into discrete points, making them brittle to perceptual noise and semantic
> ambiguity. To address this challenge, we propose RoboMAP, a framework that
> represents spatial targets as continuous, adaptive affordance heatmaps. This
> dense representation captures the uncertainty in spatial grounding and provides
> richer information for downstream policies, thereby significantly enhancing
> task success and interpretability. RoboMAP surpasses the previous
> state-of-the-art on a majority of grounding benchmarks with up to a 50x speed
> improvement, and achieves an 82\% success rate in real-world manipulation.
> Across extensive simulated and physical experiments, it demonstrates robust
> performance and shows strong zero-shot generalization to navigation. More
> details and videos can be found at https://robo-map.github.io.

