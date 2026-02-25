---
layout: default
title: CAMEL: Confidence-Gated Reflection for Reward Modeling
---

# CAMEL: Confidence-Gated Reflection for Reward Modeling
**arXiv**：[2602.20670v1](https://arxiv.org/abs/2602.20670) · [PDF](https://arxiv.org/pdf/2602.20670.pdf)  
**作者**：Zirui Zhu, Hailun Xu, Yang Luo, Yong Liu, Kanchan Sarkar, Kun Xu, Yang You  

**一句话要点**：提出CAMEL框架，通过置信度门控反射提升奖励模型效率与性能

**关键词**：奖励建模, 置信度门控, 反射机制, 强化学习, 大语言模型对齐

## 3 点简述
- 核心问题：现有奖励模型在标量判别与生成判断间存在效率与可解释性权衡
- 方法要点：基于log-probability margin的置信度门控，选择性反射低置信度实例
- 实验或效果：在三个基准上平均准确率达82.9%，以14B参数超越70B模型

## 摘要（原文）

> Reward models play a fundamental role in aligning large language models with human preferences. Existing methods predominantly follow two paradigms: scalar discriminative preference models, which are efficient but lack interpretability, and generative judging models, which offer richer reasoning at the cost of higher computational overhead. We observe that the log-probability margin between verdict tokens strongly correlates with prediction correctness, providing a reliable proxy for instance difficulty without additional inference cost. Building on this insight, we propose CAMEL, a confidence-gated reflection framework that performs a lightweight single-token preference decision first and selectively invokes reflection only for low-confidence instances. To induce effective self-correction, we train the model via reinforcement learning with counterfactual prefix augmentation, which exposes the model to diverse initial verdicts and encourages genuine revision. Empirically, CAMEL achieves state-of-the-art performance on three widely used reward-model benchmarks with 82.9% average accuracy, surpassing the best prior model by 3.2% and outperforming 70B-parameter models using only 14B parameters, while establishing a strictly better accuracy-efficiency Pareto frontier.

