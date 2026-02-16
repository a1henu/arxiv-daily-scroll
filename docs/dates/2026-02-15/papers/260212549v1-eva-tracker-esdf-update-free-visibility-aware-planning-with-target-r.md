---
layout: default
title: Eva-Tracker: ESDF-update-free, Visibility-aware Planning with Target Reacquisition for Robust Aerial Tracking
---

# Eva-Tracker: ESDF-update-free, Visibility-aware Planning with Target Reacquisition for Robust Aerial Tracking
**arXiv**：[2602.12549v1](https://arxiv.org/abs/2602.12549) · [PDF](https://arxiv.org/pdf/2602.12549.pdf)  
**作者**：Yue Lin, Yang Liu, Dong Wang, Huchuan Lu  

**一句话要点**：提出Eva-Tracker，通过预计算FoV-ESDF和恢复路径生成，实现无ESDF更新的鲁棒空中跟踪。

**关键词**：空中跟踪, 可见性感知规划, ESDF优化, 目标重获取, 轨迹预测

## 3 点简述
- 核心问题：频繁ESDF更新在跟踪中带来高计算开销，影响实时性和鲁棒性。
- 方法要点：设计目标轨迹预测、可见性感知初始路径生成和预计算FoV-ESDF，支持快速重规划。
- 实验或效果：仿真和真实实验显示，相比现有方法，计算量更低且跟踪更鲁棒。

## 摘要（原文）

> The Euclidean Signed Distance Field (ESDF) is widely used in visibility evaluation to prevent occlusions and collisions during tracking. However, frequent ESDF updates introduce considerable computational overhead. To address this issue, we propose Eva-Tracker, a visibility-aware trajectory planning framework for aerial tracking that eliminates ESDF updates and incorporates a recovery-capable path generation method for target reacquisition. First, we design a target trajectory prediction method and a visibility-aware initial path generation algorithm that maintain an appropriate observation distance, avoid occlusions, and enable rapid replanning to reacquire the target when it is lost. Then, we propose the Field of View ESDF (FoV-ESDF), a precomputed ESDF tailored to the tracker's field of view, enabling rapid visibility evaluation without requiring updates. Finally, we optimize the trajectory using differentiable FoV-ESDF-based objectives to ensure continuous visibility throughout the tracking process. Extensive simulations and real-world experiments demonstrate that our approach delivers more robust tracking results with lower computational effort than existing state-of-the-art methods. The source code is available at https://github.com/Yue-0/Eva-Tracker.

