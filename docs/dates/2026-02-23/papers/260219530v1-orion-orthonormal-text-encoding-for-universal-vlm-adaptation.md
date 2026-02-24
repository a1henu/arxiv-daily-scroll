---
layout: default
title: ORION: ORthonormal Text Encoding for Universal VLM AdaptatION
---

# ORION: ORthonormal Text Encoding for Universal VLM AdaptatION
**arXiv**：[2602.19530v1](https://arxiv.org/abs/2602.19530) · [PDF](https://arxiv.org/pdf/2602.19530.pdf)  
**作者**：Omprakash Chakraborty, Jose Dolz, Ismail Ben Ayed  

**一句话要点**：提出ORION框架，通过正交化文本编码优化视觉语言模型在分类任务中的性能。

**关键词**：视觉语言模型, 文本编码优化, 正交化损失, 低秩适应, 零样本分类, 测试时适应

## 3 点简述
- 核心问题：标准零样本分类器因文本原型嵌入相关或分离弱，限制任务特定判别性。
- 方法要点：基于低秩适应优化损失函数，结合类间正交性和原型偏差惩罚，仅使用类名微调文本编码器。
- 实验或效果：在11个基准和3个VLM骨干上验证，作为即插即用模块提升零样本、少样本和测试时适应性能。

## 摘要（原文）

> Vision language models (VLMs) have demonstrated remarkable generalization across diverse tasks, yet their performance remains constrained by the quality and geometry of the textual prototypes used to represent classes. Standard zero shot classifiers, derived from frozen text encoders and handcrafted prompts, may yield correlated or weakly separated embeddings that limit task specific discriminability. We introduce ORION, a text encoder fine tuning framework that improves pretrained VLMs using only class names. Our method optimizes, via low rank adaptation, a novel loss integrating two terms, one promoting pairwise orthogonality between the textual representations of the classes of a given task and the other penalizing deviations from the initial class prototypes. Furthermore, we provide a probabilistic interpretation of our orthogonality penalty, connecting it to the general maximum likelihood estimation (MLE) principle via Huygens theorem. We report extensive experiments on 11 benchmarks and three large VLM backbones, showing that the refined textual embeddings yield powerful replacements for the standard CLIP prototypes. Added as plug and play module on top of various state of the art methods, and across different prediction settings (zero shot, few shot and test time adaptation), ORION improves the performance consistently and significantly.

