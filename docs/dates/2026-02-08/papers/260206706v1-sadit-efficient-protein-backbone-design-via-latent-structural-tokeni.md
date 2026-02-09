---
layout: default
title: SaDiT: Efficient Protein Backbone Design via Latent Structural Tokenization and Diffusion Transformers
---

# SaDiT: Efficient Protein Backbone Design via Latent Structural Tokenization and Diffusion Transformers
**arXiv**：[2602.06706v1](https://arxiv.org/abs/2602.06706) · [PDF](https://arxiv.org/pdf/2602.06706.pdf)  
**作者**：Shentong Mo, Lanqing Li  

**一句话要点**：提出SaDiT框架，通过潜在结构标记化和扩散变换器加速蛋白质骨架设计

**关键词**：蛋白质骨架设计, 扩散变换器, 结构标记化, 计算加速, 无条件生成, 条件生成

## 3 点简述
- 核心问题：基于扩散的蛋白质骨架生成模型计算密集，影响大规模结构探索效率
- 方法要点：结合SaProt标记化和扩散变换器，利用离散潜在空间和IPA令牌缓存优化生成过程
- 实验或效果：在计算速度和结构可行性上优于RFDiffusion和Proteina，能捕捉复杂拓扑特征

## 摘要（原文）

> Generative models for de novo protein backbone design have achieved remarkable success in creating novel protein structures. However, these diffusion-based approaches remain computationally intensive and slower than desired for large-scale structural exploration. While recent efforts like Proteina have introduced flow-matching to improve sampling efficiency, the potential of tokenization for structural compression and acceleration remains largely unexplored in the protein domain. In this work, we present SaDiT, a novel framework that accelerates protein backbone generation by integrating SaProt Tokenization with a Diffusion Transformer (DiT) architecture. SaDiT leverages a discrete latent space to represent protein geometry, significantly reducing the complexity of the generation process while maintaining theoretical SE(3) equivalence. To further enhance efficiency, we introduce an IPA Token Cache mechanism that optimizes the Invariant Point Attention (IPA) layers by reusing computed token states during iterative sampling. Experimental results demonstrate that SaDiT outperforms state-of-the-art models, including RFDiffusion and Proteina, in both computational speed and structural viability. We evaluate our model across unconditional backbone generation and fold-class conditional generation tasks, where SaDiT shows superior ability to capture complex topological features with high designability.

