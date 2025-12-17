---
layout: default
title: Beyond MMD: Evaluating Graph Generative Models with Geometric Deep Learning
---

# Beyond MMD: Evaluating Graph Generative Models with Geometric Deep Learning
**arXiv**：[2512.14241v1](https://arxiv.org/abs/2512.14241) · [PDF](https://arxiv.org/pdf/2512.14241.pdf)  
**作者**：Salvatore Romano, Marco Grassia, Giuseppe Mangioni  

**一句话要点**：提出RGM方法以解决图生成模型评估中MMD的局限性

**关键词**：图生成模型, 几何深度学习, 模型评估, 图结构分析, RGM方法

## 3 点简述
- 核心问题：图生成模型评估依赖MMD，但MMD无法充分捕捉图的结构特性差异
- 方法要点：引入RGM，基于几何深度学习模型评估生成图的表示和结构相似性
- 实验或效果：评估GRAN和EDGE模型，揭示其在保持不同图域结构特征方面的局限性

## 摘要（原文）

> Graph generation is a crucial task in many fields, including network science and bioinformatics, as it enables the creation of synthetic graphs that mimic the properties of real-world networks for various applications. Graph Generative Models (GGMs) have emerged as a promising solution to this problem, leveraging deep learning techniques to learn the underlying distribution of real-world graphs and generate new samples that closely resemble them. Examples include approaches based on Variational Auto-Encoders, Recurrent Neural Networks, and more recently, diffusion-based models. However, the main limitation often lies in the evaluation process, which typically relies on Maximum Mean Discrepancy (MMD) as a metric to assess the distribution of graph properties in the generated ensemble. This paper introduces a novel methodology for evaluating GGMs that overcomes the limitations of MMD, which we call RGM (Representation-aware Graph-generation Model evaluation). As a practical demonstration of our methodology, we present a comprehensive evaluation of two state-of-the-art Graph Generative Models: Graph Recurrent Attention Networks (GRAN) and Efficient and Degree-guided graph GEnerative model (EDGE). We investigate their performance in generating realistic graphs and compare them using a Geometric Deep Learning model trained on a custom dataset of synthetic and real-world graphs, specifically designed for graph classification tasks. Our findings reveal that while both models can generate graphs with certain topological properties, they exhibit significant limitations in preserving the structural characteristics that distinguish different graph domains. We also highlight the inadequacy of Maximum Mean Discrepancy as an evaluation metric for GGMs and suggest alternative approaches for future research.

