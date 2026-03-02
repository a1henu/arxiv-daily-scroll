---
layout: default
title: Preference Packing: Efficient Preference Optimization for Large Language Models
---

# Preference Packing: Efficient Preference Optimization for Large Language Models
**arXiv**：[2602.24082v1](https://arxiv.org/abs/2602.24082) · [PDF](https://arxiv.org/pdf/2602.24082.pdf)  
**作者**：Jaekyung Cho  

**一句话要点**：提出偏好打包方法以提升大语言模型偏好优化训练的资源效率

**关键词**：偏好优化, 资源效率, 大语言模型, 训练加速, KV缓存优化

## 3 点简述
- 核心问题：大语言模型偏好优化训练中，相同输入提示对应不同响应导致资源浪费
- 方法要点：通过减少重复输入提示的注意力操作和KV缓存内存使用，提升资源效率
- 实验或效果：在文本和图像数据集上实现至少37%训练时间减少，结合现有优化技术可加速3.22倍

## 摘要（原文）

> Resource-efficient training optimization techniques are becoming increasingly important as the size of large language models (LLMs) continues to grow. In particular, batch packing is commonly used in pre-training and supervised fine-tuning to achieve resource-efficient training. We propose preference packing, a method to enhance resource efficiency in training techniques that use data with different responses for the same input prompt, such as reward models or Direct Preference Optimization (DPO). Preference packing improves resource efficiency by reducing the attention operations for duplicate input prompts and decreasing KV cache memory usage. We conducted experiments on text-only datasets and image-included datasets and achieved at least 37% reduction in training time. Notably, this method can be applied alongside existing optimization techniques such as batch sorting, resulting in a 3.22x speedup.

