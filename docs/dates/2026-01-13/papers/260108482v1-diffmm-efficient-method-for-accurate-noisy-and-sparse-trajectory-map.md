---
layout: default
title: DiffMM: Efficient Method for Accurate Noisy and Sparse Trajectory Map Matching via One Step Diffusion
---

# DiffMM: Efficient Method for Accurate Noisy and Sparse Trajectory Map Matching via One Step Diffusion
**arXiv**：[2601.08482v1](https://arxiv.org/abs/2601.08482) · [PDF](https://arxiv.org/pdf/2601.08482.pdf)  
**作者**：Chenxu Han, Sean Bin Yang, Jilin Hu  

**一句话要点**：提出DiffMM，通过一步扩散方法高效解决稀疏和噪声轨迹的地图匹配问题。

**关键词**：地图匹配, 轨迹处理, 扩散模型, 注意力机制, 稀疏轨迹, 路网拓扑

## 3 点简述
- 核心问题：现有HMM或编码器-解码器方法在处理噪声或稀疏GPS轨迹时面临挑战。
- 方法要点：使用道路段感知轨迹编码器，通过注意力机制嵌入轨迹和候选道路段，并采用一步扩散过程实现匹配。
- 实验或效果：在大规模轨迹数据集上验证，在准确性和效率上优于现有方法，尤其适用于稀疏轨迹和复杂路网。

## 摘要（原文）

> Map matching for sparse trajectories is a fundamental problem for many trajectory-based applications, e.g., traffic scheduling and traffic flow analysis. Existing methods for map matching are generally based on Hidden Markov Model (HMM) or encoder-decoder framework. However, these methods continue to face significant challenges when handling noisy or sparsely sampled GPS trajectories. To address these limitations, we propose DiffMM, an encoder-diffusion-based map matching framework that produces effective yet efficient matching results through a one-step diffusion process. We first introduce a road segment-aware trajectory encoder that jointly embeds the input trajectory and its surrounding candidate road segments into a shared latent space through an attention mechanism. Next, we propose a one step diffusion method to realize map matching through a shortcut model by leveraging the joint embedding of the trajectory and candidate road segments as conditioning context. We conduct extensive experiments on large-scale trajectory datasets, demonstrating that our approach consistently outperforms state-of-the-art map matching methods in terms of both accuracy and efficiency, particularly for sparse trajectories and complex road network topologies.

