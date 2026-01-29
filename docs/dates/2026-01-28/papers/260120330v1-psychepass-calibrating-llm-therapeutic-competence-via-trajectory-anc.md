---
layout: default
title: PsychePass: Calibrating LLM Therapeutic Competence via Trajectory-Anchored Tournaments
---

# PsychePass: Calibrating LLM Therapeutic Competence via Trajectory-Anchored Tournaments
**arXiv**：[2601.20330v1](https://arxiv.org/abs/2601.20330) · [PDF](https://arxiv.org/pdf/2601.20330.pdf)  
**作者**：Zhuang Chen, Dazhen Wan, Zhangkai Zheng, Guanqun Bi, Xiyao Xiao, Binghang Li, Minlie Huang  

**一句话要点**：提出PsychePass框架，通过轨迹锚定锦标赛校准大语言模型在心理健康咨询中的治疗能力。

**关键词**：大语言模型评估, 心理健康咨询, 轨迹锚定, 瑞士系统锦标赛, 强化学习, 治疗能力校准

## 3 点简述
- 核心问题：现有评估方法存在未锚定缺陷，导致过程漂移和标准漂移，难以可靠评估大语言模型的治疗能力。
- 方法要点：通过模拟中锚定交互轨迹，控制咨询过程以探测多方面能力；利用瑞士系统锦标赛进行动态成对战斗，生成稳健的Elo评分。
- 实验或效果：实验验证了PsychePass的有效性，其与人类专家判断具有强一致性，并能转化为可信奖励信号用于强化学习提升模型性能。

## 摘要（原文）

> While large language models show promise in mental healthcare, evaluating their therapeutic competence remains challenging due to the unstructured and longitudinal nature of counseling. We argue that current evaluation paradigms suffer from an unanchored defect, leading to two forms of instability: process drift, where unsteered client simulation wanders away from specific counseling goals, and standard drift, where static pointwise scoring lacks the stability for reliable judgment. To address this, we introduce Ps, a unified framework that calibrates the therapeutic competence of LLMs via trajectory-anchored tournaments. We first anchor the interaction trajectory in simulation, where clients precisely control the fluid consultation process to probe multifaceted capabilities. We then anchor the battle trajectory in judgments through an efficient Swiss-system tournament, utilizing dynamic pairwise battles to yield robust Elo ratings. Beyond ranking, we demonstrate that tournament trajectories can be transformed into credible reward signals, enabling on-policy reinforcement learning to enhance LLMs' performance. Extensive experiments validate the effectiveness of PsychePass and its strong consistency with human expert judgments.

