---
layout: default
title: Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models
---

# Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models
**arXiv**：[2512.16244v1](https://arxiv.org/abs/2512.16244) · [PDF](https://arxiv.org/pdf/2512.16244.pdf)  
**作者**：Xueqi Ma, Xingjun Ma, Sarah Monazam Erfani, Danilo Mandic, James Bailey  

**一句话要点**：提出粗到细开放集图节点分类框架，利用大语言模型增强分布外检测与分类

**关键词**：开放集分类, 图神经网络, 大语言模型, 分布外检测, 粗到细框架, 语义分类

## 3 点简述
- 核心问题：开放集分类需检测分布外样本并分类，现有方法将分布外视为单一类，缺乏细粒度分析。
- 方法要点：结合大语言模型进行粗分类检测分布外并生成标签，再用图神经网络细分类提升性能，实现语义分布外分类。
- 实验或效果：在图形和文本领域提升分布外检测10%，图形数据集分布外分类准确率达70%。

## 摘要（原文）

> Developing open-set classification methods capable of classifying in-distribution (ID) data while detecting out-of-distribution (OOD) samples is essential for deploying graph neural networks (GNNs) in open-world scenarios. Existing methods typically treat all OOD samples as a single class, despite real-world applications, especially high-stake settings such as fraud detection and medical diagnosis, demanding deeper insights into OOD samples, including their probable labels. This raises a critical question: can OOD detection be extended to OOD classification without true label information? To address this question, we propose a Coarse-to-Fine open-set Classification (CFC) framework that leverages large language models (LLMs) for graph datasets. CFC consists of three key components: a coarse classifier that uses LLM prompts for OOD detection and outlier label generation, a GNN-based fine classifier trained with OOD samples identified by the coarse classifier for enhanced OOD detection and ID classification, and refined OOD classification achieved through LLM prompts and post-processed OOD labels. Unlike methods that rely on synthetic or auxiliary OOD samples, CFC employs semantic OOD instances that are genuinely out-of-distribution based on their inherent meaning, improving interpretability and practical utility. Experimental results show that CFC improves OOD detection by ten percent over state-of-the-art methods on graph and text domains and achieves up to seventy percent accuracy in OOD classification on graph datasets.

