---
layout: default
title: Bootstrapping Fuzzers for Compilers of Low-Resource Language Dialects Using Language Models
---

# Bootstrapping Fuzzers for Compilers of Low-Resource Language Dialects Using Language Models
**arXiv**：[2512.05887v1](https://arxiv.org/abs/2512.05887) · [PDF](https://arxiv.org/pdf/2512.05887.pdf)  
**作者**：Sairam Vaidya, Marcel Böhme, Loris D'Antoni  

**一句话要点**：提出Germinator工具，结合语言模型与语法引导，为低资源语言方言编译器实现方言无关且有效的模糊测试种子生成。

**关键词**：编译器模糊测试, 语言模型应用, 方言无关测试, 语法引导生成, 低资源语言方言, MLIR框架

## 3 点简述
- 核心问题：可扩展编译器框架（如MLIR）中，方言的灵活开发导致测试基础设施维护困难，现有方法难以同时实现方言无关和方言有效的自动化测试生成。
- 方法要点：自动从方言规范提取语法，结合预训练大语言模型生成多样种子输入，无需手动数据，用于引导覆盖导向的模糊测试器。
- 实验或效果：在6个MLIR项目的91个方言上评估，Germinator提升行覆盖率10-120%，发现88个未知错误（40个确认），包括23个在无先前自动化测试生成器的方言中。

## 摘要（原文）

> Modern extensible compiler frameworks-such as MLIR-enable rapid creation of domain-specific language dialects. This flexibility, however, makes correctness harder to ensure as the same extensibility that accelerates development also complicates maintaining the testing infrastructure. Extensible languages require automated test generation that is both dialect-agnostic (works across dialects without manual adaptation) and dialect-effective (targets dialect-specific features to find bugs). Existing approaches typically sacrifice one of these goals by either requiring manually constructed seed corpora for each dialect, or by failing to be effective. We present a dialect-agnostic and dialect-effective grammar-based and coverage-guided fuzzing approach for extensible compilers that combines two key insights from existing work: (i) the grammars of dialects, which already encode the structural and type constraints, can often be extracted automatically from the dialect specification; and (ii) these grammars can be used in combination with pre-trained large language models to automatically generate representative and diverse seed inputs from the full dialect space without requiring any manual input or training data. These seeds can then be used to bootstrap coverage-guided fuzzers. We built this approach into a tool, Germinator. When evaluated on six MLIR projects spanning 91 dialects, Germinator generated seeds improve line coverage by 10-120% over grammar-based baselines. We compare against grammar-based baselines because they are the only class of existing automatic seed generators that can be applied uniformly across MLIR's heterogeneous dialect ecosystem. Germinator discovers 88 previously unknown bugs (40 confirmed), including 23 in dialects with no prior automated test generators, demonstrating effective and controllable testing of low-resource dialects at scale.

