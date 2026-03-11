---
layout: default
title: GNNs for Time Series Anomaly Detection: An Open-Source Framework and a Critical Evaluation
---

# GNNs for Time Series Anomaly Detection: An Open-Source Framework and a Critical Evaluation
**arXiv**：[2603.09675v1](https://arxiv.org/abs/2603.09675) · [PDF](https://arxiv.org/pdf/2603.09675.pdf)  
**作者**：Federico Bello, Gonzalo Chiarlone, Marcelo Fiori, Gastón García González, Federico Larroca  

**一句话要点**：提出开源框架以评估图神经网络在时间序列异常检测中的应用与性能

**关键词**：时间序列异常检测, 图神经网络, 开源框架, 评估策略, 可解释性, 注意力机制

## 3 点简述
- 核心问题：时间序列异常检测领域缺乏标准化评估框架，存在指标设计与解释问题。
- 方法要点：开发灵活可扩展的开源框架，支持图神经网络作为骨干模型进行可重复实验。
- 实验或效果：在真实数据集上评估，图神经网络提升检测性能和可解释性，注意力模型对不确定图结构稳健。

## 摘要（原文）

> There is growing interest in applying graph-based methods to Time Series Anomaly Detection (TSAD), particularly Graph Neural Networks (GNNs), as they naturally model dependencies among multivariate signals. GNNs are typically used as backbones in score-based TSAD pipelines, where anomalies are identified through reconstruction or prediction errors followed by thresholding. However, and despite promising results, the field still lacks standardized frameworks for evaluation and suffers from persistent issues with metric design and interpretation. We thus present an open-source framework for TSAD using GNNs, designed to support reproducible experimentation across datasets, graph structures, and evaluation strategies. Built with flexibility and extensibility in mind, the framework facilitates systematic comparisons between TSAD models and enables in-depth analysis of performance and interpretability. Using this tool, we evaluate several GNN-based architectures alongside baseline models across two real-world datasets with contrasting structural characteristics. Our results show that GNNs not only improve detection performance but also offer significant gains in interpretability, an especially valuable feature for practical diagnosis. We also find that attention-based GNNs offer robustness when graph structure is uncertain or inferred. In addition, we reflect on common evaluation practices in TSAD, showing how certain metrics and thresholding strategies can obscure meaningful comparisons. Overall, this work contributes both practical tools and critical insights to advance the development and evaluation of graph-based TSAD systems.

