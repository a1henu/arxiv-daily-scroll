---
layout: default
title: LLM-Driven Scenario-Aware Planning for Autonomous Driving
---

# LLM-Driven Scenario-Aware Planning for Autonomous Driving
**arXiv**：[2601.21876v1](https://arxiv.org/abs/2601.21876) · [PDF](https://arxiv.org/pdf/2601.21876.pdf)  
**作者**：He Li, Zhaowei Chen, Rui Gao, Guoliang Li, Qi Hao, Shuai Wang, Chengzhong Xu  

**一句话要点**：提出LLM驱动的自适应规划方法LAP，以解决自动驾驶中混合规划器切换的可靠性和效率问题。

**关键词**：自动驾驶规划, 大语言模型应用, 混合规划器切换, 场景理解, 模型预测控制, 联合优化

## 3 点简述
- 核心问题：现有混合规划器切换方法在密集交通中因启发式场景识别和低频控制更新，导致模式切换不可靠和驾驶效率低。
- 方法要点：利用大语言模型进行场景理解，通过树搜索模型预测控制和交替最小化，联合优化模式配置与运动规划。
- 实验或效果：在ROS中实现LAP，高保真仿真显示其在驾驶时间和成功率上优于基准方法。

## 摘要（原文）

> Hybrid planner switching framework (HPSF) for autonomous driving needs to reconcile high-speed driving efficiency with safe maneuvering in dense traffic. Existing HPSF methods often fail to make reliable mode transitions or sustain efficient driving in congested environments, owing to heuristic scene recognition and low-frequency control updates. To address the limitation, this paper proposes LAP, a large language model (LLM) driven, adaptive planning method, which switches between high-speed driving in low-complexity scenes and precise driving in high-complexity scenes, enabling high qualities of trajectory generation through confined gaps. This is achieved by leveraging LLM for scene understanding and integrating its inference into the joint optimization of mode configuration and motion planning. The joint optimization is solved using tree-search model predictive control and alternating minimization. We implement LAP by Python in Robot Operating System (ROS). High-fidelity simulation results show that the proposed LAP outperforms other benchmarks in terms of both driving time and success rate.

