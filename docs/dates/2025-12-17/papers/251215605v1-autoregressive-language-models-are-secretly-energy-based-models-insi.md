---
layout: default
title: Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction
---

# Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction
**arXiv**：[2512.15605v1](https://arxiv.org/abs/2512.15605) · [PDF](https://arxiv.org/pdf/2512.15605.pdf)  
**作者**：Mathieu Blondel, Michael E. Sander, Germain Vivier-Ardisson, Tianlin Liu, Vincent Roulet  

**一句话要点**：建立自回归模型与能量模型在函数空间的双射，揭示其与软贝尔曼方程的联系及前瞻能力

**关键词**：自回归模型, 能量模型, 函数空间双射, 软贝尔曼方程, 蒸馏误差界, 前瞻能力

## 3 点简述
- 核心问题：自回归模型与能量模型在大型语言模型中的统一视图及前瞻能力机制
- 方法要点：基于概率链式法则建立双射，推导监督学习等价性及蒸馏误差界
- 实验或效果：理论分析提供自回归模型规划能力的见解，未提及具体实验

## 摘要（原文）

> Autoregressive models (ARMs) currently constitute the dominant paradigm for large language models (LLMs). Energy-based models (EBMs) represent another class of models, which have historically been less prevalent in LLM development, yet naturally characterize the optimal policy in post-training alignment. In this paper, we provide a unified view of these two model classes. Taking the chain rule of probability as a starting point, we establish an explicit bijection between ARMs and EBMs in function space, which we show to correspond to a special case of the soft Bellman equation in maximum entropy reinforcement learning. Building upon this bijection, we derive the equivalence between supervised learning of ARMs and EBMs. Furthermore, we analyze the distillation of EBMs into ARMs by providing theoretical error bounds. Our results provide insights into the ability of ARMs to plan ahead, despite being based on the next-token prediction paradigm.

