---
layout: default
title: The Confusion is Real: GRAPHIC - A Network Science Approach to Confusion Matrices in Deep Learning
---

# The Confusion is Real: GRAPHIC - A Network Science Approach to Confusion Matrices in Deep Learning
**arXiv**：[2602.19770v1](https://arxiv.org/abs/2602.19770) · [PDF](https://arxiv.org/pdf/2602.19770.pdf)  
**作者**：Johanna S. Fröhlich, Bastian Heinlein, Jan U. Claar, Hans Rosenberger, Vasileios Belagiannis, Ralf R. Müller  

**一句话要点**：提出GRAPHIC方法，通过图论分析混淆矩阵以可视化深度学习中的类别混淆动态。

**关键词**：可解释人工智能, 混淆矩阵分析, 网络科学, 深度学习可视化, 类别混淆

## 3 点简述
- 核心问题：缺乏系统方法可视化深度学习训练中类别混淆及其关系演化。
- 方法要点：利用中间层线性分类器生成混淆矩阵，并解释为有向图以应用网络科学工具。
- 实验或效果：揭示线性可分性、数据集问题和架构行为，如验证人类研究中的标签歧义。

## 摘要（原文）

> Explainable artificial intelligence has emerged as a promising field of research to address reliability concerns in artificial intelligence. Despite significant progress in explainable artificial intelligence, few methods provide a systematic way to visualize and understand how classes are confused and how their relationships evolve as training progresses. In this work, we present GRAPHIC, an architecture-agnostic approach that analyzes neural networks on a class level. It leverages confusion matrices derived from intermediate layers using linear classifiers. We interpret these as adjacency matrices of directed graphs, allowing tools from network science to visualize and quantify learning dynamics across training epochs and intermediate layers. GRAPHIC provides insights into linear class separability, dataset issues, and architectural behavior, revealing, for example, similarities between flatfish and man and labeling ambiguities validated in a human study. In summary, by uncovering real confusions, GRAPHIC offers new perspectives on how neural networks learn. The code is available at https://github.com/Johanna-S-Froehlich/GRAPHIC.

