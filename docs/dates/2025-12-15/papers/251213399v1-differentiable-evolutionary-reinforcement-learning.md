---
layout: default
title: Differentiable Evolutionary Reinforcement Learning
---

# Differentiable Evolutionary Reinforcement Learning
**arXiv**：[2512.13399v1](https://arxiv.org/abs/2512.13399) · [PDF](https://arxiv.org/pdf/2512.13399.pdf)  
**作者**：Sitao Cheng, Tianle Li, Xuhan Huang, Xunjian Yin, Difan Zou  

**一句话要点**：提出可微分进化强化学习框架，以自动发现最优奖励信号，解决复杂推理任务中奖励函数设计难题。

**关键词**：可微分进化强化学习, 奖励函数优化, 双层框架, 元优化, 复杂推理任务, 分布外泛化

## 3 点简述
- 核心问题：强化学习中奖励函数设计困难，现有进化方法忽略奖励结构与任务性能的因果关系。
- 方法要点：采用双层框架，通过可微分元优化，利用内循环策略验证性能更新元优化器，近似任务成功的元梯度。
- 实验或效果：在机器人、科学模拟和数学推理领域验证，在ALFWorld和ScienceWorld上达到最先进性能，尤其在分布外场景表现突出。

## 摘要（原文）

> The design of effective reward functions presents a central and often arduous challenge in reinforcement learning (RL), particularly when developing autonomous agents for complex reasoning tasks. While automated reward optimization approaches exist, they typically rely on derivative-free evolutionary heuristics that treat the reward function as a black box, failing to capture the causal relationship between reward structure and task performance. To bridge this gap, we propose Differentiable Evolutionary Reinforcement Learning (DERL), a bilevel framework that enables the autonomous discovery of optimal reward signals. In DERL, a Meta-Optimizer evolves a reward function (i.e., Meta-Reward) by composing structured atomic primitives, guiding the training of an inner-loop policy. Crucially, unlike previous evolution, DERL is differentiable in its metaoptimization: it treats the inner-loop validation performance as a signal to update the Meta-Optimizer via reinforcement learning. This allows DERL to approximate the "meta-gradient" of task success, progressively learning to generate denser and more actionable feedback. We validate DERL across three distinct domains: robotic agent (ALFWorld), scientific simulation (ScienceWorld), and mathematical reasoning (GSM8k, MATH). Experimental results show that DERL achieves state-of-the-art performance on ALFWorld and ScienceWorld, significantly outperforming methods relying on heuristic rewards, especially in out-of-distribution scenarios. Analysis of the evolutionary trajectory demonstrates that DERL successfully captures the intrinsic structure of tasks, enabling selfimproving agent alignment without human intervention.

