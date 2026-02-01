---
layout: default
title: Value-Based Pre-Training with Downstream Feedback
---

# Value-Based Pre-Training with Downstream Feedback
**arXiv**：[2601.22108v1](https://arxiv.org/abs/2601.22108) · [PDF](https://arxiv.org/pdf/2601.22108.pdf)  
**作者**：Shuqi Ke, Giulia Fanti  

**一句话要点**：提出V-Pretraining方法，利用下游反馈引导基础模型预训练以提高效率与性能

**关键词**：基础模型预训练, 下游反馈引导, 模态无关方法, 自监督学习, 计算效率优化, 任务设计器

## 3 点简述
- 核心问题：标准预训练使用固定代理目标（如下一词预测），可能浪费计算资源于无关下游能力
- 方法要点：引入基于价值的模态无关方法，通过轻量任务设计器选择预训练任务，使预训练损失梯度与下游任务梯度对齐
- 实验或效果：在语言模型上，使用少量反馈提升推理能力；在视觉自监督学习中，改进ADE20K和NYUv2结果，同时保持ImageNet准确率

## 摘要（原文）

> Can a small amount of verified goal information steer the expensive self-supervised pretraining of foundation models? Standard pretraining optimizes a fixed proxy objective (e.g., next-token prediction), which can misallocate compute away from downstream capabilities of interest. We introduce V-Pretraining: a value-based, modality-agnostic method for controlled continued pretraining in which a lightweight task designer reshapes the pretraining task to maximize the value of each gradient step. For example, consider self-supervised learning (SSL) with sample augmentation. The V-Pretraining task designer selects pretraining tasks (e.g., augmentations) for which the pretraining loss gradient is aligned with a gradient computed over a downstream task (e.g., image segmentation). This helps steer pretraining towards relevant downstream capabilities. Notably, the pretrained model is never updated on downstream task labels; they are used only to shape the pretraining task. Under matched learner update budgets, V-Pretraining of 0.5B--7B language models improves reasoning (GSM8K test Pass@1) by up to 18% relative over standard next-token prediction using only 12% of GSM8K training examples as feedback. In vision SSL, we improve the state-of-the-art results on ADE20K by up to 1.07 mIoU and reduce NYUv2 RMSE while improving ImageNet linear accuracy, and we provide pilot evidence of improved token efficiency in continued pretraining.

