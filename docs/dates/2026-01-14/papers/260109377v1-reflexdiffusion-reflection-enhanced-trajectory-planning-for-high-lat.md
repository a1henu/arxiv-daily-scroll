---
layout: default
title: ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving
---

# ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving
**arXiv**：[2601.09377v1](https://arxiv.org/abs/2601.09377) · [PDF](https://arxiv.org/pdf/2601.09377.pdf)  
**作者**：Xuemei Yao, Xiao Yang, Jianbin Sun, Liuwei Xie, Xuebin Shao, Xiyu Fang, Hang Su, Kewei Yang  

**一句话要点**：提出ReflexDiffusion框架，通过反射增强扩散规划器以解决高横向加速度场景下的轨迹规划问题

**关键词**：自动驾驶轨迹规划, 扩散模型, 高横向加速度场景, 推理阶段优化, 物理约束强化, 长尾场景

## 3 点简述
- 核心问题：现有轨迹规划器在高横向加速度场景中因数据不平衡导致系统失效，无法充分建模车辆动力学和道路约束
- 方法要点：在迭代去噪过程中引入基于梯度的调整机制，放大关键条件信号如道路曲率，以强化物理约束
- 实验或效果：在nuPlan Test14-hard基准测试中，高横向加速度场景的驾驶分数比SOTA方法提升14.1%

## 摘要（原文）

> Generating safe and reliable trajectories for autonomous vehicles in long-tail scenarios remains a significant challenge, particularly for high-lateral-acceleration maneuvers such as sharp turns, which represent critical safety situations. Existing trajectory planners exhibit systematic failures in these scenarios due to data imbalance. This results in insufficient modelling of vehicle dynamics, road geometry, and environmental constraints in high-risk situations, leading to suboptimal or unsafe trajectory prediction when vehicles operate near their physical limits. In this paper, we introduce ReflexDiffusion, a novel inference-stage framework that enhances diffusion-based trajectory planners through reflective adjustment. Our method introduces a gradient-based adjustment mechanism during the iterative denoising process: after each standard trajectory update, we compute the gradient between the conditional and unconditional noise predictions to explicitly amplify critical conditioning signals, including road curvature and lateral vehicle dynamics. This amplification enforces strict adherence to physical constraints, particularly improving stability during high-lateral-acceleration maneuvers where precise vehicle-road interaction is paramount. Evaluated on the nuPlan Test14-hard benchmark, ReflexDiffusion achieves a 14.1% improvement in driving score for high-lateral-acceleration scenarios over the state-of-the-art (SOTA) methods. This demonstrates that inference-time trajectory optimization can effectively compensate for training data sparsity by dynamically reinforcing safety-critical constraints near handling limits. The framework's architecture-agnostic design enables direct deployment to existing diffusion-based planners, offering a practical solution for improving autonomous vehicle safety in challenging driving conditions.

