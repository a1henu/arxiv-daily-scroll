---
layout: default
title: Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements
---

# Encyclo-K: Evaluating LLMs with Dynamically Composed Knowledge Statements
**arXiv**：[2512.24867v1](https://arxiv.org/abs/2512.24867) · [PDF](https://arxiv.org/pdf/2512.24867.pdf)  
**作者**：Yiming Liang, Yizhi Li, Yantao Du, Ge Zhang, Jiayi Zhou, Yuchen Wu, Yinzhu Piao, Denghui Cao, Tong Sun, Ziniu Li, Li Du, Bo Lei, Jiaheng Liu, Chenghua Lin, Zhaoxiang Zhang, Wenhao Huang, Jiajun Zhang  

**一句话要点**：提出Encyclo-K基准，通过动态组合知识陈述评估大语言模型的多知识综合理解能力。

**关键词**：大语言模型评估, 动态基准构建, 知识陈述组合, 多知识综合理解, 可扩展评估框架

## 3 点简述
- 现有基准易受数据污染、限于单知识评估且依赖专家标注，Encyclo-K以知识陈述为单元构建问题。
- 从权威教材提取知识陈述，测试时随机组合成问题，解决基准局限性并降低标注成本。
- 在50多个大语言模型上实验，显示强区分力，模型性能呈梯度分布，验证动态评估与多陈述理解的挑战性。

## 摘要（原文）

> Benchmarks play a crucial role in tracking the rapid advancement of large language models (LLMs) and identifying their capability boundaries. However, existing benchmarks predominantly curate questions at the question level, suffering from three fundamental limitations: vulnerability to data contamination, restriction to single-knowledge-point assessment, and reliance on costly domain expert annotation. We propose Encyclo-K, a statement-based benchmark that rethinks benchmark construction from the ground up. Our key insight is that knowledge statements, not questions, can serve as the unit of curation, and questions can then be constructed from them. We extract standalone knowledge statements from authoritative textbooks and dynamically compose them into evaluation questions through random sampling at test time. This design directly addresses all three limitations: the combinatorial space is too vast to memorize, and model rankings remain stable across dynamically generated question sets, enabling reliable periodic dataset refresh; each question aggregates 8-10 statements for comprehensive multi-knowledge assessment; annotators only verify formatting compliance without requiring domain expertise, substantially reducing annotation costs. Experiments on over 50 LLMs demonstrate that Encyclo-K poses substantial challenges with strong discriminative power. Even the top-performing OpenAI-GPT-5.1 achieves only 62.07% accuracy, and model performance displays a clear gradient distribution--reasoning models span from 16.04% to 62.07%, while chat models range from 9.71% to 50.40%. These results validate the challenges introduced by dynamic evaluation and multi-statement comprehensive understanding. These findings establish Encyclo-K as a scalable framework for dynamic evaluation of LLMs' comprehensive understanding over multiple fine-grained disciplinary knowledge statements.

