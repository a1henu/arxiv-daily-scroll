---
layout: default
title: Nightmare Dreamer: Dreaming About Unsafe States And Planning Ahead
---

# Nightmare Dreamer: Dreaming About Unsafe States And Planning Ahead
**arXiv**：[2601.04686v1](https://arxiv.org/abs/2601.04686) · [PDF](https://arxiv.org/pdf/2601.04686.pdf)  
**作者**：Oluwatosin Oseni, Shengjie Wang, Jun Zhu, Micah Corah  

**一句话要点**：提出Nightmare Dreamer模型，通过世界模型预测安全违规以解决强化学习在机器人控制中的安全问题

**关键词**：安全强化学习, 模型预测控制, 机器人控制, 世界模型, 安全违规预测

## 3 点简述
- 核心问题：强化学习在机器人控制中因安全保证不足而应用受限
- 方法要点：基于模型的安全强化学习算法，利用学习的世界模型预测潜在安全违规并规划动作
- 实验或效果：在Safety Gymnasium任务中，仅使用图像观测，安全违规接近零，效率提升约20倍

## 摘要（原文）

> Reinforcement Learning (RL) has shown remarkable success in real-world applications, particularly in robotics control. However, RL adoption remains limited due to insufficient safety guarantees. We introduce Nightmare Dreamer, a model-based Safe RL algorithm that addresses safety concerns by leveraging a learned world model to predict potential safety violations and plan actions accordingly. Nightmare Dreamer achieves nearly zero safety violations while maximizing rewards. Nightmare Dreamer outperforms model-free baselines on Safety Gymnasium tasks using only image observations, achieving nearly a 20x improvement in efficiency.

