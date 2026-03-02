---
layout: default
title: Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking
---

# Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking
**arXiv**：[2602.24143v1](https://arxiv.org/abs/2602.24143) · [PDF](https://arxiv.org/pdf/2602.24143.pdf)  
**作者**：David Emukpere, Romain Deffayet, Jean-Michel Renders  

**一句话要点**：提出多物体拾取研究以诊断视觉-语言动作策略的受限泛化问题

**关键词**：视觉-语言动作策略, 多物体拾取, 泛化诊断, 操纵基准, 技能解耦, 指令跟随

## 3 点简述
- 核心问题：视觉-语言动作策略的性能是否源于鲁棒的语言-物体关联，还是依赖训练分布中的物体-位置相关性。
- 方法要点：通过控制多物体拾取实验，逐步增加物体放置变异性，评估打破熟悉关联的保留配对。
- 实验或效果：发现操纵技能获取与指令跟随解耦，建议用任务阶梯和分解指标增强基准测试。

## 摘要（原文）

> Vision-language action (VLA) policies often report strong manipulation benchmark performance with relatively few demonstrations, but it remains unclear whether this reflects robust language-to-object grounding or reliance on object--location correlations that do not transfer beyond the training distribution. We present a controlled multi-object picking study that progressively increases object placement variability up to full workspace randomization and evaluates held-out object--location pairings that break familiar associations without increasing spatial difficulty. Across these stress tests and data scaling, we find that for representative VLA policies, including SmolVLA and $π_{0.5}$, execution of the manipulation primitive remains substantially more reliable than instruction-conditioned task success in harder regimes, suggesting that manipulation skill acquisition is decoupled from instruction following. We recommend augmenting manipulation benchmarks with task ladders and decomposed metrics that separately measure primitive execution and instruction-conditioned success to better diagnose instruction-grounded generalization.

