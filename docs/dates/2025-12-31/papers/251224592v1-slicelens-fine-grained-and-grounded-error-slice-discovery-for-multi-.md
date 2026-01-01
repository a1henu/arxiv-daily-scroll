---
layout: default
title: SliceLens: Fine-Grained and Grounded Error Slice Discovery for Multi-Instance Vision Tasks
---

# SliceLens: Fine-Grained and Grounded Error Slice Discovery for Multi-Instance Vision Tasks
**arXiv**：[2512.24592v1](https://arxiv.org/abs/2512.24592) · [PDF](https://arxiv.org/pdf/2512.24592.pdf)  
**作者**：Wei Zhang, Chaoqun Wang, Zixuan Guan, Sam Kao, Pengfei Zhao, Peng Wu, Sifeng He  

**一句话要点**：提出SliceLens框架以解决多实例视觉任务中细粒度错误切片发现的问题

**关键词**：错误切片发现, 多实例视觉任务, 细粒度推理, 视觉语言模型, 基准评估

## 3 点简述
- 核心问题：现有切片发现方法主要针对图像分类，难以处理检测、分割等多实例任务中的系统失败。
- 方法要点：利用LLMs和VLMs通过基于视觉推理生成和验证失败假设，实现细粒度可解释错误切片识别。
- 实验或效果：在FeSD基准上Precision@10提升0.42，并通过模型修复实验验证可操作改进。

## 摘要（原文）

> Systematic failures of computer vision models on subsets with coherent visual patterns, known as error slices, pose a critical challenge for robust model evaluation. Existing slice discovery methods are primarily developed for image classification, limiting their applicability to multi-instance tasks such as detection, segmentation, and pose estimation. In real-world scenarios, error slices often arise from corner cases involving complex visual relationships, where existing instance-level approaches lacking fine-grained reasoning struggle to yield meaningful insights. Moreover, current benchmarks are typically tailored to specific algorithms or biased toward image classification, with artificial ground truth that fails to reflect real model failures. To address these limitations, we propose SliceLens, a hypothesis-driven framework that leverages LLMs and VLMs to generate and verify diverse failure hypotheses through grounded visual reasoning, enabling reliable identification of fine-grained and interpretable error slices. We further introduce FeSD (Fine-grained Slice Discovery), the first benchmark specifically designed for evaluating fine-grained error slice discovery across instance-level vision tasks, featuring expert-annotated and carefully refined ground-truth slices with precise grounding to local error regions. Extensive experiments on both existing benchmarks and FeSD demonstrate that SliceLens achieves state-of-the-art performance, improving Precision@10 by 0.42 (0.73 vs. 0.31) on FeSD, and identifies interpretable slices that facilitate actionable model improvements, as validated through model repair experiments.

