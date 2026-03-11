---
layout: default
title: Fine-grained Motion Retrieval via Joint-Angle Motion Images and Token-Patch Late Interaction
---

# Fine-grained Motion Retrieval via Joint-Angle Motion Images and Token-Patch Late Interaction
**arXiv**：[2603.09930v1](https://arxiv.org/abs/2603.09930) · [PDF](https://arxiv.org/pdf/2603.09930.pdf)  
**作者**：Yao Zhang, Zhuchenyang Liu, Yanlan He, Thomas Ploetz, Yu Xiao  

**一句话要点**：提出基于关节角运动图像和令牌-补丁延迟交互的细粒度运动检索方法，以提升文本-运动对齐精度和可解释性。

**关键词**：文本-运动检索, 细粒度对齐, 关节角运动图像, 延迟交互, 可解释性, 视觉Transformer

## 3 点简述
- 核心问题：现有文本-运动检索方法使用全局嵌入，忽略细粒度局部对应，导致精度降低和可解释性有限。
- 方法要点：设计关节角运动图像表示，结合预训练视觉Transformer和MaxSim延迟交互机制，增强文本-运动对齐。
- 实验或效果：在HumanML3D和KIT-ML数据集上超越现有方法，提供可解释的细粒度对应。

## 摘要（原文）

> Text-motion retrieval aims to learn a semantically aligned latent space between natural language descriptions and 3D human motion skeleton sequences, enabling bidirectional search across the two modalities. Most existing methods use a dual-encoder framework that compresses motion and text into global embeddings, discarding fine-grained local correspondences, and thus reducing accuracy. Additionally, these global-embedding methods offer limited interpretability of the retrieval results. To overcome these limitations, we propose an interpretable, joint-angle-based motion representation that maps joint-level local features into a structured pseudo-image, compatible with pre-trained Vision Transformers. For text-to-motion retrieval, we employ MaxSim, a token-wise late interaction mechanism, and enhance it with Masked Language Modeling regularization to foster robust, interpretable text-motion alignment. Extensive experiments on HumanML3D and KIT-ML show that our method outperforms state-of-the-art text-motion retrieval approaches while offering interpretable fine-grained correspondences between text and motion. The code is available in the supplementary material.

