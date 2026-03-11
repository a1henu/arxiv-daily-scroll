---
layout: default
title: ImpedanceDiffusion: Diffusion-Based Global Path Planning for UAV Swarm Navigation with Generative Impedance Control
---

# ImpedanceDiffusion: Diffusion-Based Global Path Planning for UAV Swarm Navigation with Generative Impedance Control
**arXiv**：[2603.09031v1](https://arxiv.org/abs/2603.09031) · [PDF](https://arxiv.org/pdf/2603.09031.pdf)  
**作者**：Faryal Batool, Yasheerah Yaqoot, Muhammad Ahsan Mustafa, Roohan Ahmed Khan, Aleksey Fedoseev, Dzmitry Tsetserukou  

**一句话要点**：提出ImpedanceDiffusion框架，基于扩散模型和阻抗控制实现无人机群在杂乱室内环境中的安全导航。

**关键词**：无人机群导航, 扩散模型路径规划, 阻抗控制, 语义障碍分类, 室内环境

## 3 点简述
- 核心问题：无人机群在杂乱室内环境中需要长时程规划、反应式避障和自适应柔顺性。
- 方法要点：结合图像条件扩散模型进行全局路径规划，通过APF跟踪和语义感知可变阻抗控制执行。
- 实验或效果：在20种配置中实现100%轨迹生成率和92%成功率，通过零样本仿真到真实部署验证。

## 摘要（原文）

> Safe swarm navigation in cluttered indoor environment requires long-horizon planning, reactive obstacle avoidance, and adaptive compliance. We propose ImpedanceDiffusion, a hierarchical framework that leverages image-conditioned diffusion-based global path planning with Artificial Potential Field (APF) tracking and semantic-aware variable impedance control for aerial drone swarms.
>   The diffusion model generates geometric global trajectories directly from RGB images without explicit map construction. These trajectories are tracked by an APF-based reactive layer, while a VLM-RAG module performs semantic obstacle classification with 90% retrieval accuracy to adapt impedance parameters for mixed obstacle environments during execution.
>   Two diffusion planners are evaluated: (i) a top-view long-horizon planner using single-pass inference and (ii) a first-person-view (FPV) short-horizon planner deployed via a two-stage inference pipeline. Both planners achieve a 100% trajectory generation rate across twenty static and dynamic experimental configurations and are validated via zero-shot sim-to-real deployment on Crazyflie 2.1 drones through the hierarchical APF-impedance control stack. The top-view planner produces smoother trajectories that yield conservative tracking speeds of 1.0-1.2 m/s near hard obstacles and 0.6-1.0 m/s near soft obstacles. In contrast, the FPV planner generates trajectories with greater local clearance and typically higher speeds, reaching 1.4-2.0 m/s near hard obstacles and up to 1.6 m/s near soft obstacles. Across 20 experimental configurations (100 total runs), the framework achieved a 92% success rate while maintaining stable impedance-based formation control with bounded oscillations and no in-flight collisions, demonstrating reliable and adaptive swarm navigation in cluttered indoor environments.

