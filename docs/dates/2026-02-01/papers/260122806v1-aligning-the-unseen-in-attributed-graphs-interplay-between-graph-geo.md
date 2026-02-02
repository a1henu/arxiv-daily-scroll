---
layout: default
title: Aligning the Unseen in Attributed Graphs: Interplay between Graph Geometry and Node Attributes Manifold
---

# Aligning the Unseen in Attributed Graphs: Interplay between Graph Geometry and Node Attributes Manifold
**arXiv**：[2601.22806v1](https://arxiv.org/abs/2601.22806) · [PDF](https://arxiv.org/pdf/2601.22806.pdf)  
**作者**：Aldric Labarthe, Roland Bouffanais, Julien Randon-Furling  

**一句话要点**：提出变分自编码器以解决属性图表示学习中几何冲突问题

**关键词**：属性图表示学习, 变分自编码器, 几何冲突, 度量扭曲, 结构对齐, 异常检测

## 3 点简述
- 核心问题：标准方法合并不兼容度量空间，破坏图生成过程信息
- 方法要点：分离流形学习与结构对齐，量化度量扭曲以映射属性流形
- 实验或效果：揭示传统方法无法检测的连接模式和异常，验证理论不足

## 摘要（原文）

> The standard approach to representation learning on attributed graphs -- i.e., simultaneously reconstructing node attributes and graph structure -- is geometrically flawed, as it merges two potentially incompatible metric spaces. This forces a destructive alignment that erodes information about the graph's underlying generative process. To recover this lost signal, we introduce a custom variational autoencoder that separates manifold learning from structural alignment. By quantifying the metric distortion needed to map the attribute manifold onto the graph's Heat Kernel, we transform geometric conflict into an interpretable structural descriptor. Experiments show our method uncovers connectivity patterns and anomalies undetectable by conventional approaches, proving both their theoretical inadequacy and practical limitations.

