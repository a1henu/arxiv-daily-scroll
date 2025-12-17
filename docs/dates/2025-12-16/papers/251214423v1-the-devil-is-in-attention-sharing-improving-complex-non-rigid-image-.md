---
layout: default
title: The Devil is in Attention Sharing: Improving Complex Non-rigid Image Editing Faithfulness via Attention Synergy
---

# The Devil is in Attention Sharing: Improving Complex Non-rigid Image Editing Faithfulness via Attention Synergy
**arXiv**：[2512.14423v1](https://arxiv.org/abs/2512.14423) · [PDF](https://arxiv.org/pdf/2512.14423.pdf)  
**作者**：Zhuo Chen, Fanyue Wei, Runze Xu, Jingjing Li, Lixin Duan, Angela Yao, Wen Li  

**一句话要点**：提出SynPS方法，通过注意力协同机制解决复杂非刚性图像编辑中的忠实性问题。

**关键词**：图像编辑, 注意力机制, 非刚性变形, 扩散模型, 忠实性评估

## 3 点简述
- 核心问题：现有注意力共享机制存在注意力崩溃，导致位置嵌入或语义特征主导编辑，引发过度或不足编辑。
- 方法要点：引入SynPS，动态调制位置嵌入影响，协同位置与语义信息，平衡编辑幅度与保真度。
- 实验或效果：在公开和新基准上验证，SynPS在复杂非刚性编辑中表现出优越性能和忠实性。

## 摘要（原文）

> Training-free image editing with large diffusion models has become practical, yet faithfully performing complex non-rigid edits (e.g., pose or shape changes) remains highly challenging. We identify a key underlying cause: attention collapse in existing attention sharing mechanisms, where either positional embeddings or semantic features dominate visual content retrieval, leading to over-editing or under-editing.To address this issue, we introduce SynPS, a method that Synergistically leverages Positional embeddings and Semantic information for faithful non-rigid image editing. We first propose an editing measurement that quantifies the required editing magnitude at each denoising step. Based on this measurement, we design an attention synergy pipeline that dynamically modulates the influence of positional embeddings, enabling SynPS to balance semantic modifications and fidelity preservation.By adaptively integrating positional and semantic cues, SynPS effectively avoids both over- and under-editing. Extensive experiments on public and newly curated benchmarks demonstrate the superior performance and faithfulness of our approach.

