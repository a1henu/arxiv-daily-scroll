---
layout: default
title: Toward Understanding Unlearning Difficulty: A Mechanistic Perspective and Circuit-Guided Difficulty Metric
---

# Toward Understanding Unlearning Difficulty: A Mechanistic Perspective and Circuit-Guided Difficulty Metric
**arXiv**：[2601.09624v1](https://arxiv.org/abs/2601.09624) · [PDF](https://arxiv.org/pdf/2601.09624.pdf)  
**作者**：Jiali Cheng, Ziheng Chen, Chirag Agarwal, Hadi Amiri  

**一句话要点**：提出电路引导的遗忘难度度量以分析语言模型遗忘的机制差异

**关键词**：机器遗忘, 模型电路, 难度度量, 机制分析, 语言模型, 可解释性

## 3 点简述
- 核心问题：遗忘成功性在样本间差异显著，反映模型内部机制对记忆信息的编码与保护
- 方法要点：基于模型电路提出预遗忘难度度量CUD，利用电路级信号评估样本遗忘难度
- 实验或效果：CUD能可靠区分易难样本，揭示易样本依赖短浅电路、难样本依赖深长电路的机制特征

## 摘要（原文）

> Machine unlearning is becoming essential for building trustworthy and compliant language models. Yet unlearning success varies considerably across individual samples: some are reliably erased, while others persist despite the same procedure. We argue that this disparity is not only a data-side phenomenon, but also reflects model-internal mechanisms that encode and protect memorized information. We study this problem from a mechanistic perspective based on model circuits--structured interaction pathways that govern how predictions are formed. We propose Circuit-guided Unlearning Difficulty (CUD), a {\em pre-unlearning} metric that assigns each sample a continuous difficulty score using circuit-level signals. Extensive experiments demonstrate that CUD reliably separates intrinsically easy and hard samples, and remains stable across unlearning methods. We identify key circuit-level patterns that reveal a mechanistic signature of difficulty: easy-to-unlearn samples are associated with shorter, shallower interactions concentrated in earlier-to-intermediate parts of the original model, whereas hard samples rely on longer and deeper pathways closer to late-stage computation. Compared to existing qualitative studies, CUD takes a first step toward a principled, fine-grained, and interpretable analysis of unlearning difficulty; and motivates the development of unlearning methods grounded in model mechanisms.

