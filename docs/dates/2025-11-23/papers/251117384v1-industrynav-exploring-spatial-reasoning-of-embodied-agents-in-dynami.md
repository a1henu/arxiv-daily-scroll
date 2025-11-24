---
layout: default
title: IndustryNav: Exploring Spatial Reasoning of Embodied Agents in Dynamic Industrial Navigation
---

# IndustryNav: Exploring Spatial Reasoning of Embodied Agents in Dynamic Industrial Navigation
**arXiv**：[2511.17384v1](https://arxiv.org/abs/2511.17384) · [PDF](https://arxiv.org/pdf/2511.17384.pdf)  
**作者**：Yifan Li, Lichi Li, Anh Dao, Xinyu Zhou, Yicheng Qiao, Zheda Mai, Daeun Lee, Zichen Chen, Zhen Tan, Mohit Bansal, Yu Kong  

**一句话要点**：提出IndustryNav基准以评估具身代理在动态工业导航中的空间推理能力

**关键词**：具身智能, 空间推理, 动态导航, 工业环境, 基准评估, 碰撞避免

## 3 点简述
- 现有具身基准在动态真实环境中空间推理评估不足，聚焦静态家庭场景
- 基于12个高保真Unity仓库场景，结合自我中心视觉与全局里程计评估规划
- 引入碰撞率和警告率指标，发现主流VLLMs在路径规划和避障方面存在缺陷

## 摘要（原文）

> While Visual Large Language Models (VLLMs) show great promise as embodied agents, they continue to face substantial challenges in spatial reasoning. Existing embodied benchmarks largely focus on passive, static household environments and evaluate only isolated capabilities, failing to capture holistic performance in dynamic, real-world complexity. To fill this gap, we present IndustryNav, the first dynamic industrial navigation benchmark for active spatial reasoning. IndustryNav leverages 12 manually created, high-fidelity Unity warehouse scenarios featuring dynamic objects and human movement. Our evaluation employs a PointGoal navigation pipeline that effectively combines egocentric vision with global odometry to assess holistic local-global planning. Crucially, we introduce the "collision rate" and "warning rate" metrics to measure safety-oriented behaviors and distance estimation. A comprehensive study of nine state-of-the-art VLLMs (including models such as GPT-5-mini, Claude-4.5, and Gemini-2.5) reveals that closed-source models maintain a consistent advantage; however, all agents exhibit notable deficiencies in robust path planning, collision avoidance and active exploration. This highlights a critical need for embodied research to move beyond passive perception and toward tasks that demand stable planning, active exploration, and safe behavior in dynamic, real-world environment.

