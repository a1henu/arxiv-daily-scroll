---
layout: default
title: Bus-Conditioned Zero-Shot Trajectory Generation via Task Arithmetic
---

# Bus-Conditioned Zero-Shot Trajectory Generation via Task Arithmetic
**arXiv**：[2602.13071v1](https://arxiv.org/abs/2602.13071) · [PDF](https://arxiv.org/pdf/2602.13071.pdf)  
**作者**：Shuai Liu, Ning Cao, Yile Chen, Yue Jiang, Gao Cong  

**一句话要点**：提出MobTA方法，通过任务算术实现基于公交时刻表的零样本轨迹生成

**关键词**：轨迹生成, 零样本学习, 任务算术, 移动数据, 智能城市, 公交时刻表

## 3 点简述
- 核心问题：目标城市无移动轨迹数据时，现有轨迹生成方法受限，需新零样本设置
- 方法要点：利用源城市数据和公交时刻表，建模参数偏移并通过任务算术迁移至目标城市
- 实验或效果：MobTA显著优于现有方法，性能接近使用目标城市数据微调的模型

## 摘要（原文）

> Mobility trajectory data provide essential support for smart city applications. However, such data are often difficult to obtain. Meanwhile, most existing trajectory generation methods implicitly assume that at least a subset of real mobility data from target city is available, which limits their applicability in data-inaccessible scenarios. In this work, we propose a new problem setting, called bus-conditioned zero-shot trajectory generation, where no mobility trajectories from a target city are accessible. The generation process relies solely on source city mobility data and publicly available bus timetables from both cities. Under this setting, we propose MobTA, the first approach to introduce task arithmetic into trajectory generation. MobTA models the parameter shift from bus-timetable-based trajectory generation to mobility trajectory generation in source city, and applies this shift to target city through arithmetic operations on task vectors. This enables trajectory generation that reflects target-city mobility patterns without requiring any real mobility data from it. Furthermore, we theoretically analyze MobTA's stability across base and instruction-tuned LLMs. Extensive experiments show that MobTA significantly outperforms existing methods, and achieves performance close to models finetuned using target city mobility trajectories.

