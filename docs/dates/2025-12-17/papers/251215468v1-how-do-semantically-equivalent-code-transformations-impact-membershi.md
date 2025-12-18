---
layout: default
title: How Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?
---

# How Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?
**arXiv**：[2512.15468v1](https://arxiv.org/abs/2512.15468) · [PDF](https://arxiv.org/pdf/2512.15468.pdf)  
**作者**：Hua Yang, Alejandro Velasco, Thanh Le-Cong, Md Nazmul Haque, Bowen Xu, Denys Poshyvanyk  

**一句话要点**：研究语义等价代码变换对代码大语言模型成员推断检测的影响

**关键词**：成员推断, 代码变换, 大语言模型, 知识产权合规, 语义等价

## 3 点简述
- 核心问题：语义等价代码变换可能规避成员推断检测，威胁代码知识产权合规。
- 方法要点：系统评估多种变换规则对成员推断准确性的影响，包括变量重命名等。
- 实验或效果：变量重命名降低检测成功率10.19%，但组合变换无额外效果，暴露检测漏洞。

## 摘要（原文）

> The success of large language models for code relies on vast amounts of code data, including public open-source repositories, such as GitHub, and private, confidential code from companies. This raises concerns about intellectual property compliance and the potential unauthorized use of license-restricted code. While membership inference (MI) techniques have been proposed to detect such unauthorized usage, their effectiveness can be undermined by semantically equivalent code transformation techniques, which modify code syntax while preserving semantic.
>   In this work, we systematically investigate whether semantically equivalent code transformation rules might be leveraged to evade MI detection. The results reveal that model accuracy drops by only 1.5% in the worst case for each rule, demonstrating that transformed datasets can effectively serve as substitutes for fine-tuning. Additionally, we find that one of the rules (RenameVariable) reduces MI success by 10.19%, highlighting its potential to obscure the presence of restricted code. To validate these findings, we conduct a causal analysis confirming that variable renaming has the strongest causal effect in disrupting MI detection. Notably, we find that combining multiple transformations does not further reduce MI effectiveness. Our results expose a critical loophole in license compliance enforcement for training large language models for code, showing that MI detection can be substantially weakened by transformation-based obfuscation techniques.

