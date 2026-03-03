---
layout: default
title: Surgical Post-Training: Cutting Errors, Keeping Knowledge
---

# Surgical Post-Training: Cutting Errors, Keeping Knowledge
**arXiv**：[2603.01683v1](https://arxiv.org/abs/2603.01683) · [PDF](https://arxiv.org/pdf/2603.01683.pdf)  
**作者**：Wenye Lin, Kai Han  

**一句话要点**：提出Surgical Post-Training以高效优化大语言模型推理能力并避免灾难性遗忘

**关键词**：大语言模型后训练, 灾难性遗忘, 直接偏好优化, 推理优化, 数据校正, 二元分类目标

## 3 点简述
- 核心问题：大语言模型后训练中效率与灾难性遗忘的权衡，现有方法忽视DPO奖励估计的隐式正则化作用
- 方法要点：SPoT包括数据校正管道和基于奖励的二元交叉熵目标，将推理正确性视为二元分类问题
- 实验或效果：仅用4k校正数学数据对，Qwen3-8B在领域内外任务平均准确率提升6.2%，训练时间28分钟

## 摘要（原文）

> Enhancing the reasoning capabilities of Large Language Models (LLMs) via post-training is often constrained by the trade-off between efficiency and catastrophic forgetting. While prior research emphasizes the role of on-policy data in mitigating forgetting, we uncover--and validate both theoretically and empirically--an overlooked yet critical mechanism: the implicit regularization inherent in Direct Preference Optimization's (DPO) reward estimate. This motivates our Surgical Post-Training (SPoT), a new paradigm designed to optimize reasoning efficiently while preserving learned prior knowledge. SPoT consists of: (1) a data rectification pipeline that employs an Oracle to surgically correct erroneous steps via minimal edits, generating data proximal to the model's distribution; and (2) a reward-based binary cross-entropy objective. Unlike the relative ranking in DPO, this objective treats reasoning correctness as a binary classification problem, enforcing decoupled supervision signals. Empirically, with only 4k rectified math data pairs, SPoT improves Qwen3-8B's accuracy by 6.2% on average across in-domain and OOD tasks, requiring merely 28 minutes of training on 8x H800 GPUs. Code: https://github.com/Visual-AI/SPoT

