---
layout: default
title: Adaptive Edge Learning for Density-Aware Graph Generation
---

# Adaptive Edge Learning for Density-Aware Graph Generation
**arXiv**：[2601.23052v1](https://arxiv.org/abs/2601.23052) · [PDF](https://arxiv.org/pdf/2601.23052.pdf)  
**作者**：Seyedeh Ava Razi Razavi, James Sargant, Sheridan Houghten, Renata Dividino  

**一句话要点**：提出密度感知条件图生成框架，以解决图数据生成中结构依赖性和密度匹配的挑战。

**关键词**：图生成, Wasserstein GAN, 密度感知, 边预测, 条件生成, 图卷积网络

## 3 点简述
- 核心问题：传统图生成方法依赖随机边采样，难以捕捉复杂节点间结构依赖和类特定密度分布。
- 方法要点：使用Wasserstein GAN框架，引入可学习的基于距离的边预测器和密度感知选择机制，从节点嵌入直接生成边。
- 实验或效果：在基准数据集上验证，生成图的结构一致性和类一致性优于基线，训练稳定性高且可控。

## 摘要（原文）

> Generating realistic graph-structured data is challenging due to discrete structures, variable sizes, and class-specific connectivity patterns that resist conventional generative modelling. While recent graph generation methods employ generative adversarial network (GAN) frameworks to handle permutation invariance and irregular topologies, they typically rely on random edge sampling with fixed probabilities, limiting their capacity to capture complex structural dependencies between nodes. We propose a density-aware conditional graph generation framework using Wasserstein GANs (WGAN) that replaces random sampling with a learnable distance-based edge predictor. Our approach embeds nodes into a latent space where proximity correlates with edge likelihood, enabling the generator to learn meaningful connectivity patterns. A differentiable edge predictor determines pairwise relationships directly from node embeddings, while a density-aware selection mechanism adaptively controls edge density to match class-specific sparsity distributions observed in real graphs. We train the model using a WGAN with gradient penalty, employing a GCN-based critic to ensure generated graphs exhibit realistic topology and align with target class distributions. Experiments on benchmark datasets demonstrate that our method produces graphs with superior structural coherence and class-consistent connectivity compared to existing baselines. The learned edge predictor captures complex relational patterns beyond simple heuristics, generating graphs whose density and topology closely match real structural distributions. Our results show improved training stability and controllable synthesis, making the framework effective for realistic graph generation and data augmentation. Source code is publicly available at https://github.com/ava-12/Density_Aware_WGAN.git.

