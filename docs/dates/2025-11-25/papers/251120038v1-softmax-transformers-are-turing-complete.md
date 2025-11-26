---
layout: default
title: Softmax Transformers are Turing-Complete
---

# Softmax Transformers are Turing-Complete
**arXiv**：[2511.20038v1](https://arxiv.org/abs/2511.20038) · [PDF](https://arxiv.org/pdf/2511.20038.pdf)  
**作者**：Hongjian Jiang, Michael Hahn, Georg Zetzsche, Anthony Widjaja Lin  

**一句话要点**：证明长度可泛化的软注意力链式思维变换器是图灵完备的

**关键词**：软注意力变换器, 图灵完备性, 链式思维, 长度泛化, 相对位置编码, 算术推理

## 3 点简述
- 核心问题：软注意力链式思维变换器是否图灵完备是开放问题
- 方法要点：通过链式思维C-RASP扩展证明图灵完备性
- 实验或效果：训练变换器验证复杂算术推理语言

## 摘要（原文）

> Hard attention Chain-of-Thought (CoT) transformers are known to be Turing-complete. However, it is an open problem whether softmax attention Chain-of-Thought (CoT) transformers are Turing-complete. In this paper, we prove a stronger result that length-generalizable softmax CoT transformers are Turing-complete. More precisely, our Turing-completeness proof goes via the CoT extension of the Counting RASP (C-RASP), which correspond to softmax CoT transformers that admit length generalization. We prove Turing-completeness for CoT C-RASP with causal masking over a unary alphabet (more generally, for letter-bounded languages). While we show this is not Turing-complete for arbitrary languages, we prove that its extension with relative positional encoding is Turing-complete for arbitrary languages. We empirically validate our theory by training transformers for languages requiring complex (non-linear) arithmetic reasoning.

