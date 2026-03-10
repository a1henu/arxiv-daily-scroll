---
layout: default
title: Interactive World Simulator for Robot Policy Training and Evaluation
---

# Interactive World Simulator for Robot Policy Training and Evaluation
**arXiv**：[2603.08546v1](https://arxiv.org/abs/2603.08546) · [PDF](https://arxiv.org/pdf/2603.08546.pdf)  
**作者**：Yixuan Wang, Rhythm Syed, Fangyu Wu, Mengchao Zhang, Aykut Onol, Jose Barreiros, Hooshang Nayyeri, Tony Dear, Huan Zhang, Yunzhu Li  

**一句话要点**：提出交互式世界模拟器，以解决机器人策略训练与评估中世界模型速度慢和物理一致性不足的问题。

**关键词**：世界模型, 机器人策略训练, 视频预测, 物理一致性, 模拟评估, 模仿学习

## 3 点简述
- 核心问题：现有动作条件视频预测模型速度慢，长期物理交互一致性差，限制机器人策略训练与评估的可扩展性。
- 方法要点：利用一致性模型进行图像解码和潜在空间动态预测，实现快速稳定的物理交互模拟。
- 实验或效果：模型支持15 FPS下超过10分钟的稳定交互，生成数据训练的模仿策略性能与真实数据相当，模拟与真实性能强相关。

## 摘要（原文）

> Action-conditioned video prediction models (often referred to as world models) have shown strong potential for robotics applications, but existing approaches are often slow and struggle to capture physically consistent interactions over long horizons, limiting their usefulness for scalable robot policy training and evaluation. We present Interactive World Simulator, a framework for building interactive world models from a moderate-sized robot interaction dataset. Our approach leverages consistency models for both image decoding and latent-space dynamics prediction, enabling fast and stable simulation of physical interactions. In our experiments, the learned world models produce interaction-consistent pixel-level predictions and support stable long-horizon interactions for more than 10 minutes at 15 FPS on a single RTX 4090 GPU. Our framework enables scalable demonstration collection solely within the world models to train state-of-the-art imitation policies. Through extensive real-world evaluation across diverse tasks involving rigid objects, deformable objects, object piles, and their interactions, we find that policies trained on world-model-generated data perform comparably to those trained on the same amount of real-world data. Additionally, we evaluate policies both within the world models and in the real world across diverse tasks, and observe a strong correlation between simulated and real-world performance. Together, these results establish the Interactive World Simulator as a stable and physically consistent surrogate for scalable robotic data generation and faithful, reproducible policy evaluation.

