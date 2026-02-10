---
layout: default
title: DirMoE: Dirichlet-routed Mixture of Experts
---

# DirMoE: Dirichlet-routed Mixture of Experts
**arXiv**：[2602.09001v1](https://arxiv.org/abs/2602.09001) · [PDF](https://arxiv.org/pdf/2602.09001.pdf)  
**作者**：Amirhossein Vahidi, Hesam Asadollahzadeh, Navid Akhavan Attar, Marie Moullet, Kevin Ly, Xingyi Yang, Mohammad Lotfollahi  

**一句话要点**：提出DirMoE以解决MoE模型中路由机制非可微和决策混淆的问题

**关键词**：混合专家模型, 可微路由, Dirichlet分布, 变分自编码器, 专家选择, 稀疏性控制

## 3 点简述
- 核心问题：现有MoE路由依赖非可微Top-k+Softmax，混淆专家选择和贡献分配，限制性能与扩展性。
- 方法要点：基于Dirichlet变分自编码器，通过Bernoulli和Dirichlet组件解耦专家选择与贡献，实现端到端可微路由。
- 实验或效果：DirMoE在训练中通过变分ELBO和稀疏性惩罚控制专家激活数，匹配或超越其他方法，提升专家专业化。

## 摘要（原文）

> Mixture-of-Experts (MoE) models have demonstrated exceptional performance in large-scale language models. Existing routers typically rely on non-differentiable Top-$k$+Softmax, limiting their performance and scalability. We argue that two distinct decisions, which experts to activate and how to distribute expert contributions among them, are conflated in standard Top-$k$+Softmax. We introduce Dirichlet-Routed MoE (DirMoE), a novel end-to-end differentiable routing mechanism built on a Dirichlet variational autoencoder framework. This design fundamentally disentangles the core routing problems: expert selection, modeled by a Bernoulli component, and expert contribution among chosen experts, handled by a Dirichlet component. The entire forward pass remains fully differentiable through the use of Gumbel-Sigmoid relaxation for the expert selection and implicit reparameterization for the Dirichlet distribution. Our training objective, a variational ELBO, includes a direct sparsity penalty that precisely controls the number of active experts in expectation, alongside a schedule for key hyperparameters that guides the model from an exploratory to a definitive routing state. Moreover, our DirMoE router matches or exceeds other methods while improving expert specialization.

