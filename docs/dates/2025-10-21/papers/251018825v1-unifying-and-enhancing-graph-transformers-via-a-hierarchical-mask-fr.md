---
layout: default
title: Unifying and Enhancing Graph Transformers via a Hierarchical Mask Framework
---

# Unifying and Enhancing Graph Transformers via a Hierarchical Mask Framework
**arXiv**：[2510.18825v1](https://arxiv.org/abs/2510.18825) · [PDF](https://arxiv.org/pdf/2510.18825.pdf)  
**作者**：Yujie Xing, Xiao Wang, Bin Wu, Hai Huang, Chuan Shi  

**一句话要点**：提出统一层次掩码框架与M3Dphormer模型，以增强图变换器的灵活性与性能。

**关键词**：图变换器, 注意力掩码, 层次建模, 混合专家, 双注意力计算, 图表示学习

## 3 点简述
- 现有图变换器依赖特定架构，灵活性受限，无法统一建模多样节点交互。
- 引入层次掩码框架，统一架构与注意力掩码，并设计M3Dphormer集成多级掩码与双注意力计算。
- 多基准实验显示M3Dphormer达到最先进性能，验证框架与模型有效性。

## 摘要（原文）

> Graph Transformers (GTs) have emerged as a powerful paradigm for graph
> representation learning due to their ability to model diverse node
> interactions. However, existing GTs often rely on intricate architectural
> designs tailored to specific interactions, limiting their flexibility. To
> address this, we propose a unified hierarchical mask framework that reveals an
> underlying equivalence between model architecture and attention mask
> construction. This framework enables a consistent modeling paradigm by
> capturing diverse interactions through carefully designed attention masks.
> Theoretical analysis under this framework demonstrates that the probability of
> correct classification positively correlates with the receptive field size and
> label consistency, leading to a fundamental design principle: an effective
> attention mask should ensure both a sufficiently large receptive field and a
> high level of label consistency. While no single existing mask satisfies this
> principle across all scenarios, our analysis reveals that hierarchical masks
> offer complementary strengths, motivating their effective integration. Then, we
> introduce M3Dphormer, a Mixture-of-Experts-based Graph Transformer with
> Multi-Level Masking and Dual Attention Computation. M3Dphormer incorporates
> three theoretically grounded hierarchical masks and employs a bi-level expert
> routing mechanism to adaptively integrate multi-level interaction information.
> To ensure scalability, we further introduce a dual attention computation scheme
> that dynamically switches between dense and sparse modes based on local mask
> sparsity. Extensive experiments across multiple benchmarks demonstrate that
> M3Dphormer achieves state-of-the-art performance, validating the effectiveness
> of our unified framework and model design.

