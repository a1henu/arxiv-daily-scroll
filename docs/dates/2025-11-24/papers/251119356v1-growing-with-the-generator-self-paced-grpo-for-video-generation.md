---
layout: default
title: Growing with the Generator: Self-paced GRPO for Video Generation
---

# Growing with the Generator: Self-paced GRPO for Video Generation
**arXiv**：[2511.19356v1](https://arxiv.org/abs/2511.19356) · [PDF](https://arxiv.org/pdf/2511.19356.pdf)  
**作者**：Rui Li, Yuanzhi Liang, Ziqi Ni, Haibing Huang, Chi Zhang, Xuelong Li  

**一句话要点**：提出自步GRPO以解决视频生成中静态奖励模型导致的分布偏差和优化不稳定问题

**关键词**：视频生成, 强化学习, 奖励模型, 策略优化, 自步学习, 语义对齐

## 3 点简述
- 核心问题：静态奖励模型在训练中行为固定，导致分布偏差、奖励饱和和优化不稳定
- 方法要点：引入渐进奖励机制，随生成质量提升从视觉保真度转向时间一致性和语义对齐
- 实验或效果：在VBench上验证，相比静态奖励GRPO，视觉质量和语义对齐均提升

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) has emerged as a powerful reinforcement learning paradigm for post-training video generation models. However, existing GRPO pipelines rely on static, fixed-capacity reward models whose evaluation behavior is frozen during training. Such rigid rewards introduce distributional bias, saturate quickly as the generator improves, and ultimately limit the stability and effectiveness of reinforcement-based alignment. We propose Self-Paced GRPO, a competence-aware GRPO framework in which reward feedback co-evolves with the generator. Our method introduces a progressive reward mechanism that automatically shifts its emphasis from coarse visual fidelity to temporal coherence and fine-grained text-video semantic alignment as generation quality increases. This self-paced curriculum alleviates reward-policy mismatch, mitigates reward exploitation, and yields more stable optimization. Experiments on VBench across multiple video generation backbones demonstrate consistent improvements in both visual quality and semantic alignment over GRPO baselines with static rewards, validating the effectiveness and generality of Self-Paced GRPO.

