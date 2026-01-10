---
layout: default
title: GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
---

# GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
**arXiv**：[2601.05242v1](https://arxiv.org/abs/2601.05242) · [PDF](https://arxiv.org/pdf/2601.05242.pdf)  
**作者**：Shih-Yang Liu, Xin Dong, Ximing Lu, Shizhe Diao, Peter Belcak, Mingjie Liu, Min-Hung Chen, Hongxu Yin, Yu-Chiang Frank Wang, Kwang-Ting Cheng, Yejin Choi, Jan Kautz, Pavlo Molchanov  

**一句话要点**：提出GDPO以解决多奖励强化学习中归一化导致训练信号退化的问题

**关键词**：多奖励强化学习, 策略优化, 归一化方法, 训练稳定性, 语言模型对齐

## 3 点简述
- 核心问题：GRPO在多奖励设置下归一化不同奖励组合，导致优势值趋同，降低训练信号分辨率，影响收敛。
- 方法要点：GDPO通过解耦个体奖励的归一化，保留相对差异，提升多奖励优化准确性和训练稳定性。
- 实验或效果：在工具调用、数学推理和编码推理任务中，GDPO在正确性和约束遵循指标上均优于GRPO。

## 摘要（原文）

> As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors. However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure. We then introduce Group reward-Decoupled Normalization Policy Optimization (GDPO), a new policy optimization method to resolve these issues by decoupling the normalization of individual rewards, more faithfully preserving their relative differences and enabling more accurate multi-reward optimization, along with substantially improved training stability. We compare GDPO with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length). Across all settings, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.

