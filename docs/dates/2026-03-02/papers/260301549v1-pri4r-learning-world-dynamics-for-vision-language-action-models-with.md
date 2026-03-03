---
layout: default
title: Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation
---

# Pri4R: Learning World Dynamics for Vision-Language-Action Models with Privileged 4D Representation
**arXiv**：[2603.01549v1](https://arxiv.org/abs/2603.01549) · [PDF](https://arxiv.org/pdf/2603.01549.pdf)  
**作者**：Jisoo Kim, Jungbin Cho, Sanghyeok Chu, Ananya Bal, Jinhyung Kim, Gunhee Lee, Sihaeng Lee, Seung Hwan Kim, Bohyung Han, Hyunmin Lee, Laszlo A. Jeni, Seungryong Kim  

**一句话要点**：提出Pri4R方法，通过特权4D表示学习世界动态，增强视觉-语言-动作模型的物理交互能力。

**关键词**：视觉-语言-动作模型, 世界动态学习, 3D点轨迹预测, 特权学习, 机器人操作, 时空表示

## 3 点简述
- 核心问题：现有视觉-语言-动作模型缺乏对物理世界时空动态的理解，影响精确控制。
- 方法要点：训练时利用特权4D信息，通过轻量级点轨迹头预测3D点轨迹，注入VLA特征以学习场景几何演化。
- 实验或效果：在仿真和真实世界评估中显著提升操作任务性能，如LIBERO-Long提升10%，RoboCasa提升40%。

## 摘要（原文）

> Humans learn not only how their bodies move, but also how the surrounding world responds to their actions. In contrast, while recent Vision-Language-Action (VLA) models exhibit impressive semantic understanding, they often fail to capture the spatiotemporal dynamics governing physical interaction. In this paper, we introduce Pri4R, a simple yet effective approach that endows VLA models with an implicit understanding of world dynamics by leveraging privileged 4D information during training. Specifically, Pri4R augments VLAs with a lightweight point track head that predicts 3D point tracks. By injecting VLA features into this head to jointly predict future 3D trajectories, the model learns to incorporate evolving scene geometry within its shared representation space, enabling more physically aware context for precise control. Due to its architectural simplicity, Pri4R is compatible with dominant VLA design patterns with minimal changes. During inference, we run the model using the original VLA architecture unchanged; Pri4R adds no extra inputs, outputs, or computational overhead. Across simulation and real-world evaluations, Pri4R significantly improves performance on challenging manipulation tasks, including a +10% gain on LIBERO-Long and a +40% gain on RoboCasa. We further show that 3D point track prediction is an effective supervision target for learning action-world dynamics, and validate our design choices through extensive ablations.

