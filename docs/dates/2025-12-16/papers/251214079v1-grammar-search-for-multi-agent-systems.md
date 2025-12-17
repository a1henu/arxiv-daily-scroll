---
layout: default
title: Grammar Search for Multi-Agent Systems
---

# Grammar Search for Multi-Agent Systems
**arXiv**：[2512.14079v1](https://arxiv.org/abs/2512.14079) · [PDF](https://arxiv.org/pdf/2512.14079.pdf)  
**作者**：Mayank Singh, Vikas Yadav, Shiva Krishna Reddy Malay, Shravan Nayak, Sai Rajeswar, Sathwik Tejaswi Madhusudhan, Eduardo Blanco  

**一句话要点**：提出基于固定组件的结构化搜索框架，以提升多智能体系统在数学和问答领域的性能与效率。

**关键词**：多智能体系统, 结构化搜索, 组件化框架, 数学推理, 问答系统, 成本效率

## 3 点简述
- 核心问题：多智能体系统自动搜索中，现有方法依赖LLM自由形式搜索，缺乏结构化和效率。
- 方法要点：使用固定、可组合的简单组件进行结构化搜索，替代LLM的生成灵活性。
- 实验或效果：在五个基准测试中的四个上优于先前方法，且搜索成本更低，生成系统更模块化和可解释。

## 摘要（原文）

> Automatic search for Multi-Agent Systems has recently emerged as a key focus in agentic AI research. Several prior approaches have relied on LLM-based free-form search over the code space. In this work, we propose a more structured framework that explores the same space through a fixed set of simple, composable components. We show that, despite lacking the generative flexibility of LLMs during the candidate generation stage, our method outperforms prior approaches on four out of five benchmarks across two domains: mathematics and question answering. Furthermore, our method offers additional advantages, including a more cost-efficient search process and the generation of modular, interpretable multi-agent systems with simpler logic.

