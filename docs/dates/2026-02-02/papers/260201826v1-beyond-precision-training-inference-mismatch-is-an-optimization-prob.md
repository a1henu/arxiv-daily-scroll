---
layout: default
title: Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It
---

# Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It
**arXiv**：[2602.01826v1](https://arxiv.org/abs/2602.01826) · [PDF](https://arxiv.org/pdf/2602.01826.pdf)  
**作者**：Yaxiang Zhang, Yingru Li, Jiacai Liu, Jiawei Xu, Ziniu Li, Qian Liu, Haoyuan Li  

**一句话要点**：提出基于响应长度的动态学习率调度器，以稳定大语言模型强化学习训练中的训练-推理不匹配问题。

**关键词**：强化学习, 大语言模型, 训练-推理不匹配, 学习率调度, 梯度噪声, 优化稳定性

## 3 点简述
- 核心问题：大语言模型强化学习训练不稳定，源于训练-推理不匹配与梯度噪声的动态耦合。
- 方法要点：通过响应长度作为预警信号，动态触发学习率衰减，以抑制不匹配和噪声。
- 实验或效果：经验证据表明，该方法能稳定训练，将训练-推理不匹配保持在安全水平。

## 摘要（原文）

> Reinforcement Learning (RL) for training Large Language Models is notoriously unstable. While recent studies attribute this to "training inference mismatch stemming" from inconsistent hybrid engines, standard remedies, such as Importance Sampling, might fail during extended training runs. In this work, we analyze this instability through the lens of optimization, demonstrating that gradient noise and training-inference mismatch escalate in tandem as training progresses. Meanwhile, we find that the mismatch can be effectively suppressed by shrinking the update size. Taken together, we deduce that the mismatch is not merely a static numerical discrepancy, but a dynamic failure coupled with the model's optimization. Based on this insight, we propose a simple yet effective solution: a specialized Learning Rate (LR) scheduler. Instead of pre-defined decay schedule in traditional LR scheduler, our method dynamically triggers LR decay based on response length, which we identify as a reliable early-warning signal for impending instability. Empirical evidence suggests that by reducing the learning rate as gradient noise rises, we can consistently stabilize RL training and keep the training-inference mismatch at a safe level.

