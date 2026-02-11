---
layout: default
title: Model soups need only one ingredient
---

# Model soups need only one ingredient
**arXiv**：[2602.09689v1](https://arxiv.org/abs/2602.09689) · [PDF](https://arxiv.org/pdf/2602.09689.pdf)  
**作者**：Alireza Abdollahpoorrostam, Nikolaos Dimitriadis, Adam Hazimeh, Pascal Frossard  

**一句话要点**：提出MonoSoup方法，通过单检查点分解实现ID-OOD平衡，替代多检查点集成。

**关键词**：模型集成, 鲁棒性优化, 奇异值分解, 后处理方法, 计算效率

## 3 点简述
- 问题：微调大模型提升ID准确率但损害OOD鲁棒性，多检查点集成计算成本高。
- 方法：对单检查点层更新进行SVD分解，基于熵有效秩自动重加权组件，无需数据或超参数。
- 实验：在CLIP和Qwen模型上验证，在自然分布偏移和推理任务中保持ID-OOD平衡，计算开销低。

## 摘要（原文）

> Fine-tuning large pre-trained models on a target distribution often improves in-distribution (ID) accuracy, but at the cost of out-of-distribution (OOD) robustness as representations specialize to the fine-tuning data. Weight-space ensembling methods, such as Model Soups, mitigate this effect by averaging multiple checkpoints, but they are computationally prohibitive, requiring the training and storage of dozens of fine-tuned models. In this paper, we introduce MonoSoup, a simple, data-free, hyperparameter-free, post-hoc method that achieves a strong ID-OOD balance using only a single checkpoint. Our method applies Singular Value Decomposition (SVD) to each layer's update and decomposes it into high-energy directions that capture task-specific adaptation and low-energy directions that introduce noise but may still encode residual signals useful for robustness. MonoSoup then uses entropy-based effective rank to automatically re-weigh these components with layer-wise coefficients that account for the spectral and geometric structure of the model. Experiments on CLIP models fine-tuned on ImageNet and evaluated under natural distribution shifts, as well as on Qwen language models tested on mathematical reasoning and multiple-choice benchmarks, show that this plug-and-play approach is a practical and effective alternative to multi-checkpoint methods, retaining much of their benefits without their computational overhead.

