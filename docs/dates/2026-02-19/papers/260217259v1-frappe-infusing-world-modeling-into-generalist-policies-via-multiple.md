---
layout: default
title: FRAPPE: Infusing World Modeling into Generalist Policies via Multiple Future Representation Alignment
---

# FRAPPE: Infusing World Modeling into Generalist Policies via Multiple Future Representation Alignment
**arXiv**：[2602.17259v1](https://arxiv.org/abs/2602.17259) · [PDF](https://arxiv.org/pdf/2602.17259.pdf)  
**作者**：Han Zhao, Jingbo Wang, Wenxuan Song, Shuai Chen, Yang Liu, Yan Wang, Haoang Li, Donglin Wang  

**一句话要点**：提出FRAPPE方法，通过多未来表示对齐增强通用机器人策略的世界建模能力

**关键词**：世界建模, 表示对齐, 机器人策略, 两阶段微调, 视觉基础模型, 泛化能力

## 3 点简述
- 当前方法过度强调像素级重建，限制语义学习和泛化，且推理时依赖预测观测导致误差累积
- 采用两阶段微调：中训练预测未来观测的潜在表示，后训练并行扩展计算并与多个视觉基础模型对齐表示
- 在RoboTwin基准和真实任务中表现优于现有方法，在长视野和未见场景中展示强泛化能力

## 摘要（原文）

> Enabling VLA models to predict environmental dynamics, known as world modeling, has been recognized as essential for improving robotic reasoning and generalization. However, current approaches face two main issues: 1. The training objective forces models to over-emphasize pixel-level reconstruction, which constrains semantic learning and generalization 2. Reliance on predicted future observations during inference often leads to error accumulation. To address these challenges, we introduce Future Representation Alignment via Parallel Progressive Expansion (FRAPPE). Our method adopts a two-stage fine-tuning strategy: In the mid-training phase, the model learns to predict the latent representations of future observations; In the post-training phase, we expand the computational workload in parallel and align the representation simultaneously with multiple different visual foundation models. By significantly improving fine-tuning efficiency and reducing dependence on action-annotated data, FRAPPE provides a scalable and data-efficient pathway to enhance world-awareness in generalist robotic policies. Experiments on the RoboTwin benchmark and real-world tasks demonstrate that FRAPPE outperforms state-of-the-art approaches and shows strong generalization in long-horizon and unseen scenarios.

