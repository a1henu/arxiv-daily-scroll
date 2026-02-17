---
layout: default
title: Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training
---

# Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training
**arXiv**：[2602.14759v1](https://arxiv.org/abs/2602.14759) · [PDF](https://arxiv.org/pdf/2602.14759.pdf)  
**作者**：Jonathan Lys, Vincent Gripon, Bastien Pasdeloup, Lukas Mauch, Fabien Cardinaux, Ghouthi Boukli Hacene  

**一句话要点**：提出推理时内部循环方法，通过重复应用选定块范围提升预训练语言模型性能

**关键词**：Transformer模型, 推理优化, 内部表示, 精炼机制, 预训练语言模型, 零训练改进

## 3 点简述
- 核心问题：Transformer内部表示被视为迭代精炼，但标准推理可能未充分利用精炼潜力
- 方法要点：在推理时对选定Transformer块范围进行内部循环，延长精炼过程而不训练模型
- 实验或效果：在多个基准测试中，内部循环带来小幅但一致的准确率提升，分析显示更稳定的状态演化和持续语义精炼

## 摘要（原文）

> Deep Learning architectures, and in particular Transformers, are conventionally viewed as a composition of layers. These layers are actually often obtained as the sum of two contributions: a residual path that copies the input and the output of a Transformer block. As a consequence, the inner representations (i.e. the input of these blocks) can be interpreted as iterative refinement of a propagated latent representation. Under this lens, many works suggest that the inner space is shared across layers, meaning that tokens can be decoded at early stages. Mechanistic interpretability even goes further by conjecturing that some layers act as refinement layers. Following this path, we propose inference-time inner looping, which prolongs refinement in pretrained off-the-shelf language models by repeatedly re-applying a selected block range. Across multiple benchmarks, inner looping yields modest but consistent accuracy improvements. Analyses of the resulting latent trajectories suggest more stable state evolution and continued semantic refinement. Overall, our results suggest that additional refinement can be obtained through simple test-time looping, extending computation in frozen pretrained models.

