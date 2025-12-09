---
layout: default
title: AutoICE: Automatically Synthesizing Verifiable C Code via LLM-driven Evolution
---

# AutoICE: Automatically Synthesizing Verifiable C Code via LLM-driven Evolution
**arXiv**：[2512.07501v1](https://arxiv.org/abs/2512.07501) · [PDF](https://arxiv.org/pdf/2512.07501.pdf)  
**作者**：Weilin Luo, Xueyi Liang, Haotian Deng, Yanan Liu, Hai Wan  

**一句话要点**：提出AutoICE，通过LLM驱动的进化搜索合成可验证C代码，以解决自动形式化中的错误传播问题。

**关键词**：代码合成, 形式化验证, 大语言模型, 进化算法, C语言编程

## 3 点简述
- 核心问题：现有方法因领域语料稀缺和隐式知识形式化困难，导致语法和语义错误频发。
- 方法要点：采用多样个体初始化和协作交叉，结合自反思变异，以进化搜索减少单代理迭代的错误传播。
- 实验或效果：在验证成功率上达到90.36%，超越现有最佳方法，并在开发者友好数据集上显著提升至88.33%。

## 摘要（原文）

> Automatically synthesizing verifiable code from natural language requirements ensures software correctness and reliability while significantly lowering the barrier to adopting the techniques of formal methods. With the rise of large language models (LLMs), long-standing efforts at autoformalization have gained new momentum. However, existing approaches suffer from severe syntactic and semantic errors due to the scarcity of domain-specific pre-training corpora and often fail to formalize implicit knowledge effectively. In this paper, we propose AutoICE, an LLM-driven evolutionary search for synthesizing verifiable C code. It introduces the diverse individual initialization and the collaborative crossover to enable diverse iterative updates, thereby mitigating error propagation inherent in single-agent iterations. Besides, it employs the self-reflective mutation to facilitate the discovery of implicit knowledge. Evaluation results demonstrate the effectiveness of AutoICE: it successfully verifies $90.36$\% of code, outperforming the state-of-the-art (SOTA) approach. Besides, on a developer-friendly dataset variant, AutoICE achieves a $88.33$\% verification success rate, significantly surpassing the $65$\% success rate of the SOTA approach.

