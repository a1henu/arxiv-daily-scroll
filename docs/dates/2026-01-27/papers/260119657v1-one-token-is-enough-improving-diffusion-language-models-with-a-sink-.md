---
layout: default
title: One Token Is Enough: Improving Diffusion Language Models with a Sink Token
---

# One Token Is Enough: Improving Diffusion Language Models with a Sink Token
**arXiv**：[2601.19657v1](https://arxiv.org/abs/2601.19657) · [PDF](https://arxiv.org/pdf/2601.19657.pdf)  
**作者**：Zihou Zhang, Zheyong Xie, Li Zhong, Haifeng Liu, Shaosheng Cao  

**一句话要点**：提出额外汇令牌以稳定扩散语言模型中的移动汇现象，提升推理鲁棒性。

**关键词**：扩散语言模型, 注意力机制, 移动汇现象, 推理鲁棒性, 结构汇令牌

## 3 点简述
- 核心问题：扩散语言模型存在移动汇现象，导致注意力汇位置不稳定，影响推理鲁棒性。
- 方法要点：引入一个仅关注自身的额外汇令牌，通过修改注意力掩码实现，作为结构汇稳定注意力。
- 实验或效果：实验表明单令牌能稳定注意力汇，显著提升模型性能，其有效性独立于位置且语义内容可忽略。

## 摘要（原文）

> Diffusion Language Models (DLMs) have emerged as a compelling alternative to autoregressive approaches, enabling parallel text generation with competitive performance. Despite these advantages, there is a critical instability in DLMs: the moving sink phenomenon. Our analysis indicates that sink tokens exhibit low-norm representations in the Transformer's value space, and that the moving sink phenomenon serves as a protective mechanism in DLMs to prevent excessive information mixing. However, their unpredictable positions across diffusion steps undermine inference robustness. To resolve this, we propose a simple but effective extra sink token implemented via a modified attention mask. Specifically, we introduce a special token constrained to attend solely to itself, while remaining globally visible to all other tokens. Experimental results demonstrate that introducing a single extra token stabilizes attention sinks, substantially improving model performance. Crucially, further analysis confirms that the effectiveness of this token is independent of its position and characterized by negligible semantic content, validating its role as a robust and dedicated structural sink.

