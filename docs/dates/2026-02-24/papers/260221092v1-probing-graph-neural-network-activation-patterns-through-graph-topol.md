---
layout: default
title: Probing Graph Neural Network Activation Patterns Through Graph Topology
---

# Probing Graph Neural Network Activation Patterns Through Graph Topology
**arXiv**：[2602.21092v1](https://arxiv.org/abs/2602.21092) · [PDF](https://arxiv.org/pdf/2602.21092.pdf)  
**作者**：Floriano Tori, Lorenzo Bini, Marco Sorbi, Stéphane Marchand-Maillet, Vincent Ginis  

**一句话要点**：通过图拓扑探测图神经网络激活模式，揭示曲率作为诊断工具以理解图学习失败原因

**关键词**：图神经网络, 图拓扑, 曲率分析, 大规模激活, 图变换器, 诊断工具

## 3 点简述
- 核心问题：图拓扑与图神经网络学习偏好之间的相互作用机制尚不明确
- 方法要点：利用大规模激活（极端边激活值）作为探针，分析图变换器中的激活模式
- 实验或效果：在合成图和分子基准测试中，发现大规模激活不集中于曲率极端区域，但在长距离图基准中观察到系统性曲率偏移

## 摘要（原文）

> Curvature notions on graphs provide a theoretical description of graph topology, highlighting bottlenecks and denser connected regions. Artifacts of the message passing paradigm in Graph Neural Networks, such as oversmoothing and oversquashing, have been attributed to these regions. However, it remains unclear how the topology of a graph interacts with the learned preferences of GNNs. Through Massive Activations, which correspond to extreme edge activation values in Graph Transformers, we probe this correspondence. Our findings on synthetic graphs and molecular benchmarks reveal that MAs do not preferentially concentrate on curvature extremes, despite their theoretical link to information flow. On the Long Range Graph Benchmark, we identify a systemic \textit{curvature shift}: global attention mechanisms exacerbate topological bottlenecks, drastically increasing the prevalence of negative curvature. Our work reframes curvature as a diagnostic probe for understanding when and why graph learning fails.

