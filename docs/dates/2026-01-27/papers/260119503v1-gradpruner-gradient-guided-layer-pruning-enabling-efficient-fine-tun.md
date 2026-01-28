---
layout: default
title: GradPruner: Gradient-Guided Layer Pruning Enabling Efficient Fine-Tuning and Inference for LLMs
---

# GradPruner: Gradient-Guided Layer Pruning Enabling Efficient Fine-Tuning and Inference for LLMs
**arXiv**：[2601.19503v1](https://arxiv.org/abs/2601.19503) · [PDF](https://arxiv.org/pdf/2601.19503.pdf)  
**作者**：Wei Huang, Anda Cheng, Yinggui Wang  

**一句话要点**：提出GradPruner以解决大语言模型下游微调中训练与推理效率低的问题

**关键词**：大语言模型, 结构化剪枝, 梯度引导, 高效微调, 推理优化

## 3 点简述
- 核心问题：大语言模型下游微调耗时昂贵，结构化剪枝方法常需额外训练和内存，难以实现高效微调。
- 方法要点：基于微调初期梯度累积计算IGIA-Matrix评估层重要性，剪枝后稀疏化并合并剩余层以减少干扰。
- 实验或效果：在八个下游数据集上实验，参数减少40%时精度仅下降0.99%，提升训练与推理效率。

## 摘要（原文）

> Fine-tuning Large Language Models (LLMs) with downstream data is often considered time-consuming and expensive. Structured pruning methods are primarily employed to improve the inference efficiency of pre-trained models. Meanwhile, they often require additional time and memory for training, knowledge distillation, structure search, and other strategies, making efficient model fine-tuning challenging to achieve. To simultaneously enhance the training and inference efficiency of downstream task fine-tuning, we introduce GradPruner, which can prune layers of LLMs guided by gradients in the early stages of fine-tuning. GradPruner uses the cumulative gradients of each parameter during the initial phase of fine-tuning to compute the Initial Gradient Information Accumulation Matrix (IGIA-Matrix) to assess the importance of layers and perform pruning. We sparsify the pruned layers based on the IGIA-Matrix and merge them with the remaining layers. Only elements with the same sign are merged to reduce interference from sign variations. We conducted extensive experiments on two LLMs across eight downstream datasets. Including medical, financial, and general benchmark tasks. The results demonstrate that GradPruner has achieved a parameter reduction of 40% with only a 0.99% decrease in accuracy. Our code is publicly available.

