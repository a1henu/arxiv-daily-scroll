---
layout: default
title: Reinforcement Unlearning via Group Relative Policy Optimization
---

# Reinforcement Unlearning via Group Relative Policy Optimization
**arXiv**：[2601.20568v1](https://arxiv.org/abs/2601.20568) · [PDF](https://arxiv.org/pdf/2601.20568.pdf)  
**作者**：Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci  

**一句话要点**：提出PURGE方法，基于Group Relative Policy Optimization框架，解决LLM遗忘敏感数据时的泄露与性能下降问题。

**关键词**：强化学习遗忘, Group Relative Policy Optimization, LLM合规性, 可验证遗忘, 内在奖励信号, RWKU基准

## 3 点简述
- 核心问题：LLM预训练中记忆敏感数据，需合规遗忘但现有方法易泄露数据或牺牲模型性能。
- 方法要点：PURGE使用内在奖励信号惩罚提及禁止概念，将遗忘构建为可验证任务，实现安全一致遗忘。
- 实验或效果：在RWKU基准上，遗忘效果达11%，保留98%原始效用，提升流畅度5.48%和对抗鲁棒性12.02%。

## 摘要（原文）

> During pretraining, LLMs inadvertently memorize sensitive or copyrighted data, posing significant compliance challenges under legal frameworks like the GDPR and the EU AI Act. Fulfilling these mandates demands techniques that can remove information from a deployed model without retraining from scratch. Existing unlearning approaches attempt to address this need, but often leak the very data they aim to erase, sacrifice fluency and robustness, or depend on costly external reward models. We introduce PURGE (Policy Unlearning through Relative Group Erasure), a novel method grounded in the Group Relative Policy Optimization framework that formulates unlearning as a verifiable problem. PURGE uses an intrinsic reward signal that penalizes any mention of forbidden concepts, allowing safe and consistent unlearning. Our approach reduces token usage per target by up to a factor of 46 compared with SotA methods, while improving fluency by 5.48 percent and adversarial robustness by 12.02 percent over the base model. On the Real World Knowledge Unlearning (RWKU) benchmark, PURGE achieves 11 percent unlearning effectiveness while preserving 98 percent of original utility. PURGE shows that framing LLM unlearning as a verifiable task, enables more reliable, efficient, and scalable forgetting, suggesting a promising new direction for unlearning research that combines theoretical guarantees, improved safety, and practical deployment efficiency.

