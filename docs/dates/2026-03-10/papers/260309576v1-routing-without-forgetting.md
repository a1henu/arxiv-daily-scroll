---
layout: default
title: Routing without Forgetting
---

# Routing without Forgetting
**arXiv**：[2603.09576v1](https://arxiv.org/abs/2603.09576) · [PDF](https://arxiv.org/pdf/2603.09576.pdf)  
**作者**：Alessio Masano, Giovanni Bellitto, Dipam Goswani, Joost Van de Weijer, Concetto Spampinato  

**一句话要点**：提出基于能量关联检索的路由方法，以解决Transformer在线持续学习中的动态子空间选择问题。

**关键词**：在线持续学习, Transformer路由, 能量关联检索, 动态提示生成, 类增量学习

## 3 点简述
- 核心问题：在线持续学习中，传统参数高效方法依赖梯度优化，难以处理单次观察的非平稳数据流。
- 方法要点：引入能量关联检索层，通过单步检索生成动态提示，实现前向传播中的输入条件路由。
- 实验或效果：在Split-ImageNet等基准上，显著优于现有提示方法，支持少样本学习。

## 摘要（原文）

> Continual learning in transformers is commonly addressed through parameter-efficient adaptation: prompts, adapters, or LoRA modules are specialized per task while the backbone remains frozen. Although effective in controlled multi-epoch settings, these approaches rely on gradual gradient-based specialization and struggle in Online Continual Learning (OCL), where data arrive as a non-stationary stream and each sample may be observed only once. We recast continual learning in transformers as a routing problem: under strict online constraints, the model must dynamically select the appropriate representational subspace for each input without explicit task identifiers or repeated optimization. We thus introduce Routing without Forgetting (RwF), a transformer architecture augmented with energy-based associative retrieval layers inspired by Modern Hopfield Networks. Instead of storing or merging task-specific prompts, RwF generates dynamic prompts through single-step associative retrieval over the transformer token embeddings at each layer. Retrieval corresponds to the closed-form minimization of a strictly convex free-energy functional, enabling input-conditioned routing within each forward pass, independently of iterative gradient refinement. Across challenging class-incremental benchmarks, RwF improves over existing prompt-based methods. On Split-ImageNet-R and Split-ImageNet-S, RwF outperforms prior prompt-based approaches by a large margin, even in few-shot learning regimes. These results indicate that embedding energy-based associative routing directly within the transformer backbone provides a principled and effective foundation for OCL.

