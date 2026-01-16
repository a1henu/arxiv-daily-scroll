---
layout: default
title: Loop as a Bridge: Can Looped Transformers Truly Link Representation Space and Natural Language Outputs?
---

# Loop as a Bridge: Can Looped Transformers Truly Link Representation Space and Natural Language Outputs?
**arXiv**：[2601.10242v1](https://arxiv.org/abs/2601.10242) · [PDF](https://arxiv.org/pdf/2601.10242.pdf)  
**作者**：Guanxu Chen, Dongrui Liu, Jing Shao  

**一句话要点**：探究循环Transformer能否通过迭代内省连接表示空间与自然语言输出

**关键词**：循环Transformer, 表示空间, 自然语言输出, 内省机制, 计算深度扩展

## 3 点简述
- 核心问题：大语言模型内部知识与显式语言输出间存在差距，循环Transformer能否作为内省机制弥合此差距。
- 方法要点：通过实验分析循环Transformer的迭代特性，评估其作为内省工具在连接表示与输出方面的有效性。
- 实验或效果：增加循环迭代缩小差距，但部分源于表示携带的内部知识退化；当前模型仅在最终循环感知表示，未实现跨循环改进。

## 摘要（原文）

> Large Language Models (LLMs) often exhibit a gap between their internal knowledge and their explicit linguistic outputs. In this report, we empirically investigate whether Looped Transformers (LTs)--architectures that increase computational depth by iterating shared layers--can bridge this gap by utilizing their iterative nature as a form of introspection. Our experiments reveal that while increasing loop iterations narrows the gap, it is partly driven by a degradation of their internal knowledge carried by representations. Moreover, another empirical analysis suggests that current LTs' ability to perceive representations does not improve across loops; it is only present in the final loop. These results suggest that while LTs offer a promising direction for scaling computational depth, they have yet to achieve the introspection required to truly link representation space and natural language.

