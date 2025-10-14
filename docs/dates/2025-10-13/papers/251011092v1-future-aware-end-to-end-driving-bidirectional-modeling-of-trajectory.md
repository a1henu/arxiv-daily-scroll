---
layout: default
title: Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution
---

# Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution
**arXiv**：[2510.11092v1](https://arxiv.org/abs/2510.11092) · [PDF](https://arxiv.org/pdf/2510.11092.pdf)  
**作者**：Bozhou Zhang, Nan Song, Jingyu Li, Xiatian Zhu, Jiankang Deng, Li Zhang  

**一句话要点**：提出SeerDrive框架，通过双向建模轨迹规划与场景演化以提升端到端自动驾驶性能

**关键词**：端到端自动驾驶, 轨迹规划, 场景演化预测, 鸟瞰图表示, 闭环建模, 双向关系

## 3 点简述
- 核心问题：端到端自动驾驶方法依赖当前场景，低估动态演化，限制复杂场景决策能力
- 方法要点：联合建模未来场景BEV预测与轨迹规划，实现闭环迭代优化
- 实验或效果：在NAVSIM和nuScenes基准上显著优于现有先进方法

## 摘要（原文）

> End-to-end autonomous driving methods aim to directly map raw sensor inputs
> to future driving actions such as planned trajectories, bypassing traditional
> modular pipelines. While these approaches have shown promise, they often
> operate under a one-shot paradigm that relies heavily on the current scene
> context, potentially underestimating the importance of scene dynamics and their
> temporal evolution. This limitation restricts the model's ability to make
> informed and adaptive decisions in complex driving scenarios. We propose a new
> perspective: the future trajectory of an autonomous vehicle is closely
> intertwined with the evolving dynamics of its environment, and conversely, the
> vehicle's own future states can influence how the surrounding scene unfolds.
> Motivated by this bidirectional relationship, we introduce SeerDrive, a novel
> end-to-end framework that jointly models future scene evolution and trajectory
> planning in a closed-loop manner. Our method first predicts future bird's-eye
> view (BEV) representations to anticipate the dynamics of the surrounding scene,
> then leverages this foresight to generate future-context-aware trajectories.
> Two key components enable this: (1) future-aware planning, which injects
> predicted BEV features into the trajectory planner, and (2) iterative scene
> modeling and vehicle planning, which refines both future scene prediction and
> trajectory generation through collaborative optimization. Extensive experiments
> on the NAVSIM and nuScenes benchmarks show that SeerDrive significantly
> outperforms existing state-of-the-art methods.

