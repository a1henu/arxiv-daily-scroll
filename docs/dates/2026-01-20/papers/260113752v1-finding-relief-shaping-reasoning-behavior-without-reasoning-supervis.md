---
layout: default
title: Finding RELIEF: Shaping Reasoning Behavior without Reasoning Supervision via Belief Engineering
---

# Finding RELIEF: Shaping Reasoning Behavior without Reasoning Supervision via Belief Engineering
**arXiv**：[2601.13752v1](https://arxiv.org/abs/2601.13752) · [PDF](https://arxiv.org/pdf/2601.13752.pdf)  
**作者**：Chak Tou Leong, Dingwei Chen, Heming Xia, Qingyu Yin, Sunbowen Lee, Jian Wang, Wenjie Li  

**一句话要点**：提出RELIEF框架，通过信念工程塑造大型推理模型行为，无需推理监督。

**关键词**：大型推理模型, 信念工程, 无监督学习, 行为塑造, 推理忠实性

## 3 点简述
- 大型推理模型存在计算冗余或推理不忠实问题，现有方法依赖监督且成本高。
- 揭示模型具有潜在推理信念，通过logit探测捕获，并基于此提出RELIEF框架。
- 实验表明RELIEF在效率和忠实性任务上匹配或优于基线，训练成本更低。

## 摘要（原文）

> Large reasoning models (LRMs) have achieved remarkable success in complex problem-solving, yet they often suffer from computational redundancy or reasoning unfaithfulness. Current methods for shaping LRM behavior typically rely on reinforcement learning or fine-tuning with gold-standard reasoning traces, a paradigm that is both computationally expensive and difficult to scale. In this paper, we reveal that LRMs possess latent \textit{reasoning beliefs} that internally track their own reasoning traits, which can be captured through simple logit probing. Building upon this insight, we propose Reasoning Belief Engineering (RELIEF), a simple yet effective framework that shapes LRM behavior by aligning the model's self-concept with a target belief blueprint. Crucially, RELIEF completely bypasses the need for reasoning-trace supervision. It internalizes desired traits by fine-tuning on synthesized, self-reflective question-answering pairs that affirm the target belief. Extensive experiments on efficiency and faithfulness tasks demonstrate that RELIEF matches or outperforms behavior-supervised and preference-based baselines while requiring lower training costs. Further analysis validates that shifting a model's reasoning belief effectively shapes its actual behavior.

