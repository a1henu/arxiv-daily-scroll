---
layout: default
title: Warm-Starting Collision-Free Model Predictive Control With Object-Centric Diffusion
---

# Warm-Starting Collision-Free Model Predictive Control With Object-Centric Diffusion
**arXiv**：[2601.02873v1](https://arxiv.org/abs/2601.02873) · [PDF](https://arxiv.org/pdf/2601.02873.pdf)  
**作者**：Arthur Haffemayer, Alexandre Chapin, Armand Jordana, Krzysztof Wojciechowski, Florent Lamiraux, Nicolas Mansard, Vladimir Petrik  

**一句话要点**：提出基于对象中心扩散的预热启动方法，结合模型预测控制以解决密集障碍物环境下的实时无碰撞运动生成问题。

**关键词**：模型预测控制, 扩散模型, 对象中心表示, 无碰撞运动规划, 实时控制, 机器人运动生成

## 3 点简述
- 核心问题：传统优化控制器在密集障碍物中难以快速生成可行解，扩散模型缺乏高效场景结构条件化方法。
- 方法要点：使用对象中心槽注意力机制提供紧凑障碍物表示，结合扩散变换器生成轨迹，并通过模型预测控制优化动力学和碰撞约束。
- 实验或效果：在基准任务中，该方法比采样规划器或单独组件显著提高成功率、降低延迟，真实机器人实验验证了可靠安全执行。

## 摘要（原文）

> Acting in cluttered environments requires predicting and avoiding collisions while still achieving precise control. Conventional optimization-based controllers can enforce physical constraints, but they struggle to produce feasible solutions quickly when many obstacles are present. Diffusion models can generate diverse trajectories around obstacles, yet prior approaches lacked a general and efficient way to condition them on scene structure. In this paper, we show that combining diffusion-based warm-starting conditioned with a latent object-centric representation of the scene and with a collision-aware model predictive controller (MPC) yields reliable and efficient motion generation under strict time limits. Our approach conditions a diffusion transformer on the system state, task, and surroundings, using an object-centric slot attention mechanism to provide a compact obstacle representation suitable for control. The sampled trajectories are refined by an optimal control problem that enforces rigid-body dynamics and signed-distance collision constraints, producing feasible motions in real time. On benchmark tasks, this hybrid method achieved markedly higher success rates and lower latency than sampling-based planners or either component alone. Real-robot experiments with a torque-controlled Panda confirm reliable and safe execution with MPC.

