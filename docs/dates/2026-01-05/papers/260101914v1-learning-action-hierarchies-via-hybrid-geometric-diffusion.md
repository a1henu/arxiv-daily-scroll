---
layout: default
title: Learning Action Hierarchies via Hybrid Geometric Diffusion
---

# Learning Action Hierarchies via Hybrid Geometric Diffusion
**arXiv**：[2601.01914v1](https://arxiv.org/abs/2601.01914) · [PDF](https://arxiv.org/pdf/2601.01914.pdf)  
**作者**：Arjun Ramesh Kaushik, Nalini K. Ratha, Venu Govindaraju  

**一句话要点**：提出HybridTAS框架，结合欧几里得与双曲几何的扩散模型，以解决时序动作分割中层次结构利用不足的问题。

**关键词**：时序动作分割, 扩散模型, 双曲几何, 层次结构学习, 视频理解

## 3 点简述
- 时序动作分割任务中，现有方法未充分利用动作的层次结构。
- HybridTAS通过混合几何扩散，在去噪过程中利用双曲几何的树状关系实现从粗到细的引导。
- 在GTEA、50Salads和Breakfast数据集上达到最先进性能，验证了方法的有效性。

## 摘要（原文）

> Temporal action segmentation is a critical task in video understanding, where the goal is to assign action labels to each frame in a video. While recent advances leverage iterative refinement-based strategies, they fail to explicitly utilize the hierarchical nature of human actions. In this work, we propose HybridTAS - a novel framework that incorporates a hybrid of Euclidean and hyperbolic geometries into the denoising process of diffusion models to exploit the hierarchical structure of actions. Hyperbolic geometry naturally provides tree-like relationships between embeddings, enabling us to guide the action label denoising process in a coarse-to-fine manner: higher diffusion timesteps are influenced by abstract, high-level action categories (root nodes), while lower timesteps are refined using fine-grained action classes (leaf nodes). Extensive experiments on three benchmark datasets, GTEA, 50Salads, and Breakfast, demonstrate that our method achieves state-of-the-art performance, validating the effectiveness of hyperbolic-guided denoising for the temporal action segmentation task.

