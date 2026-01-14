---
layout: default
title: Zero-Shot Distracted Driver Detection via Vision Language Models with Double Decoupling
---

# Zero-Shot Distracted Driver Detection via Vision Language Models with Double Decoupling
**arXiv**：[2601.08467v1](https://arxiv.org/abs/2601.08467) · [PDF](https://arxiv.org/pdf/2601.08467.pdf)  
**作者**：Takamichi Miyata, Sumiko Miyata, Andrew Morris  

**一句话要点**：提出双解耦框架以提升零样本分心驾驶检测的鲁棒性

**关键词**：零样本学习, 视觉语言模型, 分心驾驶检测, 主体解耦, 文本嵌入正交化, 道路安全

## 3 点简述
- 核心问题：现有视觉语言模型在分心驾驶检测中因驾驶员外观变化（如服装、年龄）与行为线索纠缠而性能受限
- 方法要点：通过主体解耦提取外观嵌入并移除其影响，同时正交化文本嵌入以增强可分性
- 实验或效果：实验显示方法在零样本分类中优于基线，适用于实际道路安全应用

## 摘要（原文）

> Distracted driving is a major cause of traffic collisions, calling for robust and scalable detection methods. Vision-language models (VLMs) enable strong zero-shot image classification, but existing VLM-based distracted driver detectors often underperform in real-world conditions. We identify subject-specific appearance variations (e.g., clothing, age, and gender) as a key bottleneck: VLMs entangle these factors with behavior cues, leading to decisions driven by who the driver is rather than what the driver is doing. To address this, we propose a subject decoupling framework that extracts a driver appearance embedding and removes its influence from the image embedding prior to zero-shot classification, thereby emphasizing distraction-relevant evidence. We further orthogonalize text embeddings via metric projection onto Stiefel manifold to improve separability while staying close to the original semantics. Experiments demonstrate consistent gains over prior baselines, indicating the promise of our approach for practical road-safety applications.

