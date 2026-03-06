---
layout: default
title: $\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space
---

# $\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space
**arXiv**：[2603.04948v1](https://arxiv.org/abs/2603.04948) · [PDF](https://arxiv.org/pdf/2603.04948.pdf)  
**作者**：Peihao Wang, Ruisi Cai, Zhen Wang, Hongyuan Mei, Qiang Liu, Pan Li, Zhangyang Wang  

**一句话要点**：提出∇-Reasoner框架，通过测试时潜在空间梯度下降增强大语言模型推理能力

**关键词**：大语言模型推理, 测试时优化, 梯度下降, 可微分文本优化, 强化学习对齐

## 3 点简述
- 核心问题：现有推理时扩展方法依赖低效离散搜索或试错提示，优化在线策略受限
- 方法要点：集成可微分文本优化，利用梯度信号从似然和奖励模型精炼文本表示
- 实验或效果：在数学推理基准上准确率提升超20%，模型调用减少约10-40%

## 摘要（原文）

> Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

