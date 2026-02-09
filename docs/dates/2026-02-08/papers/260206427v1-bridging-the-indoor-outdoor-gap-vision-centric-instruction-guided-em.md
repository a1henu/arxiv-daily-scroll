---
layout: default
title: Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters
---

# Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters
**arXiv**：[2602.06427v1](https://arxiv.org/abs/2602.06427) · [PDF](https://arxiv.org/pdf/2602.06427.pdf)  
**作者**：Yuxiang Zhao, Yirong Yang, Yanqing Zhu, Yanfen Shen, Chiyu Wang, Zhining Gu, Pei Shi, Wei Guo, Mu Xu  

**一句话要点**：提出视觉中心指令引导的具身导航框架，以解决室外到室内无缝过渡的最后一米导航问题。

**关键词**：具身导航, 视觉中心导航, 指令驱动导航, 室外到室内过渡, 无先验导航, 轨迹条件视频合成

## 3 点简述
- 核心问题：现有方法局限于室内或室外环境，依赖精确坐标，无法实现从室外到室内的精细入口导航。
- 方法要点：引入无先验指令驱动的具身导航任务，基于视觉观察和指令进行决策，利用图像提示驱动框架。
- 实验或效果：通过开源数据集和实验，在成功率与路径效率上优于现有基线方法。

## 摘要（原文）

> Embodied navigation holds significant promise for real-world applications such as last-mile delivery. However, most existing approaches are confined to either indoor or outdoor environments and rely heavily on strong assumptions, such as access to precise coordinate systems. While current outdoor methods can guide agents to the vicinity of a target using coarse-grained localization, they fail to enable fine-grained entry through specific building entrances, critically limiting their utility in practical deployment scenarios that require seamless outdoor-to-indoor transitions. To bridge this gap, we introduce a novel task: out-to-in prior-free instruction-driven embodied navigation. This formulation explicitly eliminates reliance on accurate external priors, requiring agents to navigate solely based on egocentric visual observations guided by instructions. To tackle this task, we propose a vision-centric embodied navigation framework that leverages image-based prompts to drive decision-making. Additionally, we present the first open-source dataset for this task, featuring a pipeline that integrates trajectory-conditioned video synthesis into the data generation process. Through extensive experiments, we demonstrate that our proposed method consistently outperforms state-of-the-art baselines across key metrics including success rate and path efficiency.

