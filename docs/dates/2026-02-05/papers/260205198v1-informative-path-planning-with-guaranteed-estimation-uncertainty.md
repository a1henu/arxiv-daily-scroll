---
layout: default
title: Informative Path Planning with Guaranteed Estimation Uncertainty
---

# Informative Path Planning with Guaranteed Estimation Uncertainty
**arXiv**：[2602.05198v1](https://arxiv.org/abs/2602.05198) · [PDF](https://arxiv.org/pdf/2602.05198.pdf)  
**作者**：Kalvik Jakkala, Saurav Agarwal, Jason O'Kane, Srinivas Akella  

**一句话要点**：提出保证估计不确定性的信息路径规划方法，用于环境监测机器人高效重建空间场。

**关键词**：信息路径规划, 高斯过程, 估计不确定性, 环境监测, 机器人路径规划, 非平稳核

## 3 点简述
- 核心问题：环境监测中传统方法浪费采样，信息路径规划缺乏重建质量保证。
- 方法要点：基于高斯过程模型，通过覆盖图转换和路径规划确保后验方差低于阈值。
- 实验效果：在真实地形数据上比基线减少采样点和行程，现场实验验证可行性。

## 摘要（原文）

> Environmental monitoring robots often need to reconstruct spatial fields (e.g., salinity, temperature, bathymetry) under tight distance and energy constraints. Classical boustrophedon lawnmower surveys provide geometric coverage guarantees but can waste effort by oversampling predictable regions. In contrast, informative path planning (IPP) methods leverage spatial correlations to reduce oversampling, yet typically offer no guarantees on reconstruction quality. This paper bridges these approaches by addressing informative path planning with guaranteed estimation uncertainty: computing the shortest path whose measurements ensure that the Gaussian-process (GP) posterior variance -- an intrinsic uncertainty measure that lower-bounds the mean-squared prediction error under the GP model -- falls below a user-specified threshold over the monitoring region.
>   We propose a three-stage approach: (i) learn a GP model from available prior information; (ii) transform the learned GP kernel into binary coverage maps for each candidate sensing location, indicating which locations' uncertainty can be reduced below a specified target; and (iii) plan a near-shortest route whose combined coverage satisfies the global uncertainty constraint. To address heterogeneous phenomena, we incorporate a nonstationary kernel that captures spatially varying correlation structure, and we accommodate non-convex environments with obstacles. Algorithmically, we present methods with provable approximation guarantees for sensing-location selection and for the joint selection-and-routing problem under a travel budget. Experiments on real-world topographic data show that our planners meet the uncertainty target using fewer sensing locations and shorter travel distances than a recent baseline, and field experiments with bathymetry-mapping autonomous surface and underwater vehicles demonstrate real-world feasibility.

