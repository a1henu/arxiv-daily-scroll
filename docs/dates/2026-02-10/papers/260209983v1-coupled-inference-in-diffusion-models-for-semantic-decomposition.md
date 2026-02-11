---
layout: default
title: Coupled Inference in Diffusion Models for Semantic Decomposition
---

# Coupled Inference in Diffusion Models for Semantic Decomposition
**arXiv**：[2602.09983v1](https://arxiv.org/abs/2602.09983) · [PDF](https://arxiv.org/pdf/2602.09983.pdf)  
**作者**：Calvin Yeung, Ali Zakeri, Zhuowen Zou, Mohsen Imani  

**一句话要点**：提出基于扩散模型耦合推理的语义分解框架，以解决视觉场景的潜在因子分解问题。

**关键词**：扩散模型, 语义分解, 耦合推理, 逆问题, 谐振子网络, 视觉场景理解

## 3 点简述
- 核心问题：视觉场景的语义分解，即从组合表示中分离潜在因子，以支持识别、推理和编辑。
- 方法要点：将语义分解建模为逆问题，通过重建引导项耦合扩散过程，并引入迭代采样方案提升性能。
- 实验或效果：在合成语义分解任务中，该框架优于谐振子网络，并证明后者为其特例。

## 摘要（原文）

> Many visual scenes can be described as compositions of latent factors. Effective recognition, reasoning, and editing often require not only forming such compositional representations, but also solving the decomposition problem. One popular choice for constructing these representations is through the binding operation. Resonator networks, which can be understood as coupled Hopfield networks, were proposed as a way to perform decomposition on such bound representations. Recent works have shown notable similarities between Hopfield networks and diffusion models. Motivated by these observations, we introduce a framework for semantic decomposition using coupled inference in diffusion models. Our method frames semantic decomposition as an inverse problem and couples the diffusion processes using a reconstruction-driven guidance term that encourages the composition of factor estimates to match the bound vector. We also introduce a novel iterative sampling scheme that improves the performance of our model. Finally, we show that attention-based resonator networks are a special case of our framework. Empirically, we demonstrate that our coupled inference framework outperforms resonator networks across a range of synthetic semantic decomposition tasks.

