---
layout: default
title: Language-Guided Transformer Tokenizer for Human Motion Generation
---

# Language-Guided Transformer Tokenizer for Human Motion Generation
**arXiv**：[2602.08337v1](https://arxiv.org/abs/2602.08337) · [PDF](https://arxiv.org/pdf/2602.08337.pdf)  
**作者**：Sheng Yan, Yong Wang, Xin Du, Junsong Yuan, Mengyuan Liu  

**一句话要点**：提出语言引导的Transformer分词器，以解决运动生成中高重建质量与低生成复杂度的平衡问题。

**关键词**：运动生成, 语言引导, Transformer分词器, 离散分词, 语义对齐, 生成模型简化

## 3 点简述
- 核心问题：运动离散分词中，增加分词数量提升重建质量但增加生成模型学习难度。
- 方法要点：利用语言在分词阶段对齐运动，生成紧凑高层语义表示，并设计语言丢弃方案支持无语言生成。
- 实验或效果：在HumanML3D和Motion-X基准上，Top-1和FID分数优于现有方法，验证了语义表示的高效性。

## 摘要（原文）

> In this paper, we focus on motion discrete tokenization, which converts raw motion into compact discrete tokens--a process proven crucial for efficient motion generation. In this paradigm, increasing the number of tokens is a common approach to improving motion reconstruction quality, but more tokens make it more difficult for generative models to learn. To maintain high reconstruction quality while reducing generation complexity, we propose leveraging language to achieve efficient motion tokenization, which we term Language-Guided Tokenization (LG-Tok). LG-Tok aligns natural language with motion at the tokenization stage, yielding compact, high-level semantic representations. This approach not only strengthens both tokenization and detokenization but also simplifies the learning of generative models. Furthermore, existing tokenizers predominantly adopt convolutional architectures, whose local receptive fields struggle to support global language guidance. To this end, we propose a Transformer-based Tokenizer that leverages attention mechanisms to enable effective alignment between language and motion. Additionally, we design a language-drop scheme, in which language conditions are randomly removed during training, enabling the detokenizer to support language-free guidance during generation. On the HumanML3D and Motion-X generation benchmarks, LG-Tok achieves Top-1 scores of 0.542 and 0.582, outperforming state-of-the-art methods (MARDM: 0.500 and 0.528), and with FID scores of 0.057 and 0.088, respectively, versus 0.114 and 0.147. LG-Tok-mini uses only half the tokens while maintaining competitive performance (Top-1: 0.521/0.588, FID: 0.085/0.071), validating the efficiency of our semantic representations.

