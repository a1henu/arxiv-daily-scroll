---
layout: default
title: Certified Gradient-Based Contact-Rich Manipulation via Smoothing-Error Reachable Tubes
---

# Certified Gradient-Based Contact-Rich Manipulation via Smoothing-Error Reachable Tubes
**arXiv**：[2602.09368v1](https://arxiv.org/abs/2602.09368) · [PDF](https://arxiv.org/pdf/2602.09368.pdf)  
**作者**：Wei-Chen Li, Glen Chou  

**一句话要点**：提出基于平滑误差可达管的梯度方法，以解决接触丰富操作中的梯度不连续与模型失配问题。

**关键词**：接触丰富操作, 梯度优化, 可微模拟器, 可达集分析, 鲁棒控制, 混合动力学

## 3 点简述
- 核心问题：接触丰富操作中，混合接触动力学导致梯度不连续或消失，平滑动力学虽提供连续梯度但引入模型失配风险。
- 方法要点：通过凸优化构建可微模拟器平滑动力学，量化误差为集值偏差，结合可达集分析优化时变仿射反馈策略。
- 实验或效果：在平面推动、物体旋转和灵巧操作等任务中，实现约束满足保证，安全违规和目标误差低于基线方法。

## 摘要（原文）

> Gradient-based methods can efficiently optimize controllers using physical priors and differentiable simulators, but contact-rich manipulation remains challenging due to discontinuous or vanishing gradients from hybrid contact dynamics. Smoothing the dynamics yields continuous gradients, but the resulting model mismatch can cause controller failures when executed on real systems. We address this trade-off by planning with smoothed dynamics while explicitly quantifying and compensating for the induced errors, providing formal guarantees of constraint satisfaction and goal reachability on the true hybrid dynamics. Our method smooths both contact dynamics and geometry via a novel differentiable simulator based on convex optimization, which enables us to characterize the discrepancy from the true dynamics as a set-valued deviation. This deviation constrains the optimization of time-varying affine feedback policies through analytical bounds on the system's reachable set, enabling robust constraint satisfaction guarantees for the true closed-loop hybrid dynamics, while relying solely on informative gradients from the smoothed dynamics. We evaluate our method on several contact-rich tasks, including planar pushing, object rotation, and in-hand dexterous manipulation, achieving guaranteed constraint satisfaction with lower safety violation and goal error than baselines. By bridging differentiable physics with set-valued robust control, our method is the first certifiable gradient-based policy synthesis method for contact-rich manipulation.

