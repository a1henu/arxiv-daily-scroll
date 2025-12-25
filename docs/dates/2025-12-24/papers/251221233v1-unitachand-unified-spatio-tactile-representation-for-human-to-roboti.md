---
layout: default
title: UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer
---

# UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer
**arXiv**：[2512.21233v1](https://arxiv.org/abs/2512.21233) · [PDF](https://arxiv.org/pdf/2512.21233.pdf)  
**作者**：Chi Zhang, Penglin Cai, Haoqi Yuan, Chaoyi Xu, Zongqing Lu  

**一句话要点**：提出UniTacHand统一表示，通过对比学习对齐人与机器人触觉数据，实现零样本技能迁移。

**关键词**：触觉感知, 技能迁移, 对比学习, 机器人操作, 统一表示, 数据对齐

## 3 点简述
- 核心问题：机器人触觉数据收集困难，且人与机器人触觉数据存在不对齐，阻碍技能迁移。
- 方法要点：将触觉信号投影到MANO手模型2D表面空间，使用对比学习对齐到统一潜在空间。
- 实验或效果：仅需10分钟配对数据训练，实现零样本迁移至真实机器人，泛化至未见物体，提升性能与数据效率。

## 摘要（原文）

> Tactile sensing is crucial for robotic hands to achieve human-level dexterous manipulation, especially in scenarios with visual occlusion. However, its application is often hindered by the difficulty of collecting large-scale real-world robotic tactile data. In this study, we propose to collect low-cost human manipulation data using haptic gloves for tactile-based robotic policy learning. The misalignment between human and robotic tactile data makes it challenging to transfer policies learned from human data to robots. To bridge this gap, we propose UniTacHand, a unified representation to align robotic tactile information captured by dexterous hands with human hand touch obtained from gloves. First, we project tactile signals from both human hands and robotic hands onto a morphologically consistent 2D surface space of the MANO hand model. This unification standardizes the heterogeneous data structures and inherently embeds the tactile signals with spatial context. Then, we introduce a contrastive learning method to align them into a unified latent space, trained on only 10 minutes of paired data from our data collection system. Our approach enables zero-shot tactile-based policy transfer from humans to a real robot, generalizing to objects unseen in the pre-training data. We also demonstrate that co-training on mixed data, including both human and robotic demonstrations via UniTacHand, yields better performance and data efficiency compared with using only robotic data. UniTacHand paves a path toward general, scalable, and data-efficient learning for tactile-based dexterous hands.

