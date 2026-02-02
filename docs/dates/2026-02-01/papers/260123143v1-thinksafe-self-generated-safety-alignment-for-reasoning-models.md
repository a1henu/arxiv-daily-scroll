---
layout: default
title: THINKSAFE: Self-Generated Safety Alignment for Reasoning Models
---

# THINKSAFE: Self-Generated Safety Alignment for Reasoning Models
**arXiv**：[2601.23143v1](https://arxiv.org/abs/2601.23143) · [PDF](https://arxiv.org/pdf/2601.23143.pdf)  
**作者**：Seanie Lee, Sangwoo Park, Yumin Choi, Gyeongman Kim, Minki Kang, Jihun Yun, Dongmin Park, Jongho Park, Sung Ju Hwang  

**一句话要点**：提出ThinkSafe框架，通过自生成安全对齐解决大型推理模型在强化学习优化中的安全退化问题。

**关键词**：大型推理模型, 安全对齐, 自生成学习, 拒绝引导, 微调优化, 分布偏移

## 3 点简述
- 大型推理模型在强化学习优化中过度追求合规性，导致安全机制受损，易受有害提示攻击。
- ThinkSafe利用轻量级拒绝引导，解锁模型潜在安全知识，自生成安全推理轨迹进行微调，避免外部教师蒸馏的分布偏移。
- 在DeepSeek-R1-Distill和Qwen3上实验显示，ThinkSafe显著提升安全性，同时保持推理能力，计算成本低于GRPO。

## 摘要（原文）

> Large reasoning models (LRMs) achieve remarkable performance by leveraging reinforcement learning (RL) on reasoning tasks to generate long chain-of-thought (CoT) reasoning. However, this over-optimization often prioritizes compliance, making models vulnerable to harmful prompts. To mitigate this safety degradation, recent approaches rely on external teacher distillation, yet this introduces a distributional discrepancy that degrades native reasoning. We propose ThinkSafe, a self-generated alignment framework that restores safety alignment without external teachers. Our key insight is that while compliance suppresses safety mechanisms, models often retain latent knowledge to identify harm. ThinkSafe unlocks this via lightweight refusal steering, guiding the model to generate in-distribution safety reasoning traces. Fine-tuning on these self-generated responses effectively realigns the model while minimizing distribution shift. Experiments on DeepSeek-R1-Distill and Qwen3 show ThinkSafe significantly improves safety while preserving reasoning proficiency. Notably, it achieves superior safety and comparable reasoning to GRPO, with significantly reduced computational cost. Code, models, and datasets are available at https://github.com/seanie12/ThinkSafe.git.

