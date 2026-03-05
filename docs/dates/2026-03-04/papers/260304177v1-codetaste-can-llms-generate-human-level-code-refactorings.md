---
layout: default
title: CodeTaste: Can LLMs Generate Human-Level Code Refactorings?
---

# CodeTaste: Can LLMs Generate Human-Level Code Refactorings?
**arXiv**：[2603.04177v1](https://arxiv.org/abs/2603.04177) · [PDF](https://arxiv.org/pdf/2603.04177.pdf)  
**作者**：Alex Thillen, Niels Mündler, Veselin Raychev, Martin Vechev  

**一句话要点**：提出CodeTaste基准以评估LLM代理在真实代码库中执行和发现人类重构决策的能力

**关键词**：代码重构, 大型语言模型, 基准评估, 静态分析, 程序转换

## 3 点简述
- 核心问题：LLM生成的代码常积累复杂性，需评估其能否可靠执行重构并匹配人类选择
- 方法要点：从开源仓库挖掘重构任务，结合测试套件和静态检查进行评分
- 实验或效果：前沿模型在详细指定时表现好，但发现人类选择时存在差距，分解策略可提升对齐

## 摘要（原文）

> Large language model (LLM) coding agents can generate working code, but their solutions often accumulate complexity, duplication, and architectural debt. Human developers address such issues through refactoring: behavior-preserving program transformations that improve structure and maintainability. In this paper, we investigate if LLM agents (i) can execute refactorings reliably and (ii) identify the refactorings that human developers actually chose in real codebases. We present CodeTaste, a benchmark of refactoring tasks mined from large-scale multi-file changes in open-source repositories. To score solutions, we combine repository test suites with custom static checks that verify removal of undesired patterns and introduction of desired patterns using dataflow reasoning.
>   Our experimental results indicate a clear gap across frontier models: agents perform well when refactorings are specified in detail, but often fail to discover the human refactoring choices when only presented with a focus area for improvement. A propose-then-implement decomposition improves alignment, and selecting the best-aligned proposal before implementation can yield further gains. CodeTaste provides an evaluation target and a potential preference signal for aligning coding agents with human refactoring decisions in realistic codebases.

