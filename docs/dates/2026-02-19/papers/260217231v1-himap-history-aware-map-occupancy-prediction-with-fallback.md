---
layout: default
title: HiMAP: History-aware Map-occupancy Prediction with Fallback
---

# HiMAP: History-aware Map-occupancy Prediction with Fallback
**arXiv**：[2602.17231v1](https://arxiv.org/abs/2602.17231) · [PDF](https://arxiv.org/pdf/2602.17231.pdf)  
**作者**：Yiming Xu, Yi Yang, Hao Cheng, Monika Sester  

**一句话要点**：提出HiMAP框架，通过历史感知的占用图预测解决多目标跟踪失败下的运动预测问题。

**关键词**：运动预测, 多目标跟踪, 占用图, 历史查询, 自动驾驶, DETR解码器

## 3 点简述
- 核心问题：传统运动预测依赖多目标跟踪，跟踪失败时预测质量下降，增加安全风险。
- 方法要点：将过去检测转换为时空不变的历史占用图，引入历史查询模块检索代理特定历史，驱动解码器生成多模态未来轨迹。
- 实验或效果：在Argoverse 2上，无跟踪设置下性能优于基线，FDE和ADE分别提升11%和12%，MR降低4%。

## 摘要（原文）

> Accurate motion forecasting is critical for autonomous driving, yet most predictors rely on multi-object tracking (MOT) with identity association, assuming that objects are correctly and continuously tracked. When tracking fails due to, e.g., occlusion, identity switches, or missed detections, prediction quality degrades and safety risks increase. We present \textbf{HiMAP}, a tracking-free, trajectory prediction framework that remains reliable under MOT failures. HiMAP converts past detections into spatiotemporally invariant historical occupancy maps and introduces a historical query module that conditions on the current agent state to iteratively retrieve agent-specific history from unlabeled occupancy representations. The retrieved history is summarized by a temporal map embedding and, together with the final query and map context, drives a DETR-style decoder to produce multi-modal future trajectories. This design lifts identity reliance, supports streaming inference via reusable encodings, and serves as a robust fallback when tracking is unavailable. On Argoverse~2, HiMAP achieves performance comparable to tracking-based methods while operating without IDs, and it substantially outperforms strong baselines in the no-tracking setting, yielding relative gains of 11\% in FDE, 12\% in ADE, and a 4\% reduction in MR over a fine-tuned QCNet. Beyond aggregate metrics, HiMAP delivers stable forecasts for all agents simultaneously without waiting for tracking to recover, highlighting its practical value for safety-critical autonomy. The code is available under: https://github.com/XuYiMing83/HiMAP.

