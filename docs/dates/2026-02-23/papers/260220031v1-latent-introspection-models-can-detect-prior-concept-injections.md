---
layout: default
title: Latent Introspection: Models Can Detect Prior Concept Injections
---

# Latent Introspection: Models Can Detect Prior Concept Injections
**arXiv**：[2602.20031v1](https://arxiv.org/abs/2602.20031) · [PDF](https://arxiv.org/pdf/2602.20031.pdf)  
**作者**：Theia Pearson-Vogel, Martin Vanek, Raymond Douglas, Jan Kulveit  

**一句话要点**：揭示Qwen 32B模型具备潜在内省能力，可检测先前概念注入并识别具体概念

**关键词**：模型内省, 概念注入检测, 残差流分析, AI安全性, 潜在推理, Qwen模型

## 3 点简述
- 核心问题：模型能否检测到先前上下文中的概念注入，并识别具体注入概念，这涉及潜在推理与安全性。
- 方法要点：使用logit lens分析残差流，发现检测信号，并通过提示模型关于AI内省机制的信息来增强效果。
- 实验或效果：敏感性从0.3%提升至39.2%，假阳性仅增0.6%；互信息从0.62比特升至1.05比特，排除噪声解释。

## 摘要（原文）

> We uncover a latent capacity for introspection in a Qwen 32B model, demonstrating that the model can detect when concepts have been injected into its earlier context and identify which concept was injected. While the model denies injection in sampled outputs, logit lens analysis reveals clear detection signals in the residual stream, which are attenuated in the final layers. Furthermore, prompting the model with accurate information about AI introspection mechanisms can dramatically strengthen this effect: the sensitivity to injection increases massively (0.3% -> 39.2%) with only a 0.6% increase in false positives. Also, mutual information between nine injected and recovered concepts rises from 0.62 bits to 1.05 bits, ruling out generic noise explanations. Our results demonstrate models can have a surprising capacity for introspection and steering awareness that is easy to overlook, with consequences for latent reasoning and safety.

