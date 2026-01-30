---
layout: default
title: From Logits to Latents: Contrastive Representation Shaping for LLM Unlearning
---

# From Logits to Latents: Contrastive Representation Shaping for LLM Unlearning
**arXiv**：[2601.22028v1](https://arxiv.org/abs/2601.22028) · [PDF](https://arxiv.org/pdf/2601.22028.pdf)  
**作者**：Haoran Tang, Rajiv Khanna  

**一句话要点**：提出CLReg对比表示正则化器，以减少LLM遗忘中遗忘与保留特征的干扰。

**关键词**：大语言模型遗忘, 表示学习, 对比学习, 特征解耦, 正则化方法, 隐私保护

## 3 点简述
- 核心问题：现有LLM遗忘方法可能仅抑制遗忘内容生成，但遗忘概念仍存在于表示中并与保留知识纠缠。
- 方法要点：引入CLReg，通过对比学习识别遗忘特征并将其推离保留特征，最小化保留特征偏移。
- 实验或效果：在多种遗忘基准和不同规模LLM上，CLReg减少表示纠缠，提升主流遗忘方法效果，无额外隐私风险。

## 摘要（原文）

> Most LLM unlearning methods aim to approximate retrain-from-scratch behaviors with minimal distribution shift, often via alignment-style objectives defined in the prediction space. While effective at reducing forgotten content generation, such approaches may act as suppression: forgotten concepts can persist in representations and remain entangled with retained knowledge. We introduce CLReg, a contrastive representation regularizer that identifies forget features while pushing them away from retain features, explicitly reducing forget-retain interference with minimal shifts on retain features. We provide first theoretical insights that relate representation shaping to entanglement reduction. Across unlearning benchmarks and LLMs of different sizes, CLReg decreases forget-retain representation entanglement that facilitates mainstream unlearning methods without positing extra privacy risks, inspiring future work that reshapes the representation space to remove forget concepts.

