---
layout: default
title: Test-time Adaptive Hierarchical Co-enhanced Denoising Network for Reliable Multimodal Classification
---

# Test-time Adaptive Hierarchical Co-enhanced Denoising Network for Reliable Multimodal Classification
**arXiv**：[2601.07163v1](https://arxiv.org/abs/2601.07163) · [PDF](https://arxiv.org/pdf/2601.07163.pdf)  
**作者**：Shu Shen, C. L. Philip Chen, Tong Zhang  

**一句话要点**：提出测试时自适应分层协同增强去噪网络，以解决低质量多模态数据中的可靠分类问题。

**关键词**：多模态分类, 噪声去除, 自适应学习, 测试时增强, 可靠学习, 异构数据

## 3 点简述
- 核心问题：多模态噪声导致现有方法难以可靠去除异构噪声，且对新噪声适应性和泛化能力有限。
- 方法要点：通过自适应稳定子空间对齐和样本自适应置信对齐，在全局和实例层面联合去除模态特定和跨模态噪声。
- 实验或效果：在多个基准测试中，相比先进方法，实现了更优的分类性能、鲁棒性和泛化能力。

## 摘要（原文）

> Reliable learning on low-quality multimodal data is a widely concerning issue, especially in safety-critical applications. However, multimodal noise poses a major challenge in this domain and leads existing methods to suffer from two key limitations. First, they struggle to reliably remove heterogeneous data noise, hindering robust multimodal representation learning. Second, they exhibit limited adaptability and generalization when encountering previously unseen noise. To address these issues, we propose Test-time Adaptive Hierarchical Co-enhanced Denoising Network (TAHCD). On one hand, TAHCD introduces the Adaptive Stable Subspace Alignment and Sample-Adaptive Confidence Alignment to reliably remove heterogeneous noise. They account for noise at both global and instance levels and enable jointly removal of modality-specific and cross-modality noise, achieving robust learning. On the other hand, TAHCD introduces test-time cooperative enhancement, which adaptively updates the model in response to input noise in a label-free manner, improving adaptability and generalization. This is achieved by collaboratively enhancing the joint removal process of modality-specific and cross-modality noise across global and instance levels according to sample noise. Experiments on multiple benchmarks demonstrate that the proposed method achieves superior classification performance, robustness, and generalization compared with state-of-the-art reliable multimodal learning approaches.

