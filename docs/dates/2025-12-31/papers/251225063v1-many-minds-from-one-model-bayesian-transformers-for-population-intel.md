---
layout: default
title: Many Minds from One Model: Bayesian Transformers for Population Intelligence
---

# Many Minds from One Model: Bayesian Transformers for Population Intelligence
**arXiv**：[2512.25063v1](https://arxiv.org/abs/2512.25063) · [PDF](https://arxiv.org/pdf/2512.25063.pdf)  
**作者**：Diji Yang, Yi Zhang  

**一句话要点**：提出贝叶斯变换器以从单一预训练模型生成多样模型实例，支持群体智能决策。

**关键词**：贝叶斯变换器, 群体智能, 模型采样, 归一化层, 零样本生成, 强化学习

## 3 点简述
- 核心问题：现代变换器通常训练为单思维系统，缺乏行为多样性。
- 方法要点：通过归一化层偏置的随机变量近似贝叶斯后验，实现从预训练权重采样多样模型实例。
- 实验或效果：在零样本生成和强化学习任务中，群体决策提升语义多样性和任务性能。

## 摘要（原文）

> Despite their scale and success, modern transformers are almost universally trained as single-minded systems: optimization produces one deterministic set of parameters, representing a single functional hypothesis about the data. Motivated by the idea that intelligence emerge from many minds, we propose Population Bayesian Transformers (B-Trans), which transform a standard Large Language Model into a Bayesian Transformer model to supports sampling diverse yet coherent model instances from a single set of pre-trained weights.
>   B-Trans introduces a Bayesian-motivated posterior proxy by treating the bias-like offsets in normalization layers as stochastic variables with a Gaussian variational approximation, inducing a distribution over model behavior without the cost of training full Bayesian neural networks. Sampling from this proxy yields a set of model instances with diverse behaviors while maintaining general competence. To preserve coherence within each generation, we freeze the sampled noise at the sequence level, enforcing temporal consistency across tokens. B-Trans allows for population-level decision-making, where aggregating predictions across sampled individuals significantly enhances exploration. Experiments across zero-shot generation, Reinforcement Learning with Verifiable Rewards (RLVR), and RL without explicit labels demonstrate that B-Trans effectively leverage the wisdom of crowds, yielding superior semantic diversity while achieving better task performance compared to deterministic baselines.

