---
layout: default
title: Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves
---

# Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves
**arXiv**：[2601.21582v1](https://arxiv.org/abs/2601.21582) · [PDF](https://arxiv.org/pdf/2601.21582.pdf)  
**作者**：Jonas Knupp, Jan Hendrik Metzen, Jeremias Bohn, Georg Groh, Kristian Kersting  

**一句话要点**：提出深度循环注意力混合框架以解决深度循环模型中隐藏尺寸瓶颈和参数利用不足问题

**关键词**：深度循环模型, 注意力机制, 稀疏专家, 语言推理, 参数效率, 隐藏尺寸瓶颈

## 3 点简述
- 核心问题：深度循环模型存在隐藏尺寸瓶颈、参数利用不足和缺乏匹配基线的问题
- 方法要点：结合序列注意力、深度注意力和稀疏专家注意力，通过模块化框架缓解瓶颈并解耦缩放维度
- 实验或效果：在语言推理基准上，以更少训练标记达到相同准确度，并超越更大模型

## 摘要（原文）

> Depth-recurrence facilitates latent reasoning by sharing parameters across depths. However, prior work lacks combined FLOP-, parameter-, and memory-matched baselines, underutilizes depth-recurrence due to partially fixed layer stacks, and ignores the bottleneck of constant hidden-sizes that restricts many-step latent reasoning. To address this, we introduce a modular framework of depth-recurrent attention mixtures (Dreamer), combining sequence attention, depth attention, and sparse expert attention. It alleviates the hidden-size bottleneck through attention along depth, decouples scaling dimensions, and allows depth-recurrent models to scale efficiently and effectively. Across language reasoning benchmarks, our models require 2 to 8x fewer training tokens for the same accuracy as FLOP-, parameter-, and memory-matched SOTA, and outperform ca. 2x larger SOTA models with the same training tokens. We further present insights into knowledge usage across depths, e.g., showing 2 to 11x larger expert selection diversity than SOTA MoEs.

