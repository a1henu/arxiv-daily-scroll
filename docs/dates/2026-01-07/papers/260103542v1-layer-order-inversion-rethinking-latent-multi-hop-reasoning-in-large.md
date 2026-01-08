---
layout: default
title: Layer-Order Inversion: Rethinking Latent Multi-Hop Reasoning in Large Language Models
---

# Layer-Order Inversion: Rethinking Latent Multi-Hop Reasoning in Large Language Models
**arXiv**：[2601.03542v1](https://arxiv.org/abs/2601.03542) · [PDF](https://arxiv.org/pdf/2601.03542.pdf)  
**作者**：Xukai Liu, Ye Liu, Jipeng Zhang, Yanghai Zhang, Kai Zhang, Qi Liu  

**一句话要点**：提出层序反转现象与概率召回-提取框架，以解释大语言模型中的多跳推理机制。

**关键词**：大语言模型, 多跳推理, 层序反转, 概率召回-提取, 机制解释, 系统分析

## 3 点简述
- 核心问题：大语言模型内部如何组合多跳事实，挑战跳对齐电路假设的普适性。
- 方法要点：通过系统分析揭示层序反转现象，提出概率召回-提取框架建模推理过程。
- 实验或效果：实证验证框架，重新解释层解码证据，解释思维链增益，诊断多跳失败。

## 摘要（原文）

> Large language models (LLMs) perform well on multi-hop reasoning, yet how they internally compose multiple facts remains unclear. Recent work proposes \emph{hop-aligned circuit hypothesis}, suggesting that bridge entities are computed sequentially across layers before later-hop answers. Through systematic analyses on real-world multi-hop queries, we show that this hop-aligned assumption does not generalize: later-hop answer entities can become decodable earlier than bridge entities, a phenomenon we call \emph{layer-order inversion}, which strengthens with total hops. To explain this behavior, we propose a \emph{probabilistic recall-and-extract} framework that models multi-hop reasoning as broad probabilistic recall in shallow MLP layers followed by selective extraction in deeper attention layers. This framework is empirically validated through systematic probing analyses, reinterpreting prior layer-wise decoding evidence, explaining chain-of-thought gains, and providing a mechanistic diagnosis of multi-hop failures despite correct single-hop knowledge. Code is available at https://github.com/laquabe/Layer-Order-Inversion.

