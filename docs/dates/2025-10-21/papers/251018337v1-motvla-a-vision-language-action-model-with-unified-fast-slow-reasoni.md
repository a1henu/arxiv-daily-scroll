---
layout: default
title: MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning
---

# MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning
**arXiv**：[2510.18337v1](https://arxiv.org/abs/2510.18337) · [PDF](https://arxiv.org/pdf/2510.18337.pdf)  
**作者**：Wenhui Huang, Changhe Chen, Han Qi, Chen Lv, Yilun Du, Heng Yang  

**一句话要点**：提出MoTVLA模型，通过统一快慢推理解决视觉语言动作任务中的语言引导与延迟问题。

**关键词**：视觉语言动作模型, 混合变换器, 快慢推理, 机器人学习, 语言引导性, 策略执行效率

## 3 点简述
- 现有方法语言引导性差或推理延迟高，限制机器人开放世界泛化。
- MoTVLA结合通用视觉语言模型与领域专家，实现快慢推理与行为策略学习。
- 实验在NLP基准、机器人仿真和真实世界验证其推理与任务性能优越性。

## 摘要（原文）

> Integrating visual-language instructions into visuomotor policies is gaining
> momentum in robot learning for enhancing open-world generalization. Despite
> promising advances, existing approaches face two challenges: limited language
> steerability when no generated reasoning is used as a condition, or significant
> inference latency when reasoning is incorporated.In this work, we introduce
> MoTVLA, a mixture-of-transformers (MoT)-based vision-language-action (VLA)
> model that integrates fast-slow unified reasoning with behavior policy
> learning. MoTVLA preserves the general intelligence of pre-trained VLMs
> (serving as the generalist) for tasks such as perception, scene understanding,
> and semantic planning, while incorporating a domain expert, a second
> transformer that shares knowledge with the pretrained VLM, to generate
> domain-specific fast reasoning (e.g., robot motion decomposition), thereby
> improving policy execution efficiency. By conditioning the action expert on
> decomposed motion instructions, MoTVLA can learn diverse behaviors and
> substantially improve language steerability. Extensive evaluations across
> natural language processing benchmarks, robotic simulation environments, and
> real-world experiments confirm the superiority of MoTVLA in both fast-slow
> reasoning and manipulation task performance.

