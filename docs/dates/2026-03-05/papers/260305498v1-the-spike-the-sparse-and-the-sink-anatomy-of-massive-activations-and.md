---
layout: default
title: The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks
---

# The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks
**arXiv**：[2603.05498v1](https://arxiv.org/abs/2603.05498) · [PDF](https://arxiv.org/pdf/2603.05498.pdf)  
**作者**：Shangwen Sun, Alfredo Canziani, Yann LeCun, Jiachen Zhu  

**一句话要点**：揭示Transformer中大规模激活与注意力汇的解剖关系，指出预归一化配置是关键耦合因素。

**关键词**：Transformer语言模型, 大规模激活, 注意力汇, 预归一化, 隐式参数, 注意力调制

## 3 点简述
- 核心问题：Transformer语言模型中大规模激活与注意力汇的共现现象及其功能角色和因果关系不明。
- 方法要点：通过系统实验分析，发现大规模激活作为全局隐式参数，注意力汇作为局部调制器。
- 实验或效果：识别预归一化配置为共现关键，消融后两者解耦，证明是架构设计产物。

## 摘要（原文）

> We study two recurring phenomena in Transformer language models: massive activations, in which a small number of tokens exhibit extreme outliers in a few channels, and attention sinks, in which certain tokens attract disproportionate attention mass regardless of semantic relevance. Prior work observes that these phenomena frequently co-occur and often involve the same tokens, but their functional roles and causal relationship remain unclear. Through systematic experiments, we show that the co-occurrence is largely an architectural artifact of modern Transformer design, and that the two phenomena serve related but distinct functions. Massive activations operate globally: they induce near-constant hidden representations that persist across layers, effectively functioning as implicit parameters of the model. Attention sinks operate locally: they modulate attention outputs across heads and bias individual heads toward short-range dependencies. We identify the pre-norm configuration as the key choice that enables the co-occurrence, and show that ablating it causes the two phenomena to decouple.

