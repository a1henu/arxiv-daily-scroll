---
layout: default
title: RoaD: Rollouts as Demonstrations for Closed-Loop Supervised Fine-Tuning of Autonomous Driving Policies
---

# RoaD: Rollouts as Demonstrations for Closed-Loop Supervised Fine-Tuning of Autonomous Driving Policies
**arXiv**：[2512.01993v1](https://arxiv.org/abs/2512.01993) · [PDF](https://arxiv.org/pdf/2512.01993.pdf)  
**作者**：Guillermo Garcia-Cobo, Maximilian Igl, Peter Karkus, Zhejun Zhang, Michael Watson, Yuxiao Chen, Boris Ivanovic, Marco Pavone  

**一句话要点**：提出RoaD方法，利用策略自身闭环轨迹作为演示数据，以缓解自动驾驶策略中的协变量偏移问题。

**关键词**：自动驾驶策略, 闭环监督微调, 协变量偏移缓解, 轨迹生成, 仿真基准测试, 端到端驾驶

## 3 点简述
- 核心问题：自动驾驶策略在开环行为克隆训练后，部署于闭环时因协变量偏移导致误差累积。
- 方法要点：通过策略自身闭环轨迹生成高质量演示数据，结合专家指导进行监督微调，减少数据需求。
- 实验或效果：在WOSAC和AlpaSim仿真中，性能优于或接近现有方法，驾驶分数提升41%，碰撞减少54%。

## 摘要（原文）

> Autonomous driving policies are typically trained via open-loop behavior cloning of human demonstrations. However, such policies suffer from covariate shift when deployed in closed loop, leading to compounding errors. We introduce Rollouts as Demonstrations (RoaD), a simple and efficient method to mitigate covariate shift by leveraging the policy's own closed-loop rollouts as additional training data. During rollout generation, RoaD incorporates expert guidance to bias trajectories toward high-quality behavior, producing informative yet realistic demonstrations for fine-tuning. This approach enables robust closed-loop adaptation with orders of magnitude less data than reinforcement learning, and avoids restrictive assumptions of prior closed-loop supervised fine-tuning (CL-SFT) methods, allowing broader applications domains including end-to-end driving. We demonstrate the effectiveness of RoaD on WOSAC, a large-scale traffic simulation benchmark, where it performs similar or better than the prior CL-SFT method; and in AlpaSim, a high-fidelity neural reconstruction-based simulator for end-to-end driving, where it improves driving score by 41\% and reduces collisions by 54\%.

