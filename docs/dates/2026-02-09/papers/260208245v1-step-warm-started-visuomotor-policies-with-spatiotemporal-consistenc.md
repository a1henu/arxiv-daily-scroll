---
layout: default
title: STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction
---

# STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction
**arXiv**：[2602.08245v1](https://arxiv.org/abs/2602.08245) · [PDF](https://arxiv.org/pdf/2602.08245.pdf)  
**作者**：Jinhao Li, Yuxuan Cong, Yingqiao Wang, Hao Xia, Shan Huang, Yijia Zhang, Ningyi Xu, Guohao Dai  

**一句话要点**：提出STEP方法，通过时空一致性预测机制加速扩散策略，提升机器人视觉运动控制的实时性。

**关键词**：扩散策略, 视觉运动控制, 推理加速, 时空一致性, 机器人操作, 实时系统

## 3 点简述
- 扩散策略在机器人视觉运动控制中因迭代去噪导致高推理延迟，限制实时闭环系统性能。
- STEP引入轻量级时空一致性预测机制生成高质量预热动作，保持动作分布接近目标且时间一致，不损害原始生成能力。
- 在模拟和真实世界任务中评估，STEP以2步采样在RoboMimic基准和真实任务上分别比BRIDGER和DDIM平均提高21.6%和27.5%成功率。

## 摘要（原文）

> Diffusion policies have recently emerged as a powerful paradigm for visuomotor control in robotic manipulation due to their ability to model the distribution of action sequences and capture multimodality. However, iterative denoising leads to substantial inference latency, limiting control frequency in real-time closed-loop systems. Existing acceleration methods either reduce sampling steps, bypass diffusion through direct prediction, or reuse past actions, but often struggle to jointly preserve action quality and achieve consistently low latency. In this work, we propose STEP, a lightweight spatiotemporal consistency prediction mechanism to construct high-quality warm-start actions that are both distributionally close to the target action and temporally consistent, without compromising the generative capability of the original diffusion policy. Then, we propose a velocity-aware perturbation injection mechanism that adaptively modulates actuation excitation based on temporal action variation to prevent execution stall especially for real-world tasks. We further provide a theoretical analysis showing that the proposed prediction induces a locally contractive mapping, ensuring convergence of action errors during diffusion refinement. We conduct extensive evaluations on nine simulated benchmarks and two real-world tasks. Notably, STEP with 2 steps can achieve an average 21.6% and 27.5% higher success rate than BRIDGER and DDIM on the RoboMimic benchmark and real-world tasks, respectively. These results demonstrate that STEP consistently advances the Pareto frontier of inference latency and success rate over existing methods.

