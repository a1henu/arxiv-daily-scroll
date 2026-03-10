---
layout: default
title: PhaForce: Phase-Scheduled Visual-Force Policy Learning with Slow Planning and Fast Correction for Contact-Rich Manipulation
---

# PhaForce: Phase-Scheduled Visual-Force Policy Learning with Slow Planning and Fast Correction for Contact-Rich Manipulation
**arXiv**：[2603.08342v1](https://arxiv.org/abs/2603.08342) · [PDF](https://arxiv.org/pdf/2603.08342.pdf)  
**作者**：Mingxin Wang, Zhirun Yue, Renhao Lu, Yizhe Li, Zihan Wang, Guoping Pan, Kangkang Dong, Jun Cheng, Yi Cheng, Houde Liu  

**一句话要点**：提出PhaForce相位调度视觉-力策略，通过慢速规划与快速校正解决接触丰富操作问题。

**关键词**：接触丰富操作, 视觉-力策略, 相位调度, 慢速规划, 快速校正, 机器人控制

## 3 点简述
- 核心问题：现有视觉-力策略更新频率低，缺乏相位调度机制，无法有效利用力反馈进行实时控制。
- 方法要点：结合接触感知相位预测器、慢速扩散规划器和快速校正器，实现相位调度的视觉-力融合与微调。
- 实验或效果：在真实机器人任务中平均成功率86%，提升接触质量，对几何偏移具有鲁棒适应性。

## 摘要（原文）

> Contact-rich manipulation requires not only vision-dominant task semantics but also closed-loop reactions to force/torque (F/T) transients. Yet, generative visuomotor policies are typically constrained to low-frequency updates due to inference latency and action chunking, underutilizing F/T for control-rate feedback. Furthermore, existing force-aware methods often inject force continuously and indiscriminately, lacking an explicit mechanism to schedule when / how much / where to apply force across different task phases. We propose PhaForce, a phase-scheduled visual--force policy that coordinates low-rate chunk-level planning and high-rate residual correction via a unified contact/phase schedule. PhaForce comprises (i) a contact-aware phase predictor (CAP) that estimates contact probability and phase belief, (ii) a Slow diffusion planner that performs dual-gated visual--force fusion with orthogonal residual injection to preserve vision semantics while conditioning on force, and (iii) a Fast corrector that applies control-rate phase-routed residuals in interpretable corrective subspaces for within-chunk micro-adjustments. Across multiple real-robot contact-rich tasks, PhaForce achieves an average success rate of 86% (+40 pp over baselines), while also substantially improving contact quality by regulating interaction forces and exhibiting robust adaptability to OOD geometric shifts.

