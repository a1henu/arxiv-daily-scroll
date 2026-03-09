---
layout: default
title: Boosting deep Reinforcement Learning using pretraining with Logical Options
---

# Boosting deep Reinforcement Learning using pretraining with Logical Options
**arXiv**：[2603.06565v1](https://arxiv.org/abs/2603.06565) · [PDF](https://arxiv.org/pdf/2603.06565.pdf)  
**作者**：Zihan Ye, Phil Chau, Raban Emunds, Jannis Blüml, Cedric Derstroff, Quentin Delfosse, Oleg Arenz, Kristian Kersting  

**一句话要点**：提出混合分层强化学习方法，通过逻辑选项预训练解决深度强化学习中的短视奖励过度利用问题。

**关键词**：深度强化学习, 逻辑选项, 预训练策略, 混合分层强化学习, 长时程决策

## 3 点简述
- 核心问题：深度强化学习代理常因过度利用早期奖励信号而行为不匹配，难以实现长期目标导向。
- 方法要点：采用两阶段框架，结合符号逻辑选项预训练引导策略远离短期奖励循环，再通过环境交互精炼深度策略。
- 实验或效果：在长时程决策任务中，该方法优于神经、符号和神经符号基线，提升代理性能。

## 摘要（原文）

> Deep reinforcement learning agents are often misaligned, as they over-exploit early reward signals. Recently, several symbolic approaches have addressed these challenges by encoding sparse objectives along with aligned plans. However, purely symbolic architectures are complex to scale and difficult to apply to continuous settings. Hence, we propose a hybrid approach, inspired by humans' ability to acquire new skills. We use a two-stage framework that injects symbolic structure into neural-based reinforcement learning agents without sacrificing the expressivity of deep policies. Our method, called Hybrid Hierarchical RL (H^2RL), introduces a logical option-based pretraining strategy to steer the learning policy away from short-term reward loops and toward goal-directed behavior while allowing the final policy to be refined via standard environment interaction. Empirically, we show that this approach consistently improves long-horizon decision-making and yields agents that outperform strong neural, symbolic, and neuro-symbolic baselines.

