---
layout: default
title: C-ing Clearly: Enhanced Binary Code Explanations using C code
---

# C-ing Clearly: Enhanced Binary Code Explanations using C code
**arXiv**：[2512.14500v1](https://arxiv.org/abs/2512.14500) · [PDF](https://arxiv.org/pdf/2512.14500.pdf)  
**作者**：Teodor Poncu, Ioana Pintilie, Marius Dragoi, Dragos Tantaru, Florin Brad  

**一句话要点**：提出C-ing Clearly方法，利用C代码增强LLM对汇编的理解，提升二进制代码分析性能。

**关键词**：二进制代码分析, 大语言模型微调, 汇编理解增强, 合成数据生成, 漏洞检测

## 3 点简述
- 核心问题：LLM在高级语言任务中表现优异，但在汇编等低级语言任务中理解有限。
- 方法要点：通过合成数据生成方法，利用对应C代码增强LLM对汇编的理解，并进行微调。
- 实验或效果：在二进制代码摘要和漏洞检测任务中，不同LLM家族和模型大小均显示性能提升。

## 摘要（原文）

> Large Language Models (LLMs) typically excel at coding tasks involving high-level programming languages, as opposed to lower-level programming languages, such as assembly. We propose a synthetic data generation method named C-ing Clearly, which leverages the corresponding C code to enhance an LLM's understanding of assembly. By fine-tuning on data generated through our method, we demonstrate improved LLM performance for binary code summarization and vulnerability detection. Our approach demonstrates consistent gains across different LLM families and model sizes.

