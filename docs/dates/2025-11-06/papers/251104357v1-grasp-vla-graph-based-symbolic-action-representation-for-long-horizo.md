---
layout: default
title: GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies
---

# GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies
**arXiv**：[2511.04357v1](https://arxiv.org/abs/2511.04357) · [PDF](https://arxiv.org/pdf/2511.04357.pdf)  
**作者**：Maëlic Neau, Zoe Falomir, Paulo E. Santos, Anne-Gwenn Bosser, Cédric Buche  

**一句话要点**：提出GraSP-VLA框架，结合连续场景图与符号规划以解决长视野任务中VLA策略的规划限制

**关键词**：神经符号方法, 连续场景图, 符号动作表示, 长视野规划, VLA策略, 规划域生成

## 3 点简述
- 核心问题：VLA模型缺乏符号规划，AML方法泛化性差，限制长视野任务性能
- 方法要点：使用连续场景图生成符号表示，构建规划域并协调低层VLA策略
- 实验效果：在规划域生成和真实世界长视野任务中验证了框架有效性

## 摘要（原文）

> Deploying autonomous robots that can learn new skills from demonstrations is
> an important challenge of modern robotics. Existing solutions often apply
> end-to-end imitation learning with Vision-Language Action (VLA) models or
> symbolic approaches with Action Model Learning (AML). On the one hand, current
> VLA models are limited by the lack of high-level symbolic planning, which
> hinders their abilities in long-horizon tasks. On the other hand, symbolic
> approaches in AML lack generalization and scalability perspectives. In this
> paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that
> uses a Continuous Scene Graph representation to generate a symbolic
> representation of human demonstrations. This representation is used to generate
> new planning domains during inference and serves as an orchestrator for
> low-level VLA policies, scaling up the number of actions that can be reproduced
> in a row. Our results show that GraSP-VLA is effective for modeling symbolic
> representations on the task of automatic planning domain generation from
> observations. In addition, results on real-world experiments show the potential
> of our Continuous Scene Graph representation to orchestrate low-level VLA
> policies in long-horizon tasks.

