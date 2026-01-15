---
layout: default
title: ShortCoder: Knowledge-Augmented Syntax Optimization for Token-Efficient Code Generation
---

# ShortCoder: Knowledge-Augmented Syntax Optimization for Token-Efficient Code Generation
**arXiv**：[2601.09703v1](https://arxiv.org/abs/2601.09703) · [PDF](https://arxiv.org/pdf/2601.09703.pdf)  
**作者**：Sicong Liu, Yanxian Huang, Mingwei Liu, Jiachi Chen, Ensheng Shi, Yuchi Ma, Hongyu Zhang, Yin Zhang, Yanlin Wang  

**一句话要点**：提出ShortCoder框架，通过语法优化提升代码生成的令牌效率

**关键词**：代码生成, 令牌效率, 语法优化, 大语言模型, 微调策略

## 3 点简述
- 核心问题：LLM代码生成时令牌效率低，现有研究忽视生成阶段优化
- 方法要点：基于AST的语法简化规则、混合数据合成管道和微调策略
- 实验或效果：在HumanEval上效率提升18.1%-37.8%，保持语义等价

## 摘要（原文）

> Code generation tasks aim to automate the conversion of user requirements into executable code, significantly reducing manual development efforts and enhancing software productivity. The emergence of large language models (LLMs) has significantly advanced code generation, though their efficiency is still impacted by certain inherent architectural constraints. Each token generation necessitates a complete inference pass, requiring persistent retention of contextual information in memory and escalating resource consumption. While existing research prioritizes inference-phase optimizations such as prompt compression and model quantization, the generation phase remains underexplored. To tackle these challenges, we propose a knowledge-infused framework named ShortCoder, which optimizes code generation efficiency while preserving semantic equivalence and readability. In particular, we introduce: (1) ten syntax-level simplification rules for Python, derived from AST-preserving transformations, achieving 18.1% token reduction without functional compromise; (2) a hybrid data synthesis pipeline integrating rule-based rewriting with LLM-guided refinement, producing ShorterCodeBench, a corpus of validated tuples of original code and simplified code with semantic consistency; (3) a fine-tuning strategy that injects conciseness awareness into the base LLMs. Extensive experimental results demonstrate that ShortCoder consistently outperforms state-of-the-art methods on HumanEval, achieving an improvement of 18.1%-37.8% in generation efficiency over previous methods while ensuring the performance of code generation.

