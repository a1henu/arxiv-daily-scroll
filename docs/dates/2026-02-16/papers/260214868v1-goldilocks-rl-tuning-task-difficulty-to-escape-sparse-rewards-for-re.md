---
layout: default
title: Goldilocks RL: Tuning Task Difficulty to Escape Sparse Rewards for Reasoning
---

# Goldilocks RL: Tuning Task Difficulty to Escape Sparse Rewards for Reasoning
**arXiv**：[2602.14868v1](https://arxiv.org/abs/2602.14868) · [PDF](https://arxiv.org/pdf/2602.14868.pdf)  
**作者**：Ilia Mahrooghi, Aryo Lotfi, Emmanuel Abbe  

**一句话要点**：提出Goldilocks数据采样策略以解决强化学习中稀疏奖励导致的样本效率低下问题

**关键词**：强化学习, 稀疏奖励, 数据采样, 教师-学生模型, 推理能力, 样本效率

## 3 点简述
- 核心问题：强化学习在大型语言模型推理中依赖稀疏奖励，导致样本效率低下
- 方法要点：教师模型预测问题难度，动态选择适合学生模型能力的问题进行训练
- 实验或效果：在OpenMathReasoning数据集上，相同计算预算下提升GRPO训练模型的性能

## 摘要（原文）

> Reinforcement learning has emerged as a powerful paradigm for unlocking reasoning capabilities in large language models. However, relying on sparse rewards makes this process highly sample-inefficient, as models must navigate vast search spaces with minimal feedback. While classic curriculum learning aims to mitigate this by ordering data based on complexity, the right ordering for a specific model is often unclear. To address this, we propose Goldilocks, a novel teacher-driven data sampling strategy that aims to predict each question's difficulty for the student model. The teacher model selects questions of appropriate difficulty for the student model, i.e., questions that are neither too easy nor too hard (Goldilocks principle), while training the student with GRPO. By leveraging the student's performance on seen samples, the teacher continuously adapts to the student's evolving abilities. On OpenMathReasoning dataset, Goldilocks data sampling improves the performance of models trained with standard GRPO under the same compute budget.

