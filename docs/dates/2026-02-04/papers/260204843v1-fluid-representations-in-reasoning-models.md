---
layout: default
title: Fluid Representations in Reasoning Models
---

# Fluid Representations in Reasoning Models
**arXiv**：[2602.04843v1](https://arxiv.org/abs/2602.04843) · [PDF](https://arxiv.org/pdf/2602.04843.pdf)  
**作者**：Dmitrii Kharlapenko, Alessandro Stolfo, Arthur Conmy, Mrinmaya Sachan, Zhijing Jin  

**一句话要点**：提出流体推理表示以揭示推理语言模型在抽象问题中的内部机制

**关键词**：推理语言模型, 机制分析, 抽象表示, 引导实验, 语义混淆规划

## 3 点简述
- 核心问题：推理语言模型在抽象问题中性能优越的内部机制尚不明确
- 方法要点：通过机制分析研究QwQ-32B在语义混淆规划域中的表示演化
- 实验或效果：通过引导实验证明抽象编码对问题解决的因果提升作用

## 摘要（原文）

> Reasoning language models, which generate long chains of thought, dramatically outperform non-reasoning language models on abstract problems. However, the internal model mechanisms that allow this superior performance remain poorly understood. We present a mechanistic analysis of how QwQ-32B - a model specifically trained to produce extensive reasoning traces - process abstract structural information. On Mystery Blocksworld - a semantically obfuscated planning domain - we find that QwQ-32B gradually improves its internal representation of actions and concepts during reasoning. The model develops abstract encodings that focus on structure rather than specific action names. Through steering experiments, we establish causal evidence that these adaptations improve problem solving: injecting refined representations from successful traces boosts accuracy, while symbolic representations can replace many obfuscated encodings with minimal performance loss. We find that one of the factors driving reasoning model performance is in-context refinement of token representations, which we dub Fluid Reasoning Representations.

