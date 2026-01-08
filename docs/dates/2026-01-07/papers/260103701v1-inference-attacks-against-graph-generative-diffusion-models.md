---
layout: default
title: Inference Attacks Against Graph Generative Diffusion Models
---

# Inference Attacks Against Graph Generative Diffusion Models
**arXiv**：[2601.03701v1](https://arxiv.org/abs/2601.03701) · [PDF](https://arxiv.org/pdf/2601.03701.pdf)  
**作者**：Xiuling Wang, Xin Huang, Guibo Luo, Jianliang Xu  

**一句话要点**：提出针对图生成扩散模型的三种黑盒推理攻击，揭示其隐私风险并设计防御机制。

**关键词**：图生成扩散模型, 隐私攻击, 推理攻击, 图重构, 成员推理, 防御机制

## 3 点简述
- 核心问题：图生成扩散模型的隐私风险未充分探索，存在信息泄露隐患。
- 方法要点：设计图重构攻击、属性推理攻击和成员推理攻击，从生成图中推断训练数据信息。
- 实验或效果：在三种模型和六个真实图上验证攻击有效性，并提出防御机制平衡安全与效用。

## 摘要（原文）

> Graph generative diffusion models have recently emerged as a powerful paradigm for generating complex graph structures, effectively capturing intricate dependencies and relationships within graph data. However, the privacy risks associated with these models remain largely unexplored. In this paper, we investigate information leakage in such models through three types of black-box inference attacks. First, we design a graph reconstruction attack, which can reconstruct graphs structurally similar to those training graphs from the generated graphs. Second, we propose a property inference attack to infer the properties of the training graphs, such as the average graph density and the distribution of densities, from the generated graphs. Third, we develop two membership inference attacks to determine whether a given graph is present in the training set. Extensive experiments on three different types of graph generative diffusion models and six real-world graphs demonstrate the effectiveness of these attacks, significantly outperforming the baseline approaches. Finally, we propose two defense mechanisms that mitigate these inference attacks and achieve a better trade-off between defense strength and target model utility than existing methods. Our code is available at https://zenodo.org/records/17946102.

