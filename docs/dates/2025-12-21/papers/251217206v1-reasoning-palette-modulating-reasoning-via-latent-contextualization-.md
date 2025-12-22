---
layout: default
title: Reasoning Palette: Modulating Reasoning via Latent Contextualization for Controllable Exploration for (V)LMs
---

# Reasoning Palette: Modulating Reasoning via Latent Contextualization for Controllable Exploration for (V)LMs
**arXiv**：[2512.17206v1](https://arxiv.org/abs/2512.17206) · [PDF](https://arxiv.org/pdf/2512.17206.pdf)  
**作者**：Rujiao Long, Yang Li, Xingyao Zhang, Weixun Wang, Tianqianjin Lin, Xi Zhao, Yuchi Xu, Wenbo Su, Junchi Yan, Bo Zheng  

**一句话要点**：提出Reasoning Palette框架，通过潜在变量调制推理轨迹，增强大语言模型的探索能力。

**关键词**：潜在调制, 推理控制, 变分自编码器, 强化学习, 大语言模型

## 3 点简述
- 核心问题：大语言模型在推理和强化学习中探索效率低，路径冗余且多样性不足。
- 方法要点：使用变分自编码器推断潜在上下文，解码为可学习前缀以调制模型内部推理策略。
- 实验或效果：在多个推理基准测试中实现性能提升，支持可解释和可控的推理行为。

## 摘要（原文）

> Exploration capacity shapes both inference-time performance and reinforcement learning (RL) training for large (vision-) language models, as stochastic sampling often yields redundant reasoning paths with little high-level diversity. This paper proposes Reasoning Palette, a novel latent-modulation framework that endows the model with a stochastic latent variable for strategic contextualization, guiding its internal planning prior to token generation. This latent context is inferred from the mean-pooled embedding of a question-answer pair via a variational autoencoder (VAE), where each sampled latent potentially encodes a distinct reasoning context. During inference, a sampled latent is decoded into learnable token prefixes and prepended to the input prompt, modulating the model's internal reasoning trajectory. In this way, the model performs internal sampling over reasoning strategies prior to output generation, which shapes the style and structure of the entire response sequence. A brief supervised fine-tuning (SFT) warm-up phase allows the model to adapt to this latent conditioning. Within RL optimization, Reasoning Palette facilitates structured exploration by enabling on-demand injection for diverse reasoning modes, significantly enhancing exploration efficiency and sustained learning capability. Experiments across multiple reasoning benchmarks demonstrate that our method enables interpretable and controllable control over the (vision-) language model's strategic behavior, thereby achieving consistent performance gains over standard RL methods.

