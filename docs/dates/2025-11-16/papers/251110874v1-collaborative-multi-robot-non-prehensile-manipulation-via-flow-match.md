---
layout: default
title: Collaborative Multi-Robot Non-Prehensile Manipulation via Flow-Matching Co-Generation
---

# Collaborative Multi-Robot Non-Prehensile Manipulation via Flow-Matching Co-Generation
**arXiv**：[2511.10874v1](https://arxiv.org/abs/2511.10874) · [PDF](https://arxiv.org/pdf/2511.10874.pdf)  
**作者**：Yorai Shaoul, Zhe Chen, Mohamed Naveed Gul Mohamed, Federico Pecora, Maxim Likhachev, Jiaoyang Li  

**一句话要点**：提出基于流匹配协同生成与匿名运动规划的协作多机器人非抓取操作框架

**关键词**：多机器人协作, 非抓取操作, 流匹配生成, 运动规划, 多物体重定位

## 3 点简述
- 核心问题：多机器人在杂乱环境中协同重定位多物体，需联合推理接触、操作与导航。
- 方法要点：集成流匹配协同生成模型与匿名多机器人运动规划，统一机器人级和物体级协调。
- 实验效果：在模拟环境中优于基线，验证生成协同设计与集成规划的有效性。

## 摘要（原文）

> Coordinating a team of robots to reposition multiple objects in cluttered environments requires reasoning jointly about where robots should establish contact, how to manipulate objects once contact is made, and how to navigate safely and efficiently at scale. Prior approaches typically fall into two extremes -- either learning the entire task or relying on privileged information and hand-designed planners -- both of which struggle to handle diverse objects in long-horizon tasks. To address these challenges, we present a unified framework for collaborative multi-robot, multi-object non-prehensile manipulation that integrates flow-matching co-generation with anonymous multi-robot motion planning. Within this framework, a generative model co-generates contact formations and manipulation trajectories from visual observations, while a novel motion planner conveys robots at scale. Crucially, the same planner also supports coordination at the object level, assigning manipulated objects to larger target structures and thereby unifying robot- and object-level reasoning within a single algorithmic framework. Experiments in challenging simulated environments demonstrate that our approach outperforms baselines in both motion planning and manipulation tasks, highlighting the benefits of generative co-design and integrated planning for scaling collaborative manipulation to complex multi-agent, multi-object settings. Visit gco-paper.github.io for code and demonstrations.

