---
layout: default
title: Safe and Stylized Trajectory Planning for Autonomous Driving via Diffusion Model
---

# Safe and Stylized Trajectory Planning for Autonomous Driving via Diffusion Model
**arXiv**：[2602.04329v1](https://arxiv.org/abs/2602.04329) · [PDF](https://arxiv.org/pdf/2602.04329.pdf)  
**作者**：Shuo Pei, Yong Wang, Yuanchen Zhu, Chen Sun, Qin Li, Yanan Zhao, Huachun Tan  

**一句话要点**：提出SDD Planner扩散模型框架，以在复杂场景中实现安全与风格化轨迹规划

**关键词**：自动驾驶轨迹规划, 扩散模型, 安全约束, 驾驶风格, 实时规划, 多源感知

## 3 点简述
- 核心问题：自动驾驶在复杂场景中需兼顾安全约束与驾驶风格，实时规划挑战大
- 方法要点：集成多源风格感知编码器和风格引导动态轨迹生成器，通过扩散去噪调制权重
- 实验或效果：在StyleDrive基准上SM-PDMS指标提升3.9%，NuPlan测试中排名第一，实车闭环验证有效

## 摘要（原文）

> Achieving safe and stylized trajectory planning in complex real-world scenarios remains a critical challenge for autonomous driving systems. This paper proposes the SDD Planner, a diffusion-based framework designed to effectively reconcile safety constraints with driving styles in real time. The framework integrates two core modules: a Multi-Source Style-Aware Encoder, which employs distance-sensitive attention to fuse dynamic agent data and environmental contexts for heterogeneous safety-style perception; and a Style-Guided Dynamic Trajectory Generator, which adaptively modulates priority weights within the diffusion denoising process to generate user-preferred yet safe trajectories. Extensive experiments demonstrate that SDD Planner achieves state-of-the-art performance. On the StyleDrive benchmark, it improves the SM-PDMS metric by 3.9% over WoTE, the strongest baseline. Furthermore, on the NuPlan Test14 and Test14-hard benchmarks, SDD Planner ranks first with overall scores of 91.76 and 80.32, respectively, outperforming leading methods such as PLUTO. Real-vehicle closed-loop tests further confirm that SDD Planner maintains high safety standards while aligning with preset driving styles, validating its practical applicability for real-world deployment.

