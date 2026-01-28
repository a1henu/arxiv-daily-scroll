---
layout: default
title: Self-Supervised Weight Templates for Scalable Vision Model Initialization
---

# Self-Supervised Weight Templates for Scalable Vision Model Initialization
**arXiv**：[2601.19694v1](https://arxiv.org/abs/2601.19694) · [PDF](https://arxiv.org/pdf/2601.19694.pdf)  
**作者**：Yucheng Xie, Fu Feng, Ruixiao Shi, Jing Wang, Yong Rui, Xin Geng  

**一句话要点**：提出SWEET框架，通过自监督权重模板实现视觉模型的可扩展初始化。

**关键词**：自监督学习, 模型初始化, 权重模板, 可扩展架构, 视觉任务, Tucker分解

## 3 点简述
- 核心问题：传统预训练和微调难以适应不同规模架构的部署需求。
- 方法要点：基于Tucker分解学习共享权重模板和尺寸特定权重缩放器，支持灵活组合。
- 实验或效果：在分类、检测、分割和生成任务中展示先进性能，提升跨宽度泛化能力。

## 摘要（原文）

> The increasing scale and complexity of modern model parameters underscore the importance of pre-trained models. However, deployment often demands architectures of varying sizes, exposing limitations of conventional pre-training and fine-tuning. To address this, we propose SWEET, a self-supervised framework that performs constraint-based pre-training to enable scalable initialization in vision tasks. Instead of pre-training a fixed-size model, we learn a shared weight template and size-specific weight scalers under Tucker-based factorization, which promotes modularity and supports flexible adaptation to architectures with varying depths and widths. Target models are subsequently initialized by composing and reweighting the template through lightweight weight scalers, whose parameters can be efficiently learned from minimal training data. To further enhance flexibility in width expansion, we introduce width-wise stochastic scaling, which regularizes the template along width-related dimensions and encourages robust, width-invariant representations for improved cross-width generalization. Extensive experiments on \textsc{classification}, \textsc{detection}, \textsc{segmentation} and \textsc{generation} tasks demonstrate the state-of-the-art performance of SWEET for initializing variable-sized vision models.

