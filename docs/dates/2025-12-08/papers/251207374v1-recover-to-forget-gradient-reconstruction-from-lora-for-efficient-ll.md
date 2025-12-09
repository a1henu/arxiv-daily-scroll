---
layout: default
title: Recover-to-Forget: Gradient Reconstruction from LoRA for Efficient LLM Unlearning
---

# Recover-to-Forget: Gradient Reconstruction from LoRA for Efficient LLM Unlearning
**arXiv**：[2512.07374v1](https://arxiv.org/abs/2512.07374) · [PDF](https://arxiv.org/pdf/2512.07374.pdf)  
**作者**：Yezi Liu, Hanning Chen, Wenjun Huang, Yang Ni, Mohsen Imani  

**一句话要点**：提出R2F框架，通过从LoRA重建梯度实现高效LLM遗忘学习

**关键词**：大语言模型, 遗忘学习, LoRA, 梯度重建, 模型迁移

## 3 点简述
- 核心问题：现有遗忘学习方法需全模型微调或原始数据，限制可扩展性
- 方法要点：基于LoRA参数梯度，训练解码器近似全模型梯度方向
- 实验或效果：在代理模型上训练解码器，可迁移至目标模型，保持性能

## 摘要（原文）

> Unlearning in large foundation models (e.g., LLMs) is essential for enabling dynamic knowledge updates, enforcing data deletion rights, and correcting model behavior. However, existing unlearning methods often require full-model fine-tuning or access to the original training data, which limits their scalability and practicality. In this work, we introduce Recover-to-Forget (R2F), a novel framework for efficient unlearning in LLMs based on reconstructing full-model gradient directions from low-rank LoRA adapter updates. Rather than performing backpropagation through the full model, we compute gradients with respect to LoRA parameters using multiple paraphrased prompts and train a gradient decoder to approximate the corresponding full-model gradients. To ensure applicability to larger or black-box models, the decoder is trained on a proxy model and transferred to target models. We provide a theoretical analysis of cross-model generalization and demonstrate that our method achieves effective unlearning while preserving general model performance. Experimental results demonstrate that R2F offers a scalable and lightweight alternative for unlearning in pretrained LLMs without requiring full retraining or access to internal parameters.

