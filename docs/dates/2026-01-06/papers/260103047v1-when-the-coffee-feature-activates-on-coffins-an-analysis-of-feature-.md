---
layout: default
title: When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability
---

# When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability
**arXiv**：[2601.03047v1](https://arxiv.org/abs/2601.03047) · [PDF](https://arxiv.org/pdf/2601.03047.pdf)  
**作者**：Raphael Ronge, Markus Maier, Frederick Eberhardt  

**一句话要点**：复现并评估稀疏自编码器在大型语言模型特征提取与引导中的脆弱性

**关键词**：机制可解释性, 稀疏自编码器, 特征提取, 特征引导, AI安全, 大型语言模型

## 3 点简述
- 核心问题：评估Anthropic基于稀疏自编码器的机制可解释性方法在开源模型中的泛化可靠性
- 方法要点：使用Llama 3.1复现特征提取与引导实验，分析层选择、引导幅度和上下文的影响
- 实验或效果：发现特征引导存在显著脆弱性，难以区分主题相似特征，当前方法在安全关键应用中可靠性不足

## 摘要（原文）

> Recent work by Anthropic on Mechanistic interpretability claims to understand and control Large Language Models by extracting human-interpretable features from their neural activation patterns using sparse autoencoders (SAEs). If successful, this approach offers one of the most promising routes for human oversight in AI safety. We conduct an initial stress-test of these claims by replicating their main results with open-source SAEs for Llama 3.1. While we successfully reproduce basic feature extraction and steering capabilities, our investigation suggests that major caution is warranted regarding the generalizability of these claims. We find that feature steering exhibits substantial fragility, with sensitivity to layer selection, steering magnitude, and context. We observe non-standard activation behavior and demonstrate the difficulty to distinguish thematically similar features from one another. While SAE-based interpretability produces compelling demonstrations in selected cases, current methods often fall short of the systematic reliability required for safety-critical applications. This suggests a necessary shift in focus from prioritizing interpretability of internal representations toward reliable prediction and control of model output. Our work contributes to a more nuanced understanding of what mechanistic interpretability has achieved and highlights fundamental challenges for AI safety that remain unresolved.

