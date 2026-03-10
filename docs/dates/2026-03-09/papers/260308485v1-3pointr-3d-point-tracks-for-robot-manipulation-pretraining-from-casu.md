---
layout: default
title: 3PoinTr: 3D Point Tracks for Robot Manipulation Pretraining from Casual Videos
---

# 3PoinTr: 3D Point Tracks for Robot Manipulation Pretraining from Casual Videos
**arXiv**：[2603.08485v1](https://arxiv.org/abs/2603.08485) · [PDF](https://arxiv.org/pdf/2603.08485.pdf)  
**作者**：Adam Hung, Bardienus Pieter Duisterhof, Jeffrey Ichnowski  

**一句话要点**：提出3PoinTr方法，通过预测3D点轨迹从随意人类视频预训练机器人策略，以解决数据效率低和具身差距问题。

**关键词**：机器人操作预训练, 3D点轨迹预测, Transformer架构, 行为克隆, 具身差距, 视频学习

## 3 点简述
- 核心问题：机器人策略训练需大量演示，从人类视频学习面临具身差距，限制自然动作应用。
- 方法要点：使用Transformer预测3D点轨迹作为中间表示，结合Perceiver IO提取紧凑特征，支持样本高效行为克隆。
- 实验或效果：在模拟和真实任务中，仅需20个标注演示即实现稳健空间泛化，优于基线方法。

## 摘要（原文）

> Data-efficient training of robust robot policies is the key to unlocking automation in a wide array of novel tasks. Current systems require large volumes of demonstrations to achieve robustness, which is impractical in many applications. Learning policies directly from human videos is a promising alternative that removes teleoperation costs, but it shifts the challenge toward overcoming the embodiment gap (differences in kinematics and strategies between robots and humans), often requiring restrictive and carefully choreographed human motions. We propose 3PoinTr, a method for pretraining robot policies from casual and unconstrained human videos, enabling learning from motions natural for humans. 3PoinTr uses a transformer architecture to predict 3D point tracks as an intermediate embodiment-agnostic representation. 3D point tracks encode goal specifications, scene geometry, and spatiotemporal relationships. We use a Perceiver IO architecture to extract a compact representation for sample-efficient behavior cloning, even when point tracks violate downstream embodiment-specific constraints. We conduct thorough evaluation on simulated and real-world tasks, and find that 3PoinTr achieves robust spatial generalization on diverse categories of manipulation tasks with only 20 action-labeled robot demonstrations. 3PoinTr outperforms the baselines, including behavior cloning methods, as well as prior methods for pretraining from human videos. We also provide evaluations of 3PoinTr's 3D point track predictions compared to an existing point track prediction baseline. We find that 3PoinTr produces more accurate and higher quality point tracks due to a lightweight yet expressive architecture built on a single transformer, in addition to a training formulation that preserves supervision of partially occluded points. Project page: https://adamhung60.github.io/3PoinTr/.

