---
layout: default
title: LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI
---

# LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI
**arXiv**：[2601.21511v1](https://arxiv.org/abs/2601.21511) · [PDF](https://arxiv.org/pdf/2601.21511.pdf)  
**作者**：Niki van Stein, Anna V. Kononova, Lars Kotthoff, Thomas Bäck  

**一句话要点**：提出LLaMEA-SAGE，利用可解释AI的结构反馈指导自动化算法设计，提升搜索效率与性能。

**关键词**：自动化算法设计, 可解释AI, 大语言模型, 代码结构分析, 进化算法, 性能优化

## 3 点简述
- 核心问题：自动化算法设计仅依赖适应度反馈，忽略生成代码的结构信息，导致搜索效率受限。
- 方法要点：从抽象语法树提取图论和复杂度特征，通过可解释AI识别关键特征并转化为自然语言指令，指导LLM生成代码。
- 实验或效果：在GECCO-MA-BBOB基准测试中，LLaMEA-SAGE优于现有自动化算法设计方法，实现更快收敛和更高性能。

## 摘要（原文）

> Large language models have enabled automated algorithm design (AAD) by generating optimization algorithms directly from natural-language prompts. While evolutionary frameworks such as LLaMEA demonstrate strong exploratory capabilities across the algorithm design space, their search dynamics are entirely driven by fitness feedback, leaving substantial information about the generated code unused. We propose a mechanism for guiding AAD using feedback constructed from graph-theoretic and complexity features extracted from the abstract syntax trees of the generated algorithms, based on a surrogate model learned over an archive of evaluated solutions. Using explainable AI techniques, we identify features that substantially affect performance and translate them into natural-language mutation instructions that steer subsequent LLM-based code generation without restricting expressivity.
>   We propose LLaMEA-SAGE, which integrates this feature-driven guidance into LLaMEA, and evaluate it across several benchmarks. We show that the proposed structured guidance achieves the same performance faster than vanilla LLaMEA in a small controlled experiment. In a larger-scale experiment using the MA-BBOB suite from the GECCO-MA-BBOB competition, our guided approach achieves superior performance compared to state-of-the-art AAD methods. These results demonstrate that signals derived from code can effectively bias LLM-driven algorithm evolution, bridging the gap between code structure and human-understandable performance feedback in automated algorithm design.

