---
layout: default
title: LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models
---

# LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models
**arXiv**：[2511.07727v1](https://arxiv.org/abs/2511.07727) · [PDF](https://arxiv.org/pdf/2511.07727.pdf)  
**作者**：Xiaohan Zhang, Yan Ding, Yohei Hayamizu, Zainab Altaweel, Yifeng Zhu, Yuke Zhu, Peter Stone, Chris Paxton, Shiqi Zhang  

**一句话要点**：提出LLM-GROP框架，结合大语言模型与视觉方法解决移动操作任务规划问题

**关键词**：任务与运动规划, 大语言模型, 移动操作, 物体重排, 视觉基础, 机器人导航

## 3 点简述
- 核心问题：移动操作中任务与运动规划的结合，处理多物体放置的模糊目标
- 方法要点：利用大语言模型常识知识指导任务规划，视觉方法选择机器人基位置
- 实验或效果：真实世界实验成功率84.4%，但性能低于人类服务员

## 摘要（原文）

> Task planning and motion planning are two of the most important problems in robotics, where task planning methods help robots achieve high-level goals and motion planning methods maintain low-level feasibility. Task and motion planning (TAMP) methods interleave the two processes of task planning and motion planning to ensure goal achievement and motion feasibility. Within the TAMP context, we are concerned with the mobile manipulation (MoMa) of multiple objects, where it is necessary to interleave actions for navigation and manipulation.
>   In particular, we aim to compute where and how each object should be placed given underspecified goals, such as ``set up dinner table with a fork, knife and plate.'' We leverage the rich common sense knowledge from large language models (LLMs), e.g., about how tableware is organized, to facilitate both task-level and motion-level planning. In addition, we use computer vision methods to learn a strategy for selecting base positions to facilitate MoMa behaviors, where the base position corresponds to the robot's ``footprint'' and orientation in its operating space. Altogether, this article provides a principled TAMP framework for MoMa tasks that accounts for common sense about object rearrangement and is adaptive to novel situations that include many objects that need to be moved. We performed quantitative experiments in both real-world settings and simulated environments. We evaluated the success rate and efficiency in completing long-horizon object rearrangement tasks. While the robot completed 84.4\% real-world object rearrangement trials, subjective human evaluations indicated that the robot's performance is still lower than experienced human waiters.

