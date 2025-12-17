---
layout: default
title: Enhancing Interpretability for Vision Models via Shapley Value Optimization
---

# Enhancing Interpretability for Vision Models via Shapley Value Optimization
**arXiv**：[2512.14354v1](https://arxiv.org/abs/2512.14354) · [PDF](https://arxiv.org/pdf/2512.14354.pdf)  
**作者**：Kanglong Fan, Yunqiao Yang, Chen Ma  

**一句话要点**：提出基于Shapley值优化的自解释框架，以增强视觉模型的可解释性并保持性能。

**关键词**：可解释性增强, Shapley值优化, 自解释神经网络, 视觉模型, 辅助任务训练

## 3 点简述
- 核心问题：深度神经网络决策过程不透明，现有解释方法存在忠实度低或性能牺牲问题。
- 方法要点：在训练中集成Shapley值估计作为辅助任务，公平分配预测分数至图像块，确保解释与决策逻辑对齐。
- 实验或效果：在多个基准测试中实现最先进的可解释性，同时保持模型性能和兼容性。

## 摘要（原文）

> Deep neural networks have demonstrated remarkable performance across various domains, yet their decision-making processes remain opaque. Although many explanation methods are dedicated to bringing the obscurity of DNNs to light, they exhibit significant limitations: post-hoc explanation methods often struggle to faithfully reflect model behaviors, while self-explaining neural networks sacrifice performance and compatibility due to their specialized architectural designs. To address these challenges, we propose a novel self-explaining framework that integrates Shapley value estimation as an auxiliary task during training, which achieves two key advancements: 1) a fair allocation of the model prediction scores to image patches, ensuring explanations inherently align with the model's decision logic, and 2) enhanced interpretability with minor structural modifications, preserving model performance and compatibility. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art interpretability.

