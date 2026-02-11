---
layout: default
title: Continual Learning for non-stationary regression via Memory-Efficient Replay
---

# Continual Learning for non-stationary regression via Memory-Efficient Replay
**arXiv**：[2602.09720v1](https://arxiv.org/abs/2602.09720) · [PDF](https://arxiv.org/pdf/2602.09720.pdf)  
**作者**：Pablo García-Santaclara, Bruno Fernández-Castro, RebecaP. Díaz-Redondo, Martín Alonso-Gamarra  

**一句话要点**：提出基于原型的生成重放框架，用于在线无任务持续回归，以应对非静态数据流。

**关键词**：持续学习, 回归任务, 生成重放, 原型学习, 在线学习, 非静态数据流

## 3 点简述
- 核心问题：持续学习研究多集中于分类，回归任务缺乏有效方法，尤其在动态环境中数据流非静态。
- 方法要点：采用自适应输出空间离散化模型，实现基于原型的生成重放，无需存储原始数据，支持在线无任务学习。
- 实验或效果：在多个基准数据集上验证，框架减少遗忘，提供比现有方法更稳定的性能。

## 摘要（原文）

> Data streams are rarely static in dynamic environments like Industry 4.0. Instead, they constantly change, making traditional offline models outdated unless they can quickly adjust to the new data. This need can be adequately addressed by continual learning (CL), which allows systems to gradually acquire knowledge without incurring the prohibitive costs of retraining them from scratch. Most research on continual learning focuses on classification problems, while very few studies address regression tasks. We propose the first prototype-based generative replay framework designed for online task-free continual regression. Our approach defines an adaptive output-space discretization model, enabling prototype-based generative replay for continual regression without storing raw data. Evidence obtained from several benchmark datasets shows that our framework reduces forgetting and provides more stable performance than other state-of-the-art solutions.

