---
layout: default
title: Temporally-Sampled Efficiently Adaptive State Lattices for Autonomous Ground Robot Navigation in Partially Observed Environments
---

# Temporally-Sampled Efficiently Adaptive State Lattices for Autonomous Ground Robot Navigation in Partially Observed Environments
**arXiv**：[2602.13159v1](https://arxiv.org/abs/2602.13159) · [PDF](https://arxiv.org/pdf/2602.13159.pdf)  
**作者**：Ashwin Satish Menon, Eric R. Damm, Eli S. Lancaster, Felix A. Sanchez, Jason M. Gregory, Thomas M. Howard  

**一句话要点**：提出TSEASL以解决越野机器人导航中因区域规划频繁变更导致的不安全行为问题

**关键词**：越野机器人导航, 部分可观测环境, 区域规划仲裁, 轨迹优化, 规划稳定性

## 3 点简述
- 核心问题：部分可观测环境下，区域规划频繁变更导致参考轨迹不稳定，引发不安全导航行为
- 方法要点：TSEASL通过仲裁架构，比较新旧轨迹以优化区域规划，提升稳定性
- 实验或效果：在Warthog机器人上测试，TSEASL减少了手动干预，提高了规划稳定性

## 摘要（原文）

> Due to sensor limitations, environments that off-road mobile robots operate in are often only partially observable. As the robots move throughout the environment and towards their goal, the optimal route is continuously revised as the sensors perceive new information. In traditional autonomous navigation architectures, a regional motion planner will consume the environment map and output a trajectory for the local motion planner to use as a reference. Due to the continuous revision of the regional plan guidance as a result of changing map information, the reference trajectories which are passed down to the local planner can differ significantly across sequential planning cycles. This rapidly changing guidance can result in unsafe navigation behavior, often requiring manual safety interventions during autonomous traversals in off-road environments. To remedy this problem, we propose Temporally-Sampled Efficiently Adaptive State Lattices (TSEASL), which is a regional planner arbitration architecture that considers updated and optimized versions of previously generated trajectories against the currently generated trajectory. When tested on a Clearpath Robotics Warthog Unmanned Ground Vehicle as well as real map data collected from the Warthog, results indicate that when running TSEASL, the robot did not require manual interventions in the same locations where the robot was running the baseline planner. Additionally, higher levels of planner stability were recorded with TSEASL over the baseline. The paper concludes with a discussion of further improvements to TSEASL in order to make it more generalizable to various off-road autonomy scenarios.

