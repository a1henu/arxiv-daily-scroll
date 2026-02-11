---
layout: default
title: A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models
---

# A Unified Assessment of the Poverty of the Stimulus Argument for Neural Language Models
**arXiv**：[2602.09992v1](https://arxiv.org/abs/2602.09992) · [PDF](https://arxiv.org/pdf/2602.09992.pdf)  
**作者**：Xiulin Yang, Arianna Bisazza, Nathan Schneider, Ethan Gotlieb Wilcox  

**一句话要点**：提出POSHBench评估套件，测试神经语言模型在刺激贫乏论下的语法泛化能力

**关键词**：刺激贫乏论, 神经语言模型, 语法泛化, POSHBench, 归纳偏置, 数据效率

## 3 点简述
- 核心问题：探讨神经语言模型能否在有限输入下实现类似儿童的语法泛化，挑战刺激贫乏论关于先天语法必要性的主张
- 方法要点：基于Transformer模型，在1000万至5000万单词的发展合理文本上训练，并引入三种认知启发的归纳偏置
- 实验或效果：模型在无直接正面证据下显示泛化迹象，但数据效率低于儿童，且归纳偏置未显著提升POSHBench性能

## 摘要（原文）

> How can children acquire native-level syntax from limited input? According to the Poverty of the Stimulus Hypothesis (PoSH), the linguistic input children receive is insufficient to explain certain generalizations that are robustly learned; innate linguistic constraints, many have argued, are thus necessary to explain language learning. Neural language models, which lack such language-specific constraints in their design, offer a computational test of this longstanding (but controversial) claim. We introduce \poshbench, a training-and-evaluation suite targeting question formation, islands to movement, and other English phenomena at the center of the PoSH arguments. Training Transformer models on 10--50M words of developmentally plausible text, we find indications of generalization on all phenomena even without direct positive evidence -- yet neural models remain less data-efficient and their generalizations are weaker than those of children. We further enhance our models with three recently proposed cognitively motivated inductive biases. We find these biases improve general syntactic competence but not \poshbench performance. Our findings challenge the claim that innate syntax is the only possible route to generalization, while suggesting that human-like data efficiency requires inductive biases beyond those tested here.

