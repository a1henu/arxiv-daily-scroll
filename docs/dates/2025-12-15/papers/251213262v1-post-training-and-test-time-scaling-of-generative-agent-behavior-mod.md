---
layout: default
title: Post-Training and Test-Time Scaling of Generative Agent Behavior Models for Interactive Autonomous Driving
---

# Post-Training and Test-Time Scaling of Generative Agent Behavior Models for Interactive Autonomous Driving
**arXiv**：[2512.13262v1](https://arxiv.org/abs/2512.13262) · [PDF](https://arxiv.org/pdf/2512.13262.pdf)  
**作者**：Hyunki Seong, Jeong-Kyun Lee, Heesoo Myeong, Yongho Shin, Hyun-Mook Cho, Duck Hoon Kim, Pranav Desai, Monu Surana  

**一句话要点**：提出GRBO和Warm-K方法，以增强自动驾驶中生成式智能体行为模型的安全性和闭环性能。

**关键词**：自动驾驶行为建模, 强化学习后训练, 测试时采样策略, 闭环评估, 安全性能优化, 群体交互学习

## 3 点简述
- 核心问题：模仿学习模型存在数据集偏差，导致安全关键场景下鲁棒性不足，且多数研究依赖开环评估，忽略闭环执行中的累积误差。
- 方法要点：GRBO通过强化学习后训练，利用群体相对优势最大化和人类正则化微调预训练模型；Warm-K采用热启动Top-K采样策略，在测试时平衡一致性和多样性。
- 实验或效果：GRBO仅用10%训练数据提升安全性能超40%，保持行为真实性；Warm-K增强测试时行为一致性和反应性，无需重新训练。

## 摘要（原文）

> Learning interactive motion behaviors among multiple agents is a core challenge in autonomous driving. While imitation learning models generate realistic trajectories, they often inherit biases from datasets dominated by safe demonstrations, limiting robustness in safety-critical cases. Moreover, most studies rely on open-loop evaluation, overlooking compounding errors in closed-loop execution. We address these limitations with two complementary strategies. First, we propose Group Relative Behavior Optimization (GRBO), a reinforcement learning post-training method that fine-tunes pretrained behavior models via group relative advantage maximization with human regularization. Using only 10% of the training dataset, GRBO improves safety performance by over 40% while preserving behavioral realism. Second, we introduce Warm-K, a warm-started Top-K sampling strategy that balances consistency and diversity in motion selection. Our Warm-K method-based test-time scaling enhances behavioral consistency and reactivity at test time without retraining, mitigating covariate shift and reducing performance discrepancies. Demo videos are available in the supplementary material.

