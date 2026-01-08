---
layout: default
title: Bootstrapping Code Translation with Weighted Multilanguage Exploration
---

# Bootstrapping Code Translation with Weighted Multilanguage Exploration
**arXiv**：[2601.03512v1](https://arxiv.org/abs/2601.03512) · [PDF](https://arxiv.org/pdf/2601.03512.pdf)  
**作者**：Yuhan Wu, Huan Zhang, Wei Cheng, Chen Shen, Jingyue Yang, Wei Hu  

**一句话要点**：提出BootTrans方法，利用测试套件功能不变性解决多语言代码翻译中数据稀缺与优化不平衡问题。

**关键词**：代码翻译, 多语言编程, 自举训练, 测试套件验证, 优化平衡, 强化学习

## 3 点简述
- 核心问题：多语言代码翻译面临并行数据稀缺和语言对间优化不平衡的挑战。
- 方法要点：基于测试套件构建通用验证机制，通过双池架构和语言感知权重动态扩展训练数据。
- 实验或效果：在HumanEval-X和TransCoder-Test基准上显著优于基线模型，验证了自举和加权组件的有效性。

## 摘要（原文）

> Code translation across multiple programming languages is essential yet challenging due to two vital obstacles: scarcity of parallel data paired with executable test oracles, and optimization imbalance when handling diverse language pairs. We propose BootTrans, a bootstrapping method that resolves both obstacles. Its key idea is to leverage the functional invariance and cross-lingual portability of test suites, adapting abundant pivot-language unit tests to serve as universal verification oracles for multilingual RL training. Our method introduces a dual-pool architecture with seed and exploration pools to progressively expand training data via execution-guided experience collection. Furthermore, we design a language-aware weighting mechanism that dynamically prioritizes harder translation directions based on relative performance across sibling languages, mitigating optimization imbalance. Extensive experiments on the HumanEval-X and TransCoder-Test benchmarks demonstrate substantial improvements over baseline LLMs across all translation directions, with ablations validating the effectiveness of both bootstrapping and weighting components.

