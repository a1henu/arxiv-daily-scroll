---
layout: default
title: Interpretable and Steerable Concept Bottleneck Sparse Autoencoders
---

# Interpretable and Steerable Concept Bottleneck Sparse Autoencoders
**arXiv**：[2512.10805v1](https://arxiv.org/abs/2512.10805) · [PDF](https://arxiv.org/pdf/2512.10805.pdf)  
**作者**：Akshay Kulkarni, Tsui-Wei Weng, Vivek Narayanaswamy, Shusen Liu, Wesam A. Sakla, Kowshik Thopalli  

**一句话要点**：提出概念瓶颈稀疏自编码器以提升大视觉模型的解释性与可操控性

**关键词**：稀疏自编码器, 解释性度量, 可操控性度量, 概念瓶颈, 后处理框架, 视觉语言模型

## 3 点简述
- 稀疏自编码器在解释性与可操控性方面存在多数神经元效用低的问题
- 引入新指标分析并设计后处理框架，通过剪枝和概念瓶颈增强
- 实验显示在视觉语言模型和图像生成任务中解释性提升32.1%，可操控性提升14.5%

## 摘要（原文）

> Sparse autoencoders (SAEs) promise a unified approach for mechanistic interpretability, concept discovery, and model steering in LLMs and LVLMs. However, realizing this potential requires that the learned features be both interpretable and steerable. To that end, we introduce two new computationally inexpensive interpretability and steerability metrics and conduct a systematic analysis on LVLMs. Our analysis uncovers two observations; (i) a majority of SAE neurons exhibit either low interpretability or low steerability or both, rendering them ineffective for downstream use; and (ii) due to the unsupervised nature of SAEs, user-desired concepts are often absent in the learned dictionary, thus limiting their practical utility. To address these limitations, we propose Concept Bottleneck Sparse Autoencoders (CB-SAE) - a novel post-hoc framework that prunes low-utility neurons and augments the latent space with a lightweight concept bottleneck aligned to a user-defined concept set. The resulting CB-SAE improves interpretability by +32.1% and steerability by +14.5% across LVLMs and image generation tasks. We will make our code and model weights available.

