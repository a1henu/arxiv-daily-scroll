---
layout: default
title: ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution
---

# ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution
**arXiv**：[2603.02510v1](https://arxiv.org/abs/2603.02510) · [PDF](https://arxiv.org/pdf/2603.02510.pdf)  
**作者**：Liu Yang, Zeyu Nie, Andrew Liu, Felix Zou, Deniz Altinbüken, Amir Yazdanbakhsh, Quanquan C. Liu  

**一句话要点**：提出ParEVO框架以合成针对不规则数据结构的高性能并行算法

**关键词**：并行算法合成, 不规则数据结构, 进化编码代理, 大语言模型微调, 高性能计算

## 3 点简述
- 核心问题：不规则数据结构（如稀疏图）的并行编程因依赖不可预测而困难，现有大语言模型常生成含竞态和死锁的代码。
- 方法要点：通过Parlay-Instruct数据集、微调模型和进化编码代理，结合编译器和性能分析反馈迭代修复代码。
- 实验或效果：在ParEval基准上平均加速106倍，复杂不规则图问题上加速13.6倍，匹配专家基线。

## 摘要（原文）

> The transition from sequential to parallel computing is essential for modern high-performance applications but is hindered by the steep learning curve of concurrent programming. This challenge is magnified for irregular data structures (such as sparse graphs, unbalanced trees, and non-uniform meshes) where static scheduling fails and data dependencies are unpredictable. Current Large Language Models (LLMs) often fail catastrophically on these tasks, generating code plagued by subtle race conditions, deadlocks, and sub-optimal scaling.
>   We bridge this gap with ParEVO, a framework designed to synthesize high-performance parallel algorithms for irregular data. Our contributions include: (1) The Parlay-Instruct Corpus, a curated dataset of 13,820 tasks synthesized via a "Critic-Refine" pipeline that explicitly filters for empirically performant algorithms that effectively utilize Work-Span parallel primitives; (2) specialized DeepSeek, Qwen, and Gemini models fine-tuned to align probabilistic generation with the rigorous semantics of the ParlayLib library; and (3) an Evolutionary Coding Agent (ECA) that improves the "last mile" of correctness by iteratively repairing code using feedback from compilers, dynamic race detectors, and performance profilers.
>   On the ParEval benchmark, ParEVO achieves an average 106x speedup (with a maximum of 1103x) across the suite, and a robust 13.6x speedup specifically on complex irregular graph problems, outperforming state-of-the-art commercial models. Furthermore, our evolutionary approach matches state-of-the-art expert human baselines, achieving up to a 4.1x speedup on specific highly-irregular kernels. Source code and datasets are available at https://github.com/WildAlg/ParEVO.

