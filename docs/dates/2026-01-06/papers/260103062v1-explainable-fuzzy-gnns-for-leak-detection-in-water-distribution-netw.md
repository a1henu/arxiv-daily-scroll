---
layout: default
title: Explainable Fuzzy GNNs for Leak Detection in Water Distribution Networks
---

# Explainable Fuzzy GNNs for Leak Detection in Water Distribution Networks
**arXiv**：[2601.03062v1](https://arxiv.org/abs/2601.03062) · [PDF](https://arxiv.org/pdf/2601.03062.pdf)  
**作者**：Qusai Khaled, Pasquale De Marinis, Moez Louati, David Ferras, Laura Genga, Uzay Kaymak  

**一句话要点**：提出可解释模糊图神经网络以解决供水管网泄漏检测中的黑盒问题

**关键词**：图神经网络, 可解释人工智能, 模糊逻辑, 泄漏检测, 供水管网, 节点分类

## 3 点简述
- 核心问题：图神经网络在供水管网泄漏检测中缺乏可解释性，阻碍实际应用。
- 方法要点：集成互信息识别关键区域，结合模糊逻辑提供基于规则的节点分类解释。
- 实验或效果：模糊图神经网络在检测和定位上性能略低于基准，但提供直观的空间局部化解释。

## 摘要（原文）

> Timely leak detection in water distribution networks is critical for conserving resources and maintaining operational efficiency. Although Graph Neural Networks (GNNs) excel at capturing spatial-temporal dependencies in sensor data, their black-box nature and the limited work on graph-based explainable models for water networks hinder practical adoption. We propose an explainable GNN framework that integrates mutual information to identify critical network regions and fuzzy logic to provide clear, rule-based explanations for node classification tasks. After benchmarking several GNN architectures, we selected the generalized graph convolution network (GENConv) for its superior performance and developed a fuzzy-enhanced variant that offers intuitive explanations for classified leak locations. Our fuzzy graph neural network (FGENConv) achieved Graph F1 scores of 0.889 for detection and 0.814 for localization, slightly below the crisp GENConv 0.938 and 0.858, respectively. Yet it compensates by providing spatially localized, fuzzy rule-based explanations. By striking the right balance between precision and explainability, the proposed fuzzy network could enable hydraulic engineers to validate predicted leak locations, conserve human resources, and optimize maintenance strategies. The code is available at github.com/pasqualedem/GNNLeakDetection.

