---
layout: default
title: SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding
---

# SAKED: Mitigating Hallucination in Large Vision-Language Models via Stability-Aware Knowledge Enhanced Decoding
**arXiv**：[2602.09825v1](https://arxiv.org/abs/2602.09825) · [PDF](https://arxiv.org/pdf/2602.09825.pdf)  
**作者**：Zhaoxu Li, Chenqi Kong, Peijun Bao, Song Xia, Yi Tu, Yi Yu, Xinghao Jiang, Xudong Jiang  

**一句话要点**：提出SAKED方法，通过稳定性感知知识增强解码缓解大型视觉语言模型中的幻觉问题。

**关键词**：大型视觉语言模型, 幻觉缓解, 稳定性感知解码, 知识稳定性评分, 训练免费方法

## 3 点简述
- 核心问题：大型视觉语言模型在不确定时易产生幻觉，影响安全性和可靠性。
- 方法要点：基于层间知识稳定性评分，动态利用最可靠内部知识进行解码。
- 实验或效果：在多种模型、任务和基准测试中实现最先进的幻觉缓解性能。

## 摘要（原文）

> Hallucinations in Large Vision-Language Models (LVLMs) pose significant security and reliability risks in real-world applications. Inspired by the observation that humans are more error-prone when uncertain or hesitant, we investigate how instability in a model 's internal knowledge contributes to LVLM hallucinations. We conduct extensive empirical analyses from three perspectives, namely attention heads, model layers, and decoding tokens, and identify three key hallucination patterns: (i) visual activation drift across attention heads, (ii) pronounced knowledge fluctuations across layers, and (iii) visual focus distraction between neighboring output tokens. Building on these findings, we propose Stability-Aware Knowledge-Enhanced Decoding (SAKED), which introduces a layer-wise Knowledge Stability Score (KSS) to quantify knowledge stability throughout the model. By contrasting the most stability-aware and stability-agnostic layers, SAKED suppresses decoding noise and dynamically leverages the most reliable internal knowledge for faithful token generation. Moreover, SAKED is training-free and can be seamlessly integrated into different architectures. Extensive experiments demonstrate that SAKED achieves state-of-the-art performance for hallucination mitigation on various models, tasks, and benchmarks.

