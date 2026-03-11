---
layout: default
title: NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models
---

# NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models
**arXiv**：[2603.09542v1](https://arxiv.org/abs/2603.09542) · [PDF](https://arxiv.org/pdf/2603.09542.pdf)  
**作者**：Ziyue Zhu, Shangyang Wu, Shuai Zhao, Zhiqiu Zhao, Shengjie Li, Yi Wang, Fang Li, Haoran Luo  

**一句话要点**：提出NS-VLA框架，通过在线强化学习解决机器人操作中视觉-语言-动作模型的挑战。

**关键词**：神经符号模型, 视觉-语言-动作, 在线强化学习, 机器人操作, 数据效率, 零样本泛化

## 3 点简述
- 核心问题：VLA模型在可重用原语学习、数据依赖和探索能力方面存在不足。
- 方法要点：引入符号编码器提取结构化原语，符号求解器高效生成动作序列，在线RL优化探索。
- 实验或效果：在机器人操作基准上表现优异，具备高数据效率和零样本泛化能力。

## 摘要（原文）

> Vision-Language-Action (VLA) models are formulated to ground instructions in visual context and generate action sequences for robotic manipulation. Despite recent progress, VLA models still face challenges in learning related and reusable primitives, reducing reliance on large-scale data and complex architectures, and enabling exploration beyond demonstrations. To address these challenges, we propose a novel Neuro-Symbolic Vision-Language-Action (NS-VLA) framework via online reinforcement learning (RL). It introduces a symbolic encoder to embedding vision and language features and extract structured primitives, utilizes a symbolic solver for data-efficient action sequencing, and leverages online RL to optimize generation via expansive exploration. Experiments on robotic manipulation benchmarks demonstrate that NS-VLA outperforms previous methods in both one-shot training and data-perturbed settings, while simultaneously exhibiting superior zero-shot generalizability, high data efficiency and expanded exploration space. Our code is available.

