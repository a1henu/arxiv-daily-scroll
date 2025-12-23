---
layout: default
title: LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry
---

# LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry
**arXiv**：[2512.19629v1](https://arxiv.org/abs/2512.19629) · [PDF](https://arxiv.org/pdf/2512.19629.pdf)  
**作者**：Jiaqi Peng, Wenzhe Cai, Yuqiang Yang, Tai Wang, Yuan Shen, Jiangmiao Pang  

**一句话要点**：提出LoGoPlanner以解决无结构环境中端到端导航的定位依赖与误差传播问题

**关键词**：端到端导航, 视觉几何, 度量感知, 定位接地, 无结构环境, 机器人规划

## 3 点简述
- 传统模块化导航方法存在延迟和级联误差，端到端方法依赖外部定位模块限制泛化
- 通过微调视觉几何骨干实现绝对度量尺度预测，重建历史观测几何提供环境感知，基于隐式几何条件化策略
- 在仿真和真实世界评估中，减少累积误差，提升规划一致性和避障，优于基线27.3%并泛化良好

## 摘要（原文）

> Trajectory planning in unstructured environments is a fundamental and challenging capability for mobile robots. Traditional modular pipelines suffer from latency and cascading errors across perception, localization, mapping, and planning modules. Recent end-to-end learning methods map raw visual observations directly to control signals or trajectories, promising greater performance and efficiency in open-world settings. However, most prior end-to-end approaches still rely on separate localization modules that depend on accurate sensor extrinsic calibration for self-state estimation, thereby limiting generalization across embodiments and environments. We introduce LoGoPlanner, a localization-grounded, end-to-end navigation framework that addresses these limitations by: (1) finetuning a long-horizon visual-geometry backbone to ground predictions with absolute metric scale, thereby providing implicit state estimation for accurate localization; (2) reconstructing surrounding scene geometry from historical observations to supply dense, fine-grained environmental awareness for reliable obstacle avoidance; and (3) conditioning the policy on implicit geometry bootstrapped by the aforementioned auxiliary tasks, thereby reducing error propagation.We evaluate LoGoPlanner in both simulation and real-world settings, where its fully end-to-end design reduces cumulative error while metric-aware geometry memory enhances planning consistency and obstacle avoidance, leading to more than a 27.3\% improvement over oracle-localization baselines and strong generalization across embodiments and environments. The code and models have been made publicly available on the \href{https://steinate.github.io/logoplanner.github.io/}{project page}.

