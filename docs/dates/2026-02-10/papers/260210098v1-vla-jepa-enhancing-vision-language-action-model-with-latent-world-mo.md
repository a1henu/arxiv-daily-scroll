---
layout: default
title: VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model
---

# VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model
**arXiv**：[2602.10098v1](https://arxiv.org/abs/2602.10098) · [PDF](https://arxiv.org/pdf/2602.10098.pdf)  
**作者**：Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu, Hanxin Zhu, Guangzhong Sun, Xin Jin, Zhibo Chen  

**一句话要点**：提出VLA-JEPA框架，通过泄漏无关状态预测增强视觉-语言-动作模型的泛化与鲁棒性。

**关键词**：视觉-语言-动作模型, 潜在世界模型, JEPA预训练, 状态预测, 泛化能力, 鲁棒性

## 3 点简述
- 核心问题：现有VLA模型预训练易受像素变化、外观偏差和动作无关运动干扰，导致泛化能力差。
- 方法要点：采用JEPA风格预训练，在潜在空间预测未来状态，避免信息泄漏，学习稳健的动态抽象。
- 实验或效果：在LIBERO等数据集和真实世界任务中，VLA-JEPA相比现有方法在泛化和鲁棒性上取得一致提升。

## 摘要（原文）

> Pretraining Vision-Language-Action (VLA) policies on internet-scale video is appealing, yet current latent-action objectives often learn the wrong thing: they remain anchored to pixel variation rather than action-relevant state transitions, making them vulnerable to appearance bias, nuisance motion, and information leakage. We introduce VLA-JEPA, a JEPA-style pretraining framework that sidesteps these pitfalls by design. The key idea is \emph{leakage-free state prediction}: a target encoder produces latent representations from future frames, while the student pathway sees only the current observation -- future information is used solely as supervision targets, never as input. By predicting in latent space rather than pixel space, VLA-JEPA learns dynamics abstractions that are robust to camera motion and irrelevant background changes. This yields a simple two-stage recipe -- JEPA pretraining followed by action-head fine-tuning -- without the multi-stage complexity of prior latent-action pipelines. Experiments on LIBERO, LIBERO-Plus, SimplerEnv and real-world manipulation tasks show that VLA-JEPA achieves consistent gains in generalization and robustness over existing methods.

