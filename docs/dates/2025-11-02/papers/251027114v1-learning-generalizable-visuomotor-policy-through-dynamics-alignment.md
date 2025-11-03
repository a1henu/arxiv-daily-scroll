---
layout: default
title: Learning Generalizable Visuomotor Policy through Dynamics-Alignment
---

# Learning Generalizable Visuomotor Policy through Dynamics-Alignment
**arXiv**：[2510.27114v1](https://arxiv.org/abs/2510.27114) · [PDF](https://arxiv.org/pdf/2510.27114.pdf)  
**作者**：Dohyeok Lee, Jung Min Lee, Munkyung Kim, Seokhun Ju, Jin Woo Koo, Kyungjae Lee, Dohyeong Kim, TaeHyun Cho, Jungwoo Lee  

**一句话要点**：提出动态对齐流匹配策略以提升机器人视觉运动策略的泛化能力

**关键词**：机器人学习, 行为克隆, 动态预测, 策略学习, 泛化能力, 视觉运动策略

## 3 点简述
- 行为克隆方法泛化性差，受限于专家演示数据不足
- 集成动态预测与策略学习，通过相互反馈实现自校正
- 在真实机器人操作任务中，泛化性能优于基线，对视觉干扰和光照变化鲁棒

## 摘要（原文）

> Behavior cloning methods for robot learning suffer from poor generalization
> due to limited data support beyond expert demonstrations. Recent approaches
> leveraging video prediction models have shown promising results by learning
> rich spatiotemporal representations from large-scale datasets. However, these
> models learn action-agnostic dynamics that cannot distinguish between different
> control inputs, limiting their utility for precise manipulation tasks and
> requiring large pretraining datasets. We propose a Dynamics-Aligned Flow
> Matching Policy (DAP) that integrates dynamics prediction into policy learning.
> Our method introduces a novel architecture where policy and dynamics models
> provide mutual corrective feedback during action generation, enabling
> self-correction and improved generalization. Empirical validation demonstrates
> generalization performance superior to baseline methods on real-world robotic
> manipulation tasks, showing particular robustness in OOD scenarios including
> visual distractions and lighting variations.

