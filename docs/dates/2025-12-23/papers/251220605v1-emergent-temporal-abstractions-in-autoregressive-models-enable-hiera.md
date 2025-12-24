---
layout: default
title: Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning
---

# Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning
**arXiv**：[2512.20605v1](https://arxiv.org/abs/2512.20605) · [PDF](https://arxiv.org/pdf/2512.20605.pdf)  
**作者**：Seijin Kobayashi, Yanick Schimpf, Maximilian Schlegel, Angelika Steger, Maciej Wolczyk, Johannes von Oswald, Nino Scherre, Kaitlin Maile, Guillaume Lajoie, Blake A. Richards, Rif A. Saurous, James Manyika, Blaise Agüera y Arcas, Alexander Meulemans, João Sacramento  

**一句话要点**：提出内部强化学习以在自回归模型中实现分层强化学习，解决稀疏奖励下的探索效率问题。

**关键词**：自回归模型, 分层强化学习, 时间抽象动作, 内部强化学习, 稀疏奖励, 探索效率

## 3 点简述
- 核心问题：自回归模型在强化学习中逐令牌采样动作导致探索效率低下，尤其在稀疏奖励场景。
- 方法要点：引入高阶非因果序列模型，通过控制自回归模型的残差流激活来发现时间抽象动作。
- 实验或效果：在网格世界和MuJoCo任务中，模型学习压缩长激活序列到内部控制器，实现高效探索和稀疏奖励学习。

## 摘要（原文）

> Large-scale autoregressive models pretrained on next-token prediction and finetuned with reinforcement learning (RL) have achieved unprecedented success on many problem domains. During RL, these models explore by generating new outputs, one token at a time. However, sampling actions token-by-token can result in highly inefficient learning, particularly when rewards are sparse. Here, we show that it is possible to overcome this problem by acting and exploring within the internal representations of an autoregressive model. Specifically, to discover temporally-abstract actions, we introduce a higher-order, non-causal sequence model whose outputs control the residual stream activations of a base autoregressive model. On grid world and MuJoCo-based tasks with hierarchical structure, we find that the higher-order model learns to compress long activation sequence chunks onto internal controllers. Critically, each controller executes a sequence of behaviorally meaningful actions that unfold over long timescales and are accompanied with a learned termination condition, such that composing multiple controllers over time leads to efficient exploration on novel tasks. We show that direct internal controller reinforcement, a process we term "internal RL", enables learning from sparse rewards in cases where standard RL finetuning fails. Our results demonstrate the benefits of latent action generation and reinforcement in autoregressive models, suggesting internal RL as a promising avenue for realizing hierarchical RL within foundation models.

