---
layout: default
title: RFS: Reinforcement learning with Residual flow steering for dexterous manipulation
---

# RFS: Reinforcement learning with Residual flow steering for dexterous manipulation
**arXiv**：[2602.01789v1](https://arxiv.org/abs/2602.01789) · [PDF](https://arxiv.org/pdf/2602.01789.pdf)  
**作者**：Entong Su, Tyler Westenbroek, Anusha Nagabandi, Abhishek Gupta  

**一句话要点**：提出残差流引导强化学习框架，用于灵巧操作中预训练生成策略的高效微调。

**关键词**：强化学习, 生成策略微调, 残差流引导, 灵巧操作, 模仿学习, 流匹配

## 3 点简述
- 核心问题：基于模仿学习的预训练生成策略泛化能力有限，部署时需额外微调以提升鲁棒性。
- 方法要点：通过联合优化残差动作和潜在噪声分布，实现局部修正和全局探索的互补，保留预训练策略的表达结构。
- 实验或效果：在灵巧操作任务中，仿真和真实世界设置下均展示高效微调能力，提升部署性能。

## 摘要（原文）

> Imitation learning has emerged as an effective approach for bootstrapping sequential decision-making in robotics, achieving strong performance even in high-dimensional dexterous manipulation tasks. Recent behavior cloning methods further leverage expressive generative models, such as diffusion models and flow matching, to represent multimodal action distributions. However, policies pretrained in this manner often exhibit limited generalization and require additional fine-tuning to achieve robust performance at deployment time. Such adaptation must preserve the global exploration benefits of pretraining while enabling rapid correction of local execution errors.We propose \emph{Residual Flow Steering} (RFS), a data-efficient reinforcement learning framework for adapting pretrained generative policies. RFS steers a pretrained flow-matching policy by jointly optimizing a residual action and a latent noise distribution, enabling complementary forms of exploration: local refinement through residual corrections and global exploration through latent-space modulation. This design allows efficient adaptation while retaining the expressive structure of the pretrained policy.We demonstrate the effectiveness of RFS on dexterous manipulation tasks, showing efficient fine-tuning both in simulation and in real-world settings when adapting pretrained base policies.Project website:https://weirdlabuw.github.io/rfs.

