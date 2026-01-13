---
layout: default
title: Failure-Aware RL: Reliable Offline-to-Online Reinforcement Learning with Self-Recovery for Real-World Manipulation
---

# Failure-Aware RL: Reliable Offline-to-Online Reinforcement Learning with Self-Recovery for Real-World Manipulation
**arXiv**：[2601.07821v1](https://arxiv.org/abs/2601.07821) · [PDF](https://arxiv.org/pdf/2601.07821.pdf)  
**作者**：Huanyu Li, Kun Lei, Sheng Zang, Kaizhe Hu, Yongyuan Liang, Bo An, Xiaoli Li, Huazhe Xu  

**一句话要点**：提出失败感知离线到在线强化学习范式，以减少现实世界机器人操作中需干预的失败。

**关键词**：离线到在线强化学习, 失败感知学习, 机器人操作, 安全强化学习, 世界模型, 恢复策略

## 3 点简述
- 核心问题：现实世界探索中需干预的失败（如机器人打翻水或打碎玻璃）阻碍强化学习后训练的实际部署。
- 方法要点：集成基于世界模型的安全评论家和离线训练的恢复策略，以在线探索时预防失败。
- 实验或效果：在现实世界强化学习后训练中，平均减少73.1%需干预的失败并提升11.3%性能。

## 摘要（原文）

> Post-training algorithms based on deep reinforcement learning can push the limits of robotic models for specific objectives, such as generalizability, accuracy, and robustness. However, Intervention-requiring Failures (IR Failures) (e.g., a robot spilling water or breaking fragile glass) during real-world exploration happen inevitably, hindering the practical deployment of such a paradigm. To tackle this, we introduce Failure-Aware Offline-to-Online Reinforcement Learning (FARL), a new paradigm minimizing failures during real-world reinforcement learning. We create FailureBench, a benchmark that incorporates common failure scenarios requiring human intervention, and propose an algorithm that integrates a world-model-based safety critic and a recovery policy trained offline to prevent failures during online exploration. Extensive simulation and real-world experiments demonstrate the effectiveness of FARL in significantly reducing IR Failures while improving performance and generalization during online reinforcement learning post-training. FARL reduces IR Failures by 73.1% while elevating performance by 11.3% on average during real-world RL post-training. Videos and code are available at https://failure-aware-rl.github.io.

