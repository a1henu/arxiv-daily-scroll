---
layout: default
title: InternData-A1: Pioneering High-Fidelity Synthetic Data for Pre-training Generalist Policy
---

# InternData-A1: Pioneering High-Fidelity Synthetic Data for Pre-training Generalist Policy
**arXiv**：[2511.16651v1](https://arxiv.org/abs/2511.16651) · [PDF](https://arxiv.org/pdf/2511.16651.pdf)  
**作者**：Yang Tian, Yuyin Yang, Yiman Xie, Zetao Cai, Xu Shi, Ning Gao, Hangxu Liu, Xuekun Jiang, Zherui Qiu, Feng Yuan, Yaping Li, Ping Wang, Junhao Cai, Jia Zeng, Hao Dong, Jiangmiao Pang  

**一句话要点**：提出InternData-A1合成数据集，用于预训练通用策略模型，匹配真实数据性能。

**关键词**：合成数据生成, 视觉语言动作模型, 机器人预训练, 零样本迁移, 仿真到真实, 长时程技能

## 3 点简述
- 核心问题：合成数据在VLA模型预训练中未达大规模真实数据效果。
- 方法要点：构建大规模合成数据集，支持多技能、任务和场景的自主生成。
- 实验或效果：模型在仿真和真实任务中匹配π_0，实现零样本迁移。

## 摘要（原文）

> Recent works explore how real and synthetic data contribute to Vision-Language-Action (VLA) models' generalization. While current VLA models have shown the strong effectiveness of large-scale real-robot pre-training, synthetic data has not previously demonstrated comparable capability at scale. This paper provides the first evidence that synthetic data alone can match the performance of the strongest $π$-dataset in pre-training a VLA model, revealing the substantial value of large-scale simulation. The resulting model also exhibits surprisingly zero-shot sim-to-real transfer on several challenging tasks. Our synthetic dataset, InternData-A1, contains over 630k trajectories and 7,433 hours across 4 embodiments, 18 skills, 70 tasks, and 227 scenes, covering rigid, articulated, deformable, and fluid-object manipulation. It is generated through a highly autonomous, fully decoupled, and compositional simulation pipeline that enables long-horizon skill composition, flexible task assembly, and heterogeneous embodiments with minimal manual tuning. Using the same architecture as $π_0$, we pre-train a model entirely on InternData-A1 and find that it matches the official $π_0$ across 49 simulation tasks, 5 real-world tasks, and 4 long-horizon dexterous tasks. We release the dataset and will open-source the generation pipeline to broaden access to large-scale robotic data and to lower the barrier to scalable data creation for embodied AI research.

