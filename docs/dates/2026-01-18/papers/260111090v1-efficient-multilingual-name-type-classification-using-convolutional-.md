---
layout: default
title: Efficient Multilingual Name Type Classification Using Convolutional Networks
---

# Efficient Multilingual Name Type Classification Using Convolutional Networks
**arXiv**：[2601.11090v1](https://arxiv.org/abs/2601.11090) · [PDF](https://arxiv.org/pdf/2601.11090.pdf)  
**作者**：Davor Lauc  

**一句话要点**：提出Onomas-CNN X卷积网络，用于高效多语言专名分类，在CPU上实现高精度与低能耗。

**关键词**：多语言专名分类, 卷积神经网络, CPU高效处理, 深度可分离卷积, 分层分类, 低能耗模型

## 3 点简述
- 核心问题：多语言专名分类，涉及104种语言和四种实体类型（人、组织、地点、其他）。
- 方法要点：结合并行卷积分支、深度可分离操作和分层分类，优化CPU处理效率。
- 实验或效果：准确率达92.1%，单核CPU每秒处理2,813个专名，比微调XLM-RoBERTa快46倍，能耗降低46倍。

## 摘要（原文）

> We present a convolutional neural network approach for classifying proper names by language and entity type. Our model, Onomas-CNN X, combines parallel convolution branches with depthwise-separable operations and hierarchical classification to process names efficiently on CPU hardware. We evaluate the architecture on a large multilingual dataset covering 104 languages and four entity types (person, organization, location, other). Onomas-CNN X achieves 92.1% accuracy while processing 2,813 names per second on a single CPU core - 46 times faster than fine-tuned XLM-RoBERTa with comparable accuracy. The model reduces energy consumption by a factor of 46 compared to transformer baselines. Our experiments demonstrate that specialized CNN architectures remain competitive with large pre-trained models for focused NLP tasks when sufficient training data exists.

