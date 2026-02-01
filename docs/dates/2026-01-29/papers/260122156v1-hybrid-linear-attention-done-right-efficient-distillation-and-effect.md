---
layout: default
title: Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts
---

# Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts
**arXiv**：[2601.22156v1](https://arxiv.org/abs/2601.22156) · [PDF](https://arxiv.org/pdf/2601.22156.pdf)  
**作者**：Yingfa Chen, Zhen Leng Thai, Zihan Zhou, Zhu Zhang, Xingyu Shen, Shuo Wang, Chaojun Xiao, Xu Han, Zhiyuan Liu  

**一句话要点**：提出HALO蒸馏管道与HypeNet架构，以高效转换Transformer为混合模型，提升长上下文性能与效率。

**关键词**：混合注意力模型, 知识蒸馏, 长上下文建模, 位置编码, Transformer转换, 推理效率

## 3 点简述
- 核心问题：混合Transformer模型预训练成本高，现有转换方法需大量数据且长上下文性能差。
- 方法要点：HALO蒸馏管道仅需少量数据转换，HypeNet架构引入HyPE位置编码优化长度泛化。
- 实验或效果：将Qwen3转换为HypeNet，性能接近原模型，长上下文效率显著提升。

## 摘要（原文）

> Hybrid Transformer architectures, which combine softmax attention blocks and recurrent neural networks (RNNs), have shown a desirable performance-throughput tradeoff for long-context modeling, but their adoption and studies are hindered by the prohibitive cost of large-scale pre-training from scratch. Some recent studies have shown that pre-trained softmax attention blocks can be converted into RNN blocks through parameter transfer and knowledge distillation. However, these transfer methods require substantial amounts of training data (more than 10B tokens), and the resulting hybrid models also exhibit poor long-context performance, which is the scenario where hybrid models enjoy significant inference speedups over Transformer-based models. In this paper, we present HALO (Hybrid Attention via Layer Optimization), a pipeline for distilling Transformer models into RNN-attention hybrid models. We then present HypeNet, a hybrid architecture with superior length generalization enabled by a novel position encoding scheme (named HyPE) and various architectural modifications. We convert the Qwen3 series into HypeNet using HALO, achieving performance comparable to the original Transformer models while enjoying superior long-context performance and efficiency. The conversion requires just 2.3B tokens, less than 0.01% of their pre-training data

