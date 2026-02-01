---
layout: default
title: Quantifying Noise in Language Generation
---

# Quantifying Noise in Language Generation
**arXiv**：[2601.21237v1](https://arxiv.org/abs/2601.21237) · [PDF](https://arxiv.org/pdf/2601.21237.pdf)  
**作者**：Aaron Li, Ian Zhang  

**一句话要点**：量化噪声对语言生成的影响，证明单噪声字符串严格减少可生成集合，且与有限噪声等价。

**关键词**：语言生成, 噪声模型, 量化分析, 均匀生成, 非均匀生成, 理论框架

## 3 点简述
- 研究噪声模型中噪声对语言生成的影响，量化每个额外噪声字符串的作用。
- 证明单噪声字符串在均匀和非均匀生成中均严格减少可生成集合，解决了开放问题。
- 展示单噪声字符串生成与任何有限噪声生成等价，与非均匀噪声依赖生成性首次表征。

## 摘要（原文）

> Kleinberg and Mullainathan recently proposed a formal framework for studying the phenomenon of language generation, called language generation in the limit. In this model, an adversary gives an enumeration of example strings from an unknown target language, and the algorithm is tasked with correctly generating unseen strings from the target language within finite time. Refined notions of non-uniform and uniform generation were later introduced by Li, Raman, and Tewari (2025), and a noisy model was introduced by Raman and Raman (2025), which allows the adversary to insert extraneous strings. A natural question in the noisy model is to quantify the effect of noise, by studying the impact of each additional extraneous string. We show two complementary results in this setting. We first show that for both uniform and non-uniform generation, a single noisy string strictly reduces the set of collections that can be generated, thus answering an open question in Raman and Raman (2025). Then, we show for both uniform and non-uniform generation that generation with a single noisy string is equivalent to generation with any finite amount of noise, sharply contrasting with the strict hierarchy for noisy generation in the limit shown by Bai, Panigrahi, and Zhang (2026). Finally, we leverage our previous results to provide the first known characterization for non-uniform noise-dependent generatability.

