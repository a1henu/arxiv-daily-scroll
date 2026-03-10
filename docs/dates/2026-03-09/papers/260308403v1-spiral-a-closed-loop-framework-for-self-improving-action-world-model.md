---
layout: default
title: SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents
---

# SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents
**arXiv**：[2603.08403v1](https://arxiv.org/abs/2603.08403) · [PDF](https://arxiv.org/pdf/2603.08403.pdf)  
**作者**：Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  

**一句话要点**：提出SPIRAL闭环框架，通过反思规划代理实现可控长视频生成，解决语义对齐与时间一致性问题。

**关键词**：可控视频生成, 闭环世界模型, 反思规划代理, 语义动作条件, 长视频生成, 强化学习优化

## 3 点简述
- 现有单次视频生成模型存在语义不完整和时间漂移问题，SPIRAL引入闭环思维-行动-反思过程。
- 框架包含PlanAgent分解动作和CriticAgent评估反馈，支持强化学习优化以提升语义对齐。
- 实验在ActWM-Bench和主流基准上验证了SPIRAL的有效性，带来一致性能提升。

## 摘要（原文）

> We introduce SPIRAL, a self-improving planning and iterative reflective action world modeling closed-loop framework that enables controllable long-horizon video generation conditioned on high-level semantic actions. Existing one-shot video generation models operate in open-loop, often resulting in incomplete action execution, weak semantic grounding, and temporal drift. SPIRAL formulates ActWM as a closed-loop think-act-reflect process, where generation proceeds step by step under explicit planning and feedback. A PlanAgent decomposes abstract actions into object-centric sub-actions, while a CriticAgent evaluates intermediate results and guides iterative refinement with long-horizon memory. This closed-loop design naturally supports RL evolving optimization, improving semantic alignment and temporal consistency over extended horizons. We further introduce the ActWM-Dataset and ActWM-Bench for training and evaluation. Experiments across multiple TI2V backbones demonstrate consistent gains on ActWM-Bench and mainstream video generation benchmarks, validating SPIRAL's effectiveness.

