---
layout: default
title: HiMAP: History-aware Map-occupancy Prediction with Fallback
---

# HiMAP: History-aware Map-occupancy Prediction with Fallback
**arXiv**：[2602.17231v1](https://arxiv.org/abs/2602.17231) · [PDF](https://arxiv.org/pdf/2602.17231.pdf)  
**作者**：Yiming Xu, Yi Yang, Hao Cheng, Monika Sester  

**一句话要点**：提出HiMAP框架以解决自动驾驶中多目标跟踪失败时的运动预测问题

**关键词**：自动驾驶, 运动预测, 历史占用地图, 跟踪无关预测, DETR解码器

## 3 点简述
- 核心问题：传统预测依赖多目标跟踪，跟踪失败时预测质量下降和安全风险增加
- 方法要点：使用历史占用地图和查询模块，无需身份关联，实现跟踪无关的轨迹预测
- 实验或效果：在Argoverse 2数据集上，性能接近基于跟踪的方法，无跟踪设置下显著优于基线

## 摘要（原文）

> Accurate motion forecasting is critical for autonomous driving, yet most predictors rely on multi-object tracking (MOT) with identity association, assuming that objects are correctly and continuously tracked. When tracking fails due to, e.g., occlusion, identity switches, or missed detections, prediction quality degrades and safety risks increase. We present \textbf{HiMAP}, a tracking-free, trajectory prediction framework that remains reliable under MOT failures. HiMAP converts past detections into spatiotemporally invariant historical occupancy maps and introduces a historical query module that conditions on the current agent state to iteratively retrieve agent-specific history from unlabeled occupancy representations. The retrieved history is summarized by a temporal map embedding and, together with the final query and map context, drives a DETR-style decoder to produce multi-modal future trajectories. This design lifts identity reliance, supports streaming inference via reusable encodings, and serves as a robust fallback when tracking is unavailable. On Argoverse~2, HiMAP achieves performance comparable to tracking-based methods while operating without IDs, and it substantially outperforms strong baselines in the no-tracking setting, yielding relative gains of 11\% in FDE, 12\% in ADE, and a 4\% reduction in MR over a fine-tuned QCNet. Beyond aggregate metrics, HiMAP delivers stable forecasts for all agents simultaneously without waiting for tracking to recover, highlighting its practical value for safety-critical autonomy. The code is available under: https://github.com/XuYiMing83/HiMAP.

