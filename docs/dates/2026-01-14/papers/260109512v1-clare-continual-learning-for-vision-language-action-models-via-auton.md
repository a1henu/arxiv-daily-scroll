---
layout: default
title: CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion
---

# CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion
**arXiv**：[2601.09512v1](https://arxiv.org/abs/2601.09512) · [PDF](https://arxiv.org/pdf/2601.09512.pdf)  
**作者**：Ralf Römer, Yi Zhang, Angela P. Schoellig  

**一句话要点**：提出CLARE框架，通过自主适配器路由与扩展实现视觉-语言-动作模型的持续学习

**关键词**：持续学习, 视觉-语言-动作模型, 适配器路由, 参数高效, 机器人操作, 灾难性遗忘

## 3 点简述
- 核心问题：现有机器人持续学习方法依赖存储旧数据、难以处理长任务序列或需要任务标识符部署
- 方法要点：引入轻量模块化适配器，基于层间特征相似性自主扩展模型，部署时通过自编码器路由动态激活适配器
- 实验或效果：在LIBERO基准测试中，CLARE在新任务上表现优异且无灾难性遗忘，显著优于基于示例的方法

## 摘要（原文）

> To teach robots complex manipulation tasks, it is now a common practice to fine-tune a pre-trained vision-language-action model (VLA) on task-specific data. However, since this recipe updates existing representations, it is unsuitable for long-term operation in the real world, where robots must continually adapt to new tasks and environments while retaining the knowledge they have already acquired. Existing continual learning methods for robotics commonly require storing previous data (exemplars), struggle with long task sequences, or rely on task identifiers for deployment. To address these limitations, we propose CLARE, a general, parameter-efficient framework for exemplar-free continual learning with VLAs. CLARE introduces lightweight modular adapters into selected feedforward layers and autonomously expands the model only where necessary when learning a new task, guided by layer-wise feature similarity. During deployment, an autoencoder-based routing mechanism dynamically activates the most relevant adapters without requiring task labels. Through extensive experiments on the LIBERO benchmark, we show that CLARE achieves high performance on new tasks without catastrophic forgetting of earlier tasks, significantly outperforming even exemplar-based methods. Code and data are available at https://tum-lsy.github.io/clare.

