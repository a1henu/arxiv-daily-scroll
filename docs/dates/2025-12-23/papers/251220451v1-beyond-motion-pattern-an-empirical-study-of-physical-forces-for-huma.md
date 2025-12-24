---
layout: default
title: Beyond Motion Pattern: An Empirical Study of Physical Forces for Human Motion Understanding
---

# Beyond Motion Pattern: An Empirical Study of Physical Forces for Human Motion Understanding
**arXiv**：[2512.20451v1](https://arxiv.org/abs/2512.20451) · [PDF](https://arxiv.org/pdf/2512.20451.pdf)  
**作者**：Anh Dao, Manh Tran, Yufei Zhang, Xiaoming Liu, Zijun Cui  

**一句话要点**：引入物理力线索以增强动态或遮挡条件下的人体运动理解

**关键词**：人体运动理解, 物理力线索, 步态识别, 动作识别, 视频描述, 多任务评估

## 3 点简述
- 核心问题：现有方法忽视关节驱动力等物理线索，影响运动理解准确性。
- 方法要点：将物理推断的力整合到标准运动理解流程中，系统评估其影响。
- 实验效果：在步态识别、动作识别和视频描述任务中，加入力线索带来一致性能提升。

## 摘要（原文）

> Human motion understanding has advanced rapidly through vision-based progress in recognition, tracking, and captioning. However, most existing methods overlook physical cues such as joint actuation forces that are fundamental in biomechanics. This gap motivates our study: if and when do physically inferred forces enhance motion understanding? By incorporating forces into established motion understanding pipelines, we systematically evaluate their impact across baseline models on 3 major tasks: gait recognition, action recognition, and fine-grained video captioning. Across 8 benchmarks, incorporating forces yields consistent performance gains; for example, on CASIA-B, Rank-1 gait recognition accuracy improved from 89.52% to 90.39% (+0.87), with larger gain observed under challenging conditions: +2.7% when wearing a coat and +3.0% at the side view. On Gait3D, performance also increases from 46.0% to 47.3% (+1.3). In action recognition, CTR-GCN achieved +2.00% on Penn Action, while high-exertion classes like punching/slapping improved by +6.96%. Even in video captioning, Qwen2.5-VL's ROUGE-L score rose from 0.310 to 0.339 (+0.029), indicating that physics-inferred forces enhance temporal grounding and semantic richness. These results demonstrate that force cues can substantially complement visual and kinematic features under dynamic, occluded, or appearance-varying conditions.

