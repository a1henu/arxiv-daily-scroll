---
layout: default
title: An Adaptive Inspection Planning Approach Towards Routine Monitoring in Uncertain Environments
---

# An Adaptive Inspection Planning Approach Towards Routine Monitoring in Uncertain Environments
**arXiv**：[2510.24554v1](https://arxiv.org/abs/2510.24554) · [PDF](https://arxiv.org/pdf/2510.24554.pdf)  
**作者**：Vignesh Kottayam Viswanathan, Yifan Bai, Scott Fredriksson, Sumeet Satpute, Christoforos Kanellakis, George Nikolakopoulos  

**一句话要点**：提出分层框架以在不确定环境中实现机器人自适应巡检

**关键词**：机器人巡检, 环境不确定性, 分层规划, 自适应控制, 四足机器人, 地下环境

## 3 点简述
- 核心问题：环境模型与实际条件差异导致巡检路径失效
- 方法要点：结合全局视图规划和局部视图重规划以保持覆盖
- 实验或效果：在真实地下矿井中验证，使用四足机器人完成巡检

## 摘要（原文）

> In this work, we present a hierarchical framework designed to support robotic
> inspection under environment uncertainty. By leveraging a known environment
> model, existing methods plan and safely track inspection routes to visit points
> of interest. However, discrepancies between the model and actual site
> conditions, caused by either natural or human activities, can alter the surface
> morphology or introduce path obstructions. To address this challenge, the
> proposed framework divides the inspection task into: (a) generating the initial
> global view-plan for region of interests based on a historical map and (b)
> local view replanning to adapt to the current morphology of the inspection
> scene. The proposed hierarchy preserves global coverage objectives while
> enabling reactive adaptation to the local surface morphology. This enables the
> local autonomy to remain robust against environment uncertainty and complete
> the inspection tasks. We validate the approach through deployments in
> real-world subterranean mines using quadrupedal robot.

