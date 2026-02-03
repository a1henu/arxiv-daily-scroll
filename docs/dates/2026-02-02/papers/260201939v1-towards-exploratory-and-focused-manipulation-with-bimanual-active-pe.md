---
layout: default
title: Towards Exploratory and Focused Manipulation with Bimanual Active Perception: A New Problem, Benchmark and Strategy
---

# Towards Exploratory and Focused Manipulation with Bimanual Active Perception: A New Problem, Benchmark and Strategy
**arXiv**：[2602.01939v1](https://arxiv.org/abs/2602.01939) · [PDF](https://arxiv.org/pdf/2602.01939.pdf)  
**作者**：Yuxin He, Ruihao Zhang, Tianao Shen, Cheng Liu, Qiang Nie  

**一句话要点**：提出双手机器人主动感知策略以解决探索与聚焦操作中的视觉遮挡问题

**关键词**：探索与聚焦操作, 双手机器人, 主动感知, 视觉遮挡, 模仿学习, 基准数据集

## 3 点简述
- 核心问题：定义探索与聚焦操作问题，强调主动收集信息以完成复杂任务
- 方法要点：设计双手机器人主动感知策略，一臂提供主动视觉，另一臂提供力感知
- 实验或效果：建立EFM-10基准和BAPData数据集，通过模仿学习验证策略有效性

## 摘要（原文）

> Recently, active vision has reemerged as an important concept for manipulation, since visual occlusion occurs more frequently when main cameras are mounted on the robot heads. We reflect on the visual occlusion issue and identify its essence as the absence of information useful for task completion. Inspired by this, we come up with the more fundamental problem of Exploratory and Focused Manipulation (EFM). The proposed problem is about actively collecting information to complete challenging manipulation tasks that require exploration or focus. As an initial attempt to address this problem, we establish the EFM-10 benchmark that consists of 4 categories of tasks that align with our definition (10 tasks in total). We further come up with a Bimanual Active Perception (BAP) strategy, which leverages one arm to provide active vision and another arm to provide force sensing while manipulating. Based on this idea, we collect a dataset named BAPData for the tasks in EFM-10. With the dataset, we successfully verify the effectiveness of the BAP strategy in an imitation learning manner. We hope that the EFM-10 benchmark along with the BAP strategy can become a cornerstone that facilitates future research towards this direction. Project website: EFManipulation.github.io.

