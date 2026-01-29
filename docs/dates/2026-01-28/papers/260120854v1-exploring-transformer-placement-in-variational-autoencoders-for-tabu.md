---
layout: default
title: Exploring Transformer Placement in Variational Autoencoders for Tabular Data Generation
---

# Exploring Transformer Placement in Variational Autoencoders for Tabular Data Generation
**arXiv**：[2601.20854v1](https://arxiv.org/abs/2601.20854) · [PDF](https://arxiv.org/pdf/2601.20854.pdf)  
**作者**：Aníbal Silva, Moisés Santos, André Restivo, Carlos Soares  

**一句话要点**：探索Transformer在变分自编码器中的位置以提升表格数据生成效果

**关键词**：表格数据生成, 变分自编码器, Transformer, 特征交互, 混合数据类型, 生成模型

## 3 点简述
- 核心问题：标准VAE在表格数据生成中难以建模特征间关系，尤其处理混合数据类型时。
- 方法要点：通过实验研究将Transformer集成到VAE不同组件（如潜在空间和解码器）的影响。
- 实验或效果：在57个数据集上测试，发现Transformer位置影响保真度与多样性的权衡，且解码器中Transformer输入输出近似线性。

## 摘要（原文）

> Tabular data remains a challenging domain for generative models. In particular, the standard Variational Autoencoder (VAE) architecture, typically composed of multilayer perceptrons, struggles to model relationships between features, especially when handling mixed data types. In contrast, Transformers, through their attention mechanism, are better suited for capturing complex feature interactions. In this paper, we empirically investigate the impact of integrating Transformers into different components of a VAE. We conduct experiments on 57 datasets from the OpenML CC18 suite and draw two main conclusions. First, results indicate that positioning Transformers to leverage latent and decoder representations leads to a trade-off between fidelity and diversity. Second, we observe a high similarity between consecutive blocks of a Transformer in all components. In particular, in the decoder, the relationship between the input and output of a Transformer is approximately linear.

