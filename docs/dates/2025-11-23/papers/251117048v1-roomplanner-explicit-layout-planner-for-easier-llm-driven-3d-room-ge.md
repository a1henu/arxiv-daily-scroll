---
layout: default
title: RoomPlanner: Explicit Layout Planner for Easier LLM-Driven 3D Room Generation
---

# RoomPlanner: Explicit Layout Planner for Easier LLM-Driven 3D Room Generation
**arXiv**：[2511.17048v1](https://arxiv.org/abs/2511.17048) · [PDF](https://arxiv.org/pdf/2511.17048.pdf)  
**作者**：Wenzhuo Sun, Mingjian Liang, Wenxuan Song, Xuelian Cheng, Zongyuan Ge  

**一句话要点**：提出RoomPlanner框架，通过显式布局规划实现基于LLM的3D房间自动生成

**关键词**：3D房间生成, 显式布局规划, 语言驱动代理, 空间优化约束, 高效渲染采样

## 3 点简述
- 核心问题：短文本输入下自动生成几何合理的3D室内场景，无需手动布局或全景图像指导
- 方法要点：使用分层语言代理解析提示，结合布局约束优化空间排列，并采用高效采样策略渲染
- 实验或效果：生成时间低于30分钟，在渲染速度和视觉质量上超越先前方法，保持可编辑性

## 摘要（原文）

> In this paper, we propose RoomPlanner, the first fully automatic 3D room generation framework for painlessly creating realistic indoor scenes with only short text as input. Without any manual layout design or panoramic image guidance, our framework can generate explicit layout criteria for rational spatial placement. We begin by introducing a hierarchical structure of language-driven agent planners that can automatically parse short and ambiguous prompts into detailed scene descriptions. These descriptions include raw spatial and semantic attributes for each object and the background, which are then used to initialize 3D point clouds. To position objects within bounded environments, we implement two arrangement constraints that iteratively optimize spatial arrangements, ensuring a collision-free and accessible layout solution. In the final rendering stage, we propose a novel AnyReach Sampling strategy for camera trajectory, along with the Interval Timestep Flow Sampling (ITFS) strategy, to efficiently optimize the coarse 3D Gaussian scene representation. These approaches help reduce the total generation time to under 30 minutes. Extensive experiments demonstrate that our method can produce geometrically rational 3D indoor scenes, surpassing prior approaches in both rendering speed and visual quality while preserving editability. The code will be available soon.

