---
layout: default
title: Sequence Diffusion Model for Temporal Link Prediction in Continuous-Time Dynamic Graph
---

# Sequence Diffusion Model for Temporal Link Prediction in Continuous-Time Dynamic Graph
**arXiv**：[2601.23233v1](https://arxiv.org/abs/2601.23233) · [PDF](https://arxiv.org/pdf/2601.23233.pdf)  
**作者**：Nguyen Minh Duc, Viet Cuong Ta  

**一句话要点**：提出序列扩散模型SDG，用于连续时间动态图中的时序链接预测。

**关键词**：时序链接预测, 动态图学习, 扩散模型, 生成去噪, 连续时间图

## 3 点简述
- 核心问题：现有时序图神经网络缺乏显式机制捕捉未来交互的不确定性和序列结构。
- 方法要点：通过条件去噪过程联合重构历史交互序列，以捕获更全面的交互分布。
- 实验或效果：在多个时序图基准测试中，SDG持续实现最先进的预测性能。

## 摘要（原文）

> Temporal link prediction in dynamic graphs is a fundamental problem in many real-world systems. Existing temporal graph neural networks mainly focus on learning representations of historical interactions. Despite their strong performance, these models are still purely discriminative, producing point estimates for future links and lacking an explicit mechanism to capture the uncertainty and sequential structure of future temporal interactions. In this paper, we propose SDG, a novel sequence-level diffusion framework that unifies dynamic graph learning with generative denoising. Specifically, SDG injects noise into the entire historical interaction sequence and jointly reconstructs all interaction embeddings through a conditional denoising process, thereby enabling the model to capture more comprehensive interaction distributions. To align the generative process with temporal link prediction, we employ a cross-attention denoising decoder to guide the reconstruction of the destination sequence and optimize the model in an end-to-end manner. Extensive experiments on various temporal graph benchmarks show that SDG consistently achieves state-of-the-art performance in the temporal link prediction task.

