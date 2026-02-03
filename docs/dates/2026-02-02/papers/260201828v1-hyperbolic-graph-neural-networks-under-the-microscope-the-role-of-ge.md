---
layout: default
title: Hyperbolic Graph Neural Networks Under the Microscope: The Role of Geometry-Task Alignment
---

# Hyperbolic Graph Neural Networks Under the Microscope: The Role of Geometry-Task Alignment
**arXiv**：[2602.01828v1](https://arxiv.org/abs/2602.01828) · [PDF](https://arxiv.org/pdf/2602.01828.pdf)  
**作者**：Dionisia Naddeo, Jonas Linkerhägner, Nicola Toschi, Geri Skenderi, Veronica Lachi  

**一句话要点**：提出几何-任务对齐条件，揭示双曲图神经网络在度量结构对齐任务中优势

**关键词**：双曲图神经网络, 几何-任务对齐, 度量结构, 链接预测, 节点分类, 表示学习

## 3 点简述
- 核心问题：质疑双曲图神经网络仅基于图的双曲性选择，强调任务与几何对齐的重要性
- 方法要点：理论结合实验，分析HGNN在合成回归问题中的低失真表示能力，评估链接预测与节点分类的几何对齐性
- 实验或效果：发现链接预测为几何对齐任务，HGNN在此类任务中优于欧几里得模型，否则优势消失

## 摘要（原文）

> Many complex networks exhibit hyperbolic structural properties, making hyperbolic space a natural candidate for representing hierarchical and tree-like graphs with low distortion. Based on this observation, Hyperbolic Graph Neural Networks (HGNNs) have been widely adopted as a principled choice for representation learning on tree-like graphs. In this work, we question this paradigm by proposing an additional condition of geometry-task alignment, i.e., whether the metric structure of the target follows that of the input graph. We theoretically and empirically demonstrate the capability of HGNNs to recover low-distortion representations on two synthetic regression problems, and show that their geometric inductive bias becomes helpful when the problem requires preserving metric structure. Additionally, we evaluate HGNNs on the tasks of link prediction and node classification by jointly analyzing predictive performance and embedding distortion, revealing that only link prediction is geometry-aligned. Overall, our findings shift the focus from only asking "Is the graph hyperbolic?" to also questioning "Is the task aligned with hyperbolic geometry?", showing that HGNNs consistently outperform Euclidean models under such alignment, while their advantage vanishes otherwise.

