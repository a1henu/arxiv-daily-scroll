---
layout: default
title: UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data
---

# UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data
**arXiv**：[2603.05312v1](https://arxiv.org/abs/2603.05312) · [PDF](https://arxiv.org/pdf/2603.05312.pdf)  
**作者**：Sizhe Yang, Yiman Xie, Zhixuan Liang, Yang Tian, Jia Zeng, Dahua Lin, Jiangmiao Pang  

**一句话要点**：提出UltraDexGrasp框架，利用合成数据解决双手机器人灵巧抓取的通用性问题。

**关键词**：双手机器人抓取, 合成数据生成, 灵巧抓取策略, 零样本迁移, 大规模数据集

## 3 点简述
- 核心问题：双手机器人灵巧抓取数据稀缺，难以实现物理合理且几何适配的抓取。
- 方法要点：集成优化抓取合成与规划演示生成，构建大规模多策略数据集UltraDexGrasp-20M。
- 实验或效果：基于点云输入和注意力机制，策略在真实世界零样本迁移中平均成功率81.2%。

## 摘要（原文）

> Grasping is a fundamental capability for robots to interact with the physical world. Humans, equipped with two hands, autonomously select appropriate grasp strategies based on the shape, size, and weight of objects, enabling robust grasping and subsequent manipulation. In contrast, current robotic grasping remains limited, particularly in multi-strategy settings. Although substantial efforts have targeted parallel-gripper and single-hand grasping, dexterous grasping for bimanual robots remains underexplored, with data being a primary bottleneck. Achieving physically plausible and geometrically conforming grasps that can withstand external wrenches poses significant challenges. To address these issues, we introduce UltraDexGrasp, a framework for universal dexterous grasping with bimanual robots. The proposed data-generation pipeline integrates optimization-based grasp synthesis with planning-based demonstration generation, yielding high-quality and diverse trajectories across multiple grasp strategies. With this framework, we curate UltraDexGrasp-20M, a large-scale, multi-strategy grasp dataset comprising 20 million frames across 1,000 objects. Based on UltraDexGrasp-20M, we further develop a simple yet effective grasp policy that takes point clouds as input, aggregates scene features via unidirectional attention, and predicts control commands. Trained exclusively on synthetic data, the policy achieves robust zero-shot sim-to-real transfer and consistently succeeds on novel objects with varied shapes, sizes, and weights, attaining an average success rate of 81.2% in real-world universal dexterous grasping. To facilitate future research on grasping with bimanual robots, we open-source the data generation pipeline at https://github.com/InternRobotics/UltraDexGrasp.

