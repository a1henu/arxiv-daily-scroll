---
layout: default
title: Aerial World Model for Long-horizon Visual Generation and Navigation in 3D Space
---

# Aerial World Model for Long-horizon Visual Generation and Navigation in 3D Space
**arXiv**：[2512.21887v1](https://arxiv.org/abs/2512.21887) · [PDF](https://arxiv.org/pdf/2512.21887.pdf)  
**作者**：Weichen Zhang, Peizhi Tang, Xin Zeng, Fanhang Man, Shiquan Yu, Zichao Dai, Baining Zhao, Hongjin Chen, Yu Shang, Wei Wu, Chen Gao, Xinlei Chen, Xin Wang, Yong Li, Wenwu Zhu  

**一句话要点**：提出ANWM以解决无人机在3D环境中缺乏高层语义导航能力的问题

**关键词**：无人机导航, 世界模型, 视觉生成, 3D环境, 语义规划, 未来帧投影

## 3 点简述
- 核心问题：现有无人机导航策略仅优化低层目标，缺乏高层语义规划能力
- 方法要点：引入ANWM，通过未来帧投影模块预测视觉观测，评估轨迹语义合理性与导航效用
- 实验或效果：在长距离视觉预测中优于现有世界模型，提升大规模环境导航成功率

## 摘要（原文）

> Unmanned aerial vehicles (UAVs) have emerged as powerful embodied agents. One of the core abilities is autonomous navigation in large-scale three-dimensional environments. Existing navigation policies, however, are typically optimized for low-level objectives such as obstacle avoidance and trajectory smoothness, lacking the ability to incorporate high-level semantics into planning. To bridge this gap, we propose ANWM, an aerial navigation world model that predicts future visual observations conditioned on past frames and actions, thereby enabling agents to rank candidate trajectories by their semantic plausibility and navigational utility. ANWM is trained on 4-DoF UAV trajectories and introduces a physics-inspired module: Future Frame Projection (FFP), which projects past frames into future viewpoints to provide coarse geometric priors. This module mitigates representational uncertainty in long-distance visual generation and captures the mapping between 3D trajectories and egocentric observations. Empirical results demonstrate that ANWM significantly outperforms existing world models in long-distance visual forecasting and improves UAV navigation success rates in large-scale environments.

