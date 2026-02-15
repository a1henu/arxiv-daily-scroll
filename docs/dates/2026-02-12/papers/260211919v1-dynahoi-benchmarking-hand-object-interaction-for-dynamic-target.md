---
layout: default
title: DynaHOI: Benchmarking Hand-Object Interaction for Dynamic Target
---

# DynaHOI: Benchmarking Hand-Object Interaction for Dynamic Target
**arXiv**：[2602.11919v1](https://arxiv.org/abs/2602.11919) · [PDF](https://arxiv.org/pdf/2602.11919.pdf)  
**作者**：BoCheng Hu, Zhonghan Zhao, Kaiyue Zhou, Hongwei Wang, Gaoang Wang  

**一句话要点**：提出DynaHOI基准以解决动态手物交互场景的评测空白

**关键词**：手物交互, 动态目标, 运动生成基准, 在线闭环平台, 大规模数据集, 时空注意力

## 3 点简述
- 现有手物交互基准多针对静态物体，缺乏动态目标与时间协调的测试
- 引入DynaHOI-Gym平台，集成参数化运动生成器和基于rollout的评估指标
- 发布DynaHOI-10M大规模数据集，并展示ObAct基线方法提升8.1%成功率

## 摘要（原文）

> Most existing hand motion generation benchmarks for hand-object interaction (HOI) focus on static objects, leaving dynamic scenarios with moving targets and time-critical coordination largely untested. To address this gap, we introduce the DynaHOI-Gym, a unified online closed-loop platform with parameterized motion generators and rollout-based metrics for dynamic capture evaluation. Built on DynaHOI-Gym, we release DynaHOI-10M, a large-scale benchmark with 10M frames and 180K hand capture trajectories, whose target motions are organized into 8 major categories and 22 fine-grained subcategories. We also provide a simple observe-before-act baseline (ObAct) that integrates short-term observations with the current frame via spatiotemporal attention to predict actions, achieving an 8.1% improvement in location success rate.

