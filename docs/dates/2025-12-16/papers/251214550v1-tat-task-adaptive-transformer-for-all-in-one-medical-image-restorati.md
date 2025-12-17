---
layout: default
title: TAT: Task-Adaptive Transformer for All-in-One Medical Image Restoration
---

# TAT: Task-Adaptive Transformer for All-in-One Medical Image Restoration
**arXiv**：[2512.14550v1](https://arxiv.org/abs/2512.14550) · [PDF](https://arxiv.org/pdf/2512.14550.pdf)  
**作者**：Zhiwen Yang, Jiaju Zhang, Yang Yi, Jian Liang, Bingzheng Wei, Yan Xu  

**一句话要点**：提出任务自适应Transformer，通过任务自适应权重生成和损失平衡策略解决医学图像修复中的任务干扰与不平衡问题。

**关键词**：医学图像修复, 多任务学习, Transformer, 任务自适应, 梯度冲突, 损失平衡

## 3 点简述
- 核心问题：医学图像修复中，多任务共享模型面临任务干扰和任务不平衡的挑战。
- 方法要点：引入任务自适应权重生成策略，为不同任务生成特定权重参数，避免梯度冲突。
- 实验或效果：在PET合成、CT去噪和MRI超分辨率任务中，TAT在单任务和All-in-One设置下均达到先进性能。

## 摘要（原文）

> Medical image restoration (MedIR) aims to recover high-quality medical images from their low-quality counterparts. Recent advancements in MedIR have focused on All-in-One models capable of simultaneously addressing multiple different MedIR tasks. However, due to significant differences in both modality and degradation types, using a shared model for these diverse tasks requires careful consideration of two critical inter-task relationships: task interference, which occurs when conflicting gradient update directions arise across tasks on the same parameter, and task imbalance, which refers to uneven optimization caused by varying learning difficulties inherent to each task. To address these challenges, we propose a task-adaptive Transformer (TAT), a novel framework that dynamically adapts to different tasks through two key innovations. First, a task-adaptive weight generation strategy is introduced to mitigate task interference by generating task-specific weight parameters for each task, thereby eliminating potential gradient conflicts on shared weight parameters. Second, a task-adaptive loss balancing strategy is introduced to dynamically adjust loss weights based on task-specific learning difficulties, preventing task domination or undertraining. Extensive experiments demonstrate that our proposed TAT achieves state-of-the-art performance in three MedIR tasks--PET synthesis, CT denoising, and MRI super-resolution--both in task-specific and All-in-One settings. Code is available at https://github.com/Yaziwel/TAT.

