---
layout: default
title: HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation
---

# HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation
**arXiv**：[2511.14756v1](https://arxiv.org/abs/2511.14756) · [PDF](https://arxiv.org/pdf/2511.14756.pdf)  
**作者**：Lai Wei, Xuanbin Peng, Ri-Zhao Qiu, Tianshu Huang, Xuxin Cheng, Xiaolong Wang  

**一句话要点**：提出异构元控制框架以解决接触丰富的移动操作中控制器适应性问题

**关键词**：异构控制, 移动操作, 力感知策略, 专家混合, 机器人学习

## 3 点简述
- 核心问题：位置控制器在复杂交互中难以处理接触和变负载
- 方法要点：融合位置、阻抗和力-位置控制，采用专家混合路由学习
- 实验或效果：在真实人形机器人上任务性能提升超50%

## 摘要（原文）

> Learning from real-world robot demonstrations holds promise for interacting with complex real-world environments. However, the complexity and variability of interaction dynamics often cause purely positional controllers to struggle with contacts or varying payloads. To address this, we propose a Heterogeneous Meta-Control (HMC) framework for Loco-Manipulation that adaptively stitches multiple control modalities: position, impedance, and hybrid force-position. We first introduce an interface, HMC-Controller, for blending actions from different control profiles continuously in the torque space. HMC-Controller facilitates both teleoperation and policy deployment. Then, to learn a robust force-aware policy, we propose HMC-Policy to unify different controllers into a heterogeneous architecture. We adopt a mixture-of-experts style routing to learn from large-scale position-only data and fine-grained force-aware demonstrations. Experiments on a real humanoid robot show over 50% relative improvement vs. baselines on challenging tasks such as compliant table wiping and drawer opening, demonstrating the efficacy of HMC.

