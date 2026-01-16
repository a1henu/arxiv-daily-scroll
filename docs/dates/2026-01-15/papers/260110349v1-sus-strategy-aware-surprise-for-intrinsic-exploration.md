---
layout: default
title: SuS: Strategy-aware Surprise for Intrinsic Exploration
---

# SuS: Strategy-aware Surprise for Intrinsic Exploration
**arXiv**：[2601.10349v1](https://arxiv.org/abs/2601.10349) · [PDF](https://arxiv.org/pdf/2601.10349.pdf)  
**作者**：Mark Kashirskiy, Ilya Makarov  

**一句话要点**：提出策略感知惊喜以增强强化学习探索，应用于数学推理任务。

**关键词**：强化学习探索, 内在动机, 策略感知, 数学推理, 大型语言模型

## 3 点简述
- 核心问题：传统好奇心方法仅依赖状态预测误差，探索效率受限。
- 方法要点：引入策略稳定性和策略惊喜，通过预测不匹配作为新颖性信号。
- 实验效果：在大型语言模型上显著提升准确率和解决方案多样性。

## 摘要（原文）

> We propose Strategy-aware Surprise (SuS), a novel intrinsic motivation framework that uses pre-post prediction mismatch as a novelty signal for exploration in reinforcement learning. Unlike traditional curiosity-driven methods that rely solely on state prediction error, SuS introduces two complementary components: Strategy Stability (SS) and Strategy Surprise (SuS). SS measures consistency in behavioral strategy across temporal steps, while SuS captures unexpected outcomes relative to the agent's current strategy representation. Our combined reward formulation leverages both signals through learned weighting coefficients. We evaluate SuS on mathematical reasoning tasks using large language models, demonstrating significant improvements in both accuracy and solution diversity. Ablation studies confirm that removing either component results in at least 10% performance degradation, validating the synergistic nature of our approach. SuS achieves 17.4% improvement in Pass@1 and 26.4% improvement in Pass@5 compared to baseline methods, while maintaining higher strategy diversity throughout training.

