---
layout: default
title: World-Model-Augmented Web Agents with Action Correction
---

# World-Model-Augmented Web Agents with Action Correction
**arXiv**：[2602.15384v1](https://arxiv.org/abs/2602.15384) · [PDF](https://arxiv.org/pdf/2602.15384.pdf)  
**作者**：Zhouzhou Shen, Xueyu Hu, Xiyun Li, Tianqing Fang, Juncheng Li, Shengyu Zhang  

**一句话要点**：提出WAC网络代理，通过世界模型协作与动作校正解决网络任务执行中的推理与风险感知问题。

**关键词**：网络代理, 世界模型, 动作校正, 多模型协作, 风险感知, 任务执行

## 3 点简述
- 当前网络代理因预测环境变化受限，难以推理合理动作且缺乏风险意识，易导致任务失败。
- WAC采用多模型协作，动作模型咨询世界模型获取策略指导，并基于状态转移知识生成候选动作。
- 实验显示WAC在VisualWebArena和Online-Mind2Web上分别提升1.8%和1.3%的绝对性能增益。

## 摘要（原文）

> Web agents based on large language models have demonstrated promising capability in automating web tasks. However, current web agents struggle to reason out sensible actions due to the limitations of predicting environment changes, and might not possess comprehensive awareness of execution risks, prematurely performing risky actions that cause losses and lead to task failure. To address these challenges, we propose WAC, a web agent that integrates model collaboration, consequence simulation, and feedback-driven action refinement. To overcome the cognitive isolation of individual models, we introduce a multi-agent collaboration process that enables an action model to consult a world model as a web-environment expert for strategic guidance; the action model then grounds these suggestions into executable actions, leveraging prior knowledge of environmental state transition dynamics to enhance candidate action proposal. To achieve risk-aware resilient task execution, we introduce a two-stage deduction chain. A world model, specialized in environmental state transitions, simulates action outcomes, which a judge model then scrutinizes to trigger action corrective feedback when necessary. Experiments show that WAC achieves absolute gains of 1.8% on VisualWebArena and 1.3% on Online-Mind2Web.

