---
layout: default
title: The hidden risks of temporal resampling in clinical reinforcement learning
---

# The hidden risks of temporal resampling in clinical reinforcement learning
**arXiv**：[2602.06603v1](https://arxiv.org/abs/2602.06603) · [PDF](https://arxiv.org/pdf/2602.06603.pdf)  
**作者**：Thomas Frost, Hrisheekesh Vaidya, Steve Harris  

**一句话要点**：揭示临床强化学习中时间重采样的隐藏风险，强调处理不规则时序的必要性

**关键词**：离线强化学习, 临床决策, 时间重采样, 模型安全性, 离策略评估

## 3 点简述
- 核心问题：离线强化学习在医疗中常将患者数据聚合到固定时间间隔，影响模型安全性和有效性。
- 方法要点：通过网格世界导航任务和糖尿病模拟器，分析时间重采样导致性能下降的三种机制。
- 实验或效果：发现标准离策略评估指标可能无法检测性能下降，突显当前医疗ORL流程的根本风险。

## 摘要（原文）

> Offline reinforcement learning (ORL) has shown potential for improving decision-making in healthcare. However, contemporary research typically aggregates patient data into fixed time intervals, simplifying their mapping to standard ORL frameworks. The impact of these temporal manipulations on model safety and efficacy remains poorly understood. In this work, using both a gridworld navigation task and the UVA/Padova clinical diabetes simulator, we demonstrate that temporal resampling significantly degrades the performance of offline reinforcement learning algorithms during live deployment. We propose three mechanisms that drive this failure: (i) the generation of counterfactual trajectories, (ii) the distortion of temporal expectations, and (iii) the compounding of generalisation errors. Crucially, we find that standard off-policy evaluation metrics can fail to detect these drops in performance. Our findings reveal a fundamental risk in current healthcare ORL pipelines and emphasise the need for methods that explicitly handle the irregular timing of clinical decision-making.

