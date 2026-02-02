---
layout: default
title: CARE: Multi-Task Pretraining for Latent Continuous Action Representation in Robot Control
---

# CARE: Multi-Task Pretraining for Latent Continuous Action Representation in Robot Control
**arXiv**：[2601.22467v1](https://arxiv.org/abs/2601.22467) · [PDF](https://arxiv.org/pdf/2601.22467.pdf)  
**作者**：Jiaqi Shi, Xulong Zhang, Xiaoyang Qu, Jianzong Wang  

**一句话要点**：提出CARE框架，通过多任务预训练学习连续潜在动作表示，以弱监督解决机器人控制中的动作标注依赖问题。

**关键词**：机器人控制, 视觉-语言-动作模型, 弱监督学习, 多任务预训练, 连续潜在表示

## 3 点简述
- 核心问题：现有视觉-语言-动作模型依赖动作标注，限制了机器人控制的扩展性和泛化能力。
- 方法要点：利用视频-文本对进行多任务预训练，学习连续潜在动作表示，无需显式动作标签。
- 实验或效果：在模拟任务中展示更高的成功率、语义可解释性，并避免捷径学习，验证了弱监督下的有效性。

## 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models have shown promise for robot control, but their dependence on action supervision limits scalability and generalization. To address this challenge, we introduce CARE, a novel framework designed to train VLA models for robotic task execution. Unlike existing methods that depend on action annotations during pretraining, CARE eliminates the need for explicit action labels by leveraging only video-text pairs. These weakly aligned data sources enable the model to learn continuous latent action representations through a newly designed multi-task pretraining objective. During fine-tuning, a small set of labeled data is used to train the action head for control. Experimental results across various simulation tasks demonstrate CARE's superior success rate, semantic interpretability, and ability to avoid shortcut learning. These results underscore CARE's scalability, interpretability, and effectiveness in robotic control with weak supervision.

