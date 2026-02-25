---
layout: default
title: SibylSense: Adaptive Rubric Learning via Memory Tuning and Adversarial Probing
---

# SibylSense: Adaptive Rubric Learning via Memory Tuning and Adversarial Probing
**arXiv**：[2602.20751v1](https://arxiv.org/abs/2602.20751) · [PDF](https://arxiv.org/pdf/2602.20751.pdf)  
**作者**：Yifei Xu, Guilherme Potje, Shivam Shandilya, Tiancheng Yuan, Leonardo de Oliveira Nunes, Rakshanda Agarwal, Saeid Asgari, Adam Atkinson, Emre Kıcıman, Songwu Lu, Ranveer Chandra, Tusher Chakraborty  

**一句话要点**：提出SibylSense方法，通过记忆调优和对抗探测自适应学习评分标准，以解决开放生成任务中奖励对齐和鲁棒性问题。

**关键词**：开放生成任务, 奖励对齐, 自适应学习, 记忆调优, 对抗探测, 强化学习后训练

## 3 点简述
- 核心问题：开放生成任务中，设计对齐且鲁棒的奖励困难，现有评分标准构建方法成本高、浅层或不一致，易导致奖励黑客攻击。
- 方法要点：基于冻结评分标准生成器，通过可调记忆库存储已验证评分项，结合验证器奖励和对抗策略更新，自适应学习新质量维度。
- 实验或效果：在两项开放任务中，SibylSense生成更具区分性的评分标准，提升下游强化学习性能，优于静态和非自适应基线。

## 摘要（原文）

> Designing aligned and robust rewards for open-ended generation remains a key barrier to RL post-training. Rubrics provide structured, interpretable supervision, but scaling rubric construction is difficult: expert rubrics are costly, prompted rubrics are often superficial or inconsistent, and fixed-pool discriminative rubrics can saturate and drift, enabling reward hacking. We present SibylSense, an inference-time learning approach that adapts a frozen rubric generator through a tunable memory bank of validated rubric items. Memory is updated via verifier-based item rewards measured by reference-candidate answer discriminative gaps from a handful of examples. SibylSense alternates memory tuning with a rubric-adversarial policy update that produces rubric-satisfying candidate answers, shrinking discriminative gaps and driving the rubric generator to capture new quality dimensions. Experiments on two open-ended tasks show that SibylSense yields more discriminative rubrics and improves downstream RL performance over static and non-adaptive baselines.

