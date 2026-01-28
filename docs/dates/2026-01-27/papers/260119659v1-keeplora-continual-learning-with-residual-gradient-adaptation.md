---
layout: default
title: KeepLoRA: Continual Learning with Residual Gradient Adaptation
---

# KeepLoRA: Continual Learning with Residual Gradient Adaptation
**arXiv**：[2601.19659v1](https://arxiv.org/abs/2601.19659) · [PDF](https://arxiv.org/pdf/2601.19659.pdf)  
**作者**：Mao-Lin Luo, Zi-Hao Zhou, Yi-Lin Zhang, Yuanyu Wan, Tong Wei, Min-Ling Zhang  

**一句话要点**：提出KeepLoRA方法，通过残差梯度适应解决预训练视觉语言模型的持续学习问题。

**关键词**：持续学习, 视觉语言模型, 残差梯度适应, 知识保留, LoRA参数更新, 任务特定知识

## 3 点简述
- 核心问题：持续学习中需平衡预训练知识保留、已学任务知识保持和新知识获取能力。
- 方法要点：分析参数空间，将任务特定知识限制在残差子空间更新，避免干扰先前能力。
- 实验或效果：理论分析和实证验证表明，KeepLoRA有效平衡目标并实现先进性能。

## 摘要（原文）

> Continual learning for pre-trained vision-language models requires balancing three competing objectives: retaining pre-trained knowledge, preserving knowledge from a sequence of learned tasks, and maintaining the plasticity to acquire new knowledge. This paper presents a simple but effective approach called KeepLoRA to effectively balance these objectives. We first analyze the knowledge retention mechanism within the model parameter space and find that general knowledge is mainly encoded in the principal subspace, while task-specific knowledge is encoded in the residual subspace. Motivated by this finding, KeepLoRA learns new tasks by restricting LoRA parameter updates in the residual subspace to prevent interfering with previously learned capabilities. Specifically, we infuse knowledge for a new task by projecting its gradient onto a subspace orthogonal to both the principal subspace of pre-trained model and the dominant directions of previous task features. Our theoretical and empirical analyses confirm that KeepLoRA balances the three objectives and achieves state-of-the-art performance. The implementation code is available at https://github.com/MaolinLuo/KeepLoRA.

