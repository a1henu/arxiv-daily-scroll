---
layout: default
title: Discovering Interpretable Algorithms by Decompiling Transformers to RASP
---

# Discovering Interpretable Algorithms by Decompiling Transformers to RASP
**arXiv**：[2602.08857v1](https://arxiv.org/abs/2602.08857) · [PDF](https://arxiv.org/pdf/2602.08857.pdf)  
**作者**：Xinting Huang, Aleksandra Bakalova, Satwik Bhattamishra, William Merrill, Michael Hahn  

**一句话要点**：提出从Transformer提取可解释RASP程序的方法，以验证其内部实现简单算法

**关键词**：Transformer可解释性, RASP编程语言, 长度泛化, 因果干预, 算法提取

## 3 点简述
- 核心问题：Transformer是否实现简单可解释程序，以支持长度泛化能力
- 方法要点：将Transformer重参数化为RASP程序，通过因果干预提取最小充分子程序
- 实验或效果：在算法和形式语言任务中，从长度泛化Transformer成功提取简单RASP程序

## 摘要（原文）

> Recent work has shown that the computations of Transformers can be simulated in the RASP family of programming languages. These findings have enabled improved understanding of the expressive capacity and generalization abilities of Transformers. In particular, Transformers have been suggested to length-generalize exactly on problems that have simple RASP programs. However, it remains open whether trained models actually implement simple interpretable programs. In this paper, we present a general method to extract such programs from trained Transformers. The idea is to faithfully re-parameterize a Transformer as a RASP program and then apply causal interventions to discover a small sufficient sub-program. In experiments on small Transformers trained on algorithmic and formal language tasks, we show that our method often recovers simple and interpretable RASP programs from length-generalizing transformers. Our results provide the most direct evidence so far that Transformers internally implement simple RASP programs.

