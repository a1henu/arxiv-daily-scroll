---
layout: default
title: From Observation to Action: Latent Action-based Primitive Segmentation for VLA Pre-training in Industrial Settings
---

# From Observation to Action: Latent Action-based Primitive Segmentation for VLA Pre-training in Industrial Settings
**arXiv**：[2511.21428v1](https://arxiv.org/abs/2511.21428) · [PDF](https://arxiv.org/pdf/2511.21428.pdf)  
**作者**：Jiajie Zhang, Sören Schwertfeger, Alexander Kleiner  

**一句话要点**：提出基于潜在动作的无监督框架，从工业视频中提取VLA预训练数据。

**关键词**：无监督学习, 动作分割, VLA预训练, 工业视频分析, 潜在动作能量

## 3 点简述
- 核心问题：如何从无标签工业视频流中自动提取结构化数据用于VLA预训练。
- 方法要点：使用运动分词器和潜在动作能量指标进行无监督动作分割。
- 实验或效果：在公开和专有数据集上验证动作分割的有效性和语义一致性。

## 摘要（原文）

> We present a novel unsupervised framework to unlock vast unlabeled human demonstration data from continuous industrial video streams for Vision-Language-Action (VLA) model pre-training. Our method first trains a lightweight motion tokenizer to encode motion dynamics, then employs an unsupervised action segmenter leveraging a novel "Latent Action Energy" metric to discover and segment semantically coherent action primitives. The pipeline outputs both segmented video clips and their corresponding latent action sequences, providing structured data directly suitable for VLA pre-training. Evaluations on public benchmarks and a proprietary electric motor assembly dataset demonstrate effective segmentation of key tasks performed by humans at workstations. Further clustering and quantitative assessment via a Vision-Language Model confirm the semantic coherence of the discovered action primitives. To our knowledge, this is the first fully automated end-to-end system for extracting and organizing VLA pre-training data from unstructured industrial videos, offering a scalable solution for embodied AI integration in manufacturing.

