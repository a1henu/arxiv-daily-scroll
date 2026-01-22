---
layout: default
title: Mirai: Autoregressive Visual Generation Needs Foresight
---

# Mirai: Autoregressive Visual Generation Needs Foresight
**arXiv**：[2601.14671v1](https://arxiv.org/abs/2601.14671) · [PDF](https://arxiv.org/pdf/2601.14671.pdf)  
**作者**：Yonghao Yu, Lang Huang, Zerun Wang, Runyi Li, Toshihiko Yamasaki  

**一句话要点**：提出Mirai框架，通过注入未来信息改进自回归视觉生成模型的全局一致性和收敛速度。

**关键词**：自回归视觉生成, 未来信息注入, 全局一致性, 收敛加速, 图像生成, 因果建模

## 3 点简述
- 核心问题：自回归视觉生成模型因严格因果监督导致全局一致性差和收敛缓慢。
- 方法要点：Mirai框架通过显式或隐式未来信息注入，无需改变架构或增加推理开销。
- 实验或效果：在ImageNet基准上，Mirai加速收敛达10倍，并降低生成FID至4.34。

## 摘要（原文）

> Autoregressive (AR) visual generators model images as sequences of discrete tokens and are trained with next token likelihood. This strict causality supervision optimizes each step only by its immediate next token, which diminishes global coherence and slows convergence. We ask whether foresight, training signals that originate from later tokens, can help AR visual generation. We conduct a series of controlled diagnostics along the injection level, foresight layout, and foresight source axes, unveiling a key insight: aligning foresight to AR models' internal representation on the 2D image grids improves causality modeling. We formulate this insight with Mirai (meaning "future" in Japanese), a general framework that injects future information into AR training with no architecture change and no extra inference overhead: Mirai-E uses explicit foresight from multiple future positions of unidirectional representations, whereas Mirai-I leverages implicit foresight from matched bidirectional representations. Extensive experiments show that Mirai significantly accelerates convergence and improves generation quality. For instance, Mirai can speed up LlamaGen-B's convergence by up to 10$\times$ and reduce the generation FID from 5.34 to 4.34 on the ImageNet class-condition image generation benchmark. Our study highlights that visual autoregressive models need foresight.

