---
layout: default
title: Task-driven Heterophilic Graph Structure Learning
---

# Task-driven Heterophilic Graph Structure Learning
**arXiv**：[2512.23406v1](https://arxiv.org/abs/2512.23406) · [PDF](https://arxiv.org/pdf/2512.23406.pdf)  
**作者**：Ayushman Raghuvanshi, Gonzalo Mateos, Sundeep Prabhakar Chepuri  

**一句话要点**：提出频率引导的图结构学习框架，以解决异配图中图神经网络学习判别性节点表示的难题。

**关键词**：异配图学习, 图结构学习, 图神经网络, 频率引导, 监督拓扑推断, 图滤波器组

## 3 点简述
- 核心问题：异配图中连接节点标签常相异，特征相似性提供弱结构线索，导致图神经网络学习困难。
- 方法要点：通过可学习的特征驱动掩码函数联合推断同配和异配图结构，结合低通和高通图滤波器组处理，并引入基于标签的结构损失进行任务驱动学习。
- 实验或效果：在六个异配基准测试中，该方法持续优于最先进的图神经网络和图重连方法，验证了频率信息与监督拓扑推断结合的优势。

## 摘要（原文）

> Graph neural networks (GNNs) often struggle to learn discriminative node representations for heterophilic graphs, where connected nodes tend to have dissimilar labels and feature similarity provides weak structural cues. We propose frequency-guided graph structure learning (FgGSL), an end-to-end graph inference framework that jointly learns homophilic and heterophilic graph structures along with a spectral encoder. FgGSL employs a learnable, symmetric, feature-driven masking function to infer said complementary graphs, which are processed using pre-designed low- and high-pass graph filter banks. A label-based structural loss explicitly promotes the recovery of homophilic and heterophilic edges, enabling task-driven graph structure learning. We derive stability bounds for the structural loss and establish robustness guarantees for the filter banks under graph perturbations. Experiments on six heterophilic benchmarks demonstrate that FgGSL consistently outperforms state-of-the-art GNNs and graph rewiring methods, highlighting the benefits of combining frequency information with supervised topology inference.

