---
layout: default
title: Breaking the Safety-Capability Tradeoff: Reinforcement Learning with Verifiable Rewards Maintains Safety Guardrails in LLMs
---

# Breaking the Safety-Capability Tradeoff: Reinforcement Learning with Verifiable Rewards Maintains Safety Guardrails in LLMs
**arXiv**：[2511.21050v1](https://arxiv.org/abs/2511.21050) · [PDF](https://arxiv.org/pdf/2511.21050.pdf)  
**作者**：Dongkyu Derek Cho, Huan Song, Arijit Ghosh Chowdhury, Haotian An, Yawei Wang, Rohit Thekkanal, Negin Sokhandan, Sharlina Keshava, Hannah Marlowe  

**一句话要点**：提出可验证奖励强化学习以解决大语言模型安全与能力权衡问题

**关键词**：大语言模型, 强化学习, 安全对齐, 可验证奖励, KL约束优化, 安全基准

## 3 点简述
- 核心问题：微调大语言模型时存在安全与能力权衡，标准方法如SFT和RLHF会降低安全对齐
- 方法要点：使用可验证奖励强化学习，在KL约束优化下理论上消除安全退化
- 实验或效果：在五个对抗安全基准上验证，RLVR可同时提升推理能力并维持安全护栏

## 摘要（原文）

> Fine-tuning large language models (LLMs) for downstream tasks typically exhibit a fundamental safety-capability tradeoff, where improving task performance degrades safety alignment even on benign datasets. This degradation persists across standard approaches including supervised finetuning (SFT) and reinforcement learning from human feedback (RLHF). While reinforcement learning with verifiable rewards (RLVR) has emerged as a promising alternative that optimizes models on objectively measurable tasks, its safety implications remain unexplored. We present the first comprehensive theoretical and empirical analysis of safety properties in RLVR. Theoretically, we derive upper bounds on safety drift under KL-constrained optimization and prove conditions under which safety degradation is eliminated. Empirically, we conduct extensive experiments across five adversarial safety benchmarks, demonstrating that RLVR can simultaneously enhance reasoning capabilities while maintaining or improving safety guardrails. Our comprehensive ablation studies examine the effects of optimization algorithms, model scale, and task domains. Our findings challenge the prevailing assumption of an inevitable safety capability trade-off, and establish that a specific training methodology can achieve both objectives simultaneously, providing insights for the safe deployment of reasoning-capable LLMs.

