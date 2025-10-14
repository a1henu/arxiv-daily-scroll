---
layout: default
title: Placeit! A Framework for Learning Robot Object Placement Skills
---

# Placeit! A Framework for Learning Robot Object Placement Skills
**arXiv**：[2510.09267v1](https://arxiv.org/abs/2510.09267) · [PDF](https://arxiv.org/pdf/2510.09267.pdf)  
**作者**：Amina Ferrad, Johann Huber, François Hélénon, Julien Gleyze, Mahdi Khoramshahi, Stéphane Doncieux  

**一句话要点**：提出Placeit!框架，通过进化计算生成机器人物体放置技能，解决数据获取瓶颈。

**关键词**：机器人放置技能, 进化计算, 质量多样性优化, 仿真数据生成, 拾放任务

## 3 点简述
- 核心问题：机器人物体放置技能学习面临大规模高质量数据获取困难。
- 方法要点：基于进化计算和质量多样性优化，自动生成多样有效放置位姿。
- 实验或效果：在真实世界部署中，基于框架的拾放管道成功率高达90%。

## 摘要（原文）

> Robotics research has made significant strides in learning, yet mastering
> basic skills like object placement remains a fundamental challenge. A key
> bottleneck is the acquisition of large-scale, high-quality data, which is often
> a manual and laborious process. Inspired by Graspit!, a foundational work that
> used simulation to automatically generate dexterous grasp poses, we introduce
> Placeit!, an evolutionary-computation framework for generating valid placement
> positions for rigid objects. Placeit! is highly versatile, supporting tasks
> from placing objects on tables to stacking and inserting them. Our experiments
> show that by leveraging quality-diversity optimization, Placeit! significantly
> outperforms state-of-the-art methods across all scenarios for generating
> diverse valid poses. A pick&place pipeline built on our framework achieved a
> 90% success rate over 120 real-world deployments. This work positions Placeit!
> as a powerful tool for open-environment pick-and-place tasks and as a valuable
> engine for generating the data needed to train simulation-based foundation
> models in robotics.

