---
layout: default
title: Prior-Informed Flow Matching for Graph Reconstruction
---

# Prior-Informed Flow Matching for Graph Reconstruction
**arXiv**：[2601.22107v1](https://arxiv.org/abs/2601.22107) · [PDF](https://arxiv.org/pdf/2601.22107.pdf)  
**作者**：Harvey Chen, Nicolas Zilberstein, Santiago Segarra  

**一句话要点**：提出先验信息流匹配方法，以解决基于部分观测的图重构问题。

**关键词**：图重构, 流匹配, 先验信息, 生成模型, 图嵌入

## 3 点简述
- 核心问题：图重构中，经典嵌入方法缺乏全局一致性，生成模型难以融入结构先验。
- 方法要点：结合嵌入先验与连续时间流匹配，通过先验形成初始估计，再应用修正流匹配进行精炼。
- 实验或效果：在不同数据集上，该方法提升经典嵌入性能，优于现有生成基线。

## 摘要（原文）

> We introduce Prior-Informed Flow Matching (PIFM), a conditional flow model for graph reconstruction. Reconstructing graphs from partial observations remains a key challenge; classical embedding methods often lack global consistency, while modern generative models struggle to incorporate structural priors. PIFM bridges this gap by integrating embedding-based priors with continuous-time flow matching. Grounded in a permutation equivariant version of the distortion-perception theory, our method first uses a prior, such as graphons or GraphSAGE/node2vec, to form an informed initial estimate of the adjacency matrix based on local information. It then applies rectified flow matching to refine this estimate, transporting it toward the true distribution of clean graphs and learning a global coupling. Experiments on different datasets demonstrate that PIFM consistently enhances classical embeddings, outperforming them and state-of-the-art generative baselines in reconstruction accuracy.

