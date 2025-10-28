---
layout: default
title: Deep Active Inference with Diffusion Policy and Multiple Timescale World Model for Real-World Exploration and Navigation
---

# Deep Active Inference with Diffusion Policy and Multiple Timescale World Model for Real-World Exploration and Navigation
**arXiv**：[2510.23258v1](https://arxiv.org/abs/2510.23258) · [PDF](https://arxiv.org/pdf/2510.23258.pdf)  
**作者**：Riko Yokozawa, Kentaro Fujii, Yuta Nomura, Shingo Murata  

**一句话要点**：提出基于扩散策略和多时间尺度世界模型的深度主动推理框架，用于真实世界机器人探索与导航。

**关键词**：主动推理, 扩散策略, 多时间尺度世界模型, 机器人导航, 期望自由能最小化

## 3 点简述
- 核心问题：真实世界机器人导航需平衡探索获取环境信息与目标导向导航。
- 方法要点：结合扩散策略生成多样动作，多时间尺度世界模型预测长期后果以最小化期望自由能。
- 实验效果：真实世界实验显示，在探索需求高场景中，成功率更高且碰撞更少。

## 摘要（原文）

> Autonomous robotic navigation in real-world environments requires exploration
> to acquire environmental information as well as goal-directed navigation in
> order to reach specified targets. Active inference (AIF) based on the
> free-energy principle provides a unified framework for these behaviors by
> minimizing the expected free energy (EFE), thereby combining epistemic and
> extrinsic values. To realize this practically, we propose a deep AIF framework
> that integrates a diffusion policy as the policy model and a multiple timescale
> recurrent state-space model (MTRSSM) as the world model. The diffusion policy
> generates diverse candidate actions while the MTRSSM predicts their
> long-horizon consequences through latent imagination, enabling action selection
> that minimizes EFE. Real-world navigation experiments demonstrated that our
> framework achieved higher success rates and fewer collisions compared with the
> baselines, particularly in exploration-demanding scenarios. These results
> highlight how AIF based on EFE minimization can unify exploration and
> goal-directed navigation in real-world robotic settings.

