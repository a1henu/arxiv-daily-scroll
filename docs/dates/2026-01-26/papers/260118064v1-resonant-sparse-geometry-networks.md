---
layout: default
title: Resonant Sparse Geometry Networks
---

# Resonant Sparse Geometry Networks
**arXiv**：[2601.18064v1](https://arxiv.org/abs/2601.18064) · [PDF](https://arxiv.org/pdf/2601.18064.pdf)  
**作者**：Hasi Hays  

**一句话要点**：提出共振稀疏几何网络以解决Transformer计算复杂度高和参数冗余问题

**关键词**：稀疏神经网络, 几何计算, Hebbian学习, 双曲空间, 层次分类, 长距离依赖

## 3 点简述
- 核心问题：Transformer架构因密集注意力机制导致O(n²)计算复杂度和参数冗余，限制了效率和生物合理性。
- 方法要点：RSGN采用自组织稀疏层次连接，在双曲空间中嵌入节点，通过局部相关规则实现动态稀疏性和Hebbian结构学习。
- 实验效果：在长距离依赖任务上达到96.5%准确率，参数减少约15倍；在20类层次分类任务上以41,672参数实现23.8%准确率。

## 摘要（原文）

> We introduce Resonant Sparse Geometry Networks (RSGN), a brain-inspired architecture with self-organizing sparse
>   hierarchical input-dependent connectivity. Unlike Transformer architectures that employ dense attention mechanisms with
>   O(n^2) computational complexity, RSGN embeds computational nodes in learned hyperbolic space where connection strength
>   decays with geodesic distance, achieving dynamic sparsity that adapts to each input. The architecture operates on two
>   distinct timescales: fast differentiable activation propagation optimized through gradient descent, and slow
>   Hebbian-inspired structural learning for connectivity adaptation through local correlation rules. We provide rigorous
>   mathematical analysis demonstrating that RSGN achieves O(n*k) computational complexity, where k << n represents the average
>   active neighborhood size. Experimental evaluation on hierarchical classification and long-range dependency tasks
>   demonstrates that RSGN achieves 96.5% accuracy on long-range dependency tasks while using approximately 15x fewer
>   parameters than standard Transformers. On challenging hierarchical classification with 20 classes, RSGN achieves 23.8%
>   accuracy (compared to 5% random baseline) with only 41,672 parameters, nearly 10x fewer than the Transformer baselines
>   which require 403,348 parameters to achieve 30.1% accuracy. Our ablation studies confirm the contribution of each architectural
>   component, with Hebbian learning providing consistent improvements. These results suggest that brain-inspired principles
>   of sparse, geometrically-organized computation offer a promising direction toward more efficient and biologically plausible
>   neural architectures.

