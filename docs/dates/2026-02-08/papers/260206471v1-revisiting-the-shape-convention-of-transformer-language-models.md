---
layout: default
title: Revisiting the Shape Convention of Transformer Language Models
---

# Revisiting the Shape Convention of Transformer Language Models
**arXiv**：[2602.06471v1](https://arxiv.org/abs/2602.06471) · [PDF](https://arxiv.org/pdf/2602.06471.pdf)  
**作者**：Feng-Ting Liao, Meng-Hsi Chen, Guan-Ting Yi, Da-shan Shiu  

**一句话要点**：提出沙漏形前馈网络替代传统窄-宽-窄设计，优化Transformer语言模型参数分配。

**关键词**：Transformer架构, 前馈网络设计, 参数效率, 语言模型优化, 沙漏形MLP

## 3 点简述
- 核心问题：传统Transformer前馈网络采用窄-宽-窄MLP形状，参数分配可能非最优。
- 方法要点：用更深但更轻的沙漏形FFN替换传统FFN，通过残差连接提升函数逼近能力。
- 实验或效果：在400M参数内超越传统FFN，1B参数时性能相当，节省参数可增强注意力模块。

## 摘要（原文）

> Dense Transformer language models have largely adhered to one consistent architectural shape: each layer consists of an attention module followed by a feed-forward network (FFN) with a narrow-wide-narrow MLP, allocating most parameters to the MLP at expansion ratios between 2 and 4. Motivated by recent results that residual wide-narrow-wide (hourglass) MLPs offer superior function approximation capabilities, we revisit the long-standing MLP shape convention in Transformer, challenging the necessity of the narrow-wide-narrow design. To study this, we develop a Transformer variant that replaces the conventional FFN with a deeper hourglass-shaped FFN, comprising a stack of hourglass sub-MLPs connected by residual pathways. We posit that a deeper but lighter hourglass FFN can serve as a competitive alternative to the conventional FFN, and that parameters saved by using a lighter hourglass FFN can be more effectively utilized, such as by enlarging model hidden dimensions under fixed budgets. We confirm these through empirical validations across model scales: hourglass FFNs outperform conventional FFNs up to 400M and achieve comparable performance at larger scales to 1B parameters; hourglass FFN variants with reduced FFN and increased attention parameters show consistent improvements over conventional configurations at matched budgets. Together, these findings shed new light on recent work and prompt a rethinking of the narrow-wide-narrow MLP convention and the balance between attention and FFN towards efficient and expressive modern language models.

