---
layout: default
title: Schrödinger's Navigator: Imagining an Ensemble of Futures for Zero-Shot Object Navigation
---

# Schrödinger's Navigator: Imagining an Ensemble of Futures for Zero-Shot Object Navigation
**arXiv**：[2512.21201v1](https://arxiv.org/abs/2512.21201) · [PDF](https://arxiv.org/pdf/2512.21201.pdf)  
**作者**：Yu He, Da Huang, Zhenyang Liu, Zixiao Gu, Qiang Sun, Guangnan Ye, Yanwei Fu  

**一句话要点**：提出Schrödinger's Navigator框架，通过轨迹条件3D想象解决零样本物体导航在遮挡和动态环境中的挑战。

**关键词**：零样本物体导航, 轨迹条件3D想象, 机器人导航, 遮挡处理, 动态目标跟踪

## 3 点简述
- 核心问题：零样本物体导航在遮挡、未知风险和动态目标场景中性能受限。
- 方法要点：基于轨迹条件3D世界模型想象未来观测，融合到导航图中以优化策略。
- 实验或效果：在Go2四足机器人上验证，在遮挡严重环境中优于基线，提升成功率和定位精度。

## 摘要（原文）

> Zero-shot object navigation (ZSON) requires a robot to locate a target object in a previously unseen environment without relying on pre-built maps or task-specific training. However, existing ZSON methods often struggle in realistic and cluttered environments, particularly when the scene contains heavy occlusions, unknown risks, or dynamically moving target objects. To address these challenges, we propose \textbf{Schrödinger's Navigator}, a navigation framework inspired by Schrödinger's thought experiment on uncertainty. The framework treats unobserved space as a set of plausible future worlds and reasons over them before acting. Conditioned on egocentric visual inputs and three candidate trajectories, a trajectory-conditioned 3D world model imagines future observations along each path. This enables the agent to see beyond occlusions and anticipate risks in unseen regions without requiring extra detours or dense global mapping. The imagined 3D observations are fused into the navigation map and used to update a value map. These updates guide the policy toward trajectories that avoid occlusions, reduce exposure to uncertain space, and better track moving targets. Experiments on a Go2 quadruped robot across three challenging scenarios, including severe static occlusions, unknown risks, and dynamically moving targets, show that Schrödinger's Navigator consistently outperforms strong ZSON baselines in self-localization, object localization, and overall Success Rate in occlusion-heavy environments. These results demonstrate the effectiveness of trajectory-conditioned 3D imagination in enabling robust zero-shot object navigation.

