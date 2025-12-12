---
layout: default
title: Deep sets and event-level maximum-likelihood estimation for fast pile-up jet rejection in ATLAS
---

# Deep sets and event-level maximum-likelihood estimation for fast pile-up jet rejection in ATLAS
**arXiv**：[2512.10819v1](https://arxiv.org/abs/2512.10819) · [PDF](https://arxiv.org/pdf/2512.10819.pdf)  
**作者**：Mohammed Aboelela  

**一句话要点**：提出基于Deep Sets的DIPz模型和MLPL判别器，以高效处理ATLAS触发器中多喷注事件的堆积背景抑制。

**关键词**：堆积背景抑制, Deep Sets架构, 喷注起源回归, 事件级判别, ATLAS触发器, 实时处理

## 3 点简述
- 核心问题：LHC高亮度运行导致堆积碰撞增多，多喷注事件背景抑制需求迫切，尤其在实时触发层面。
- 方法要点：使用Deep Sets架构的DIPz模型，基于带电粒子轨迹回归喷注起源位置，结合MLPL进行事件级判别。
- 实验或效果：该方法提供鲁棒且计算高效的堆积抑制方案，适用于ATLAS高级触发器的实时事件选择。

## 摘要（原文）

> Multiple proton-proton collisions (pile-up) occur at every bunch crossing at the LHC, with the mean number of interactions expected to reach 80 during Run 3 and up to 200 at the High-Luminosity LHC. As a direct consequence, events with multijet signatures will occur at increasingly high rates. To cope with the increased luminosity, being able to efficiently group jets according to their origin along the beamline is crucial, particularly at the trigger level. In this work, a novel uncertainty-aware jet regression model based on a Deep Sets architecture is introduced, DIPz, to regress on a jet origin position along the beamline. The inputs to the DIPz algorithm are the charged particle tracks associated to each jet. An event-level discriminant, the Maximum Log Product of Likelihoods (MLPL), is constructed by combining the DIPz per-jet predictions. MLPL is cut-optimized to select events compatible with targeted multi-jet signature selection. This combined approach provides a robust and computationally efficient method for pile-up rejection in multi-jet final states, applicable to real-time event selections at the ATLAS High Level Trigger.

