---
layout: default
title: SC-Arena: A Natural Language Benchmark for Single-Cell Reasoning with Knowledge-Augmented Evaluation
---

# SC-Arena: A Natural Language Benchmark for Single-Cell Reasoning with Knowledge-Augmented Evaluation
**arXiv**：[2602.23199v1](https://arxiv.org/abs/2602.23199) · [PDF](https://arxiv.org/pdf/2602.23199.pdf)  
**作者**：Jiahao Zhao, Feng Jiang, Shaowei Qin, Zhonghui Zhang, Junhao Liu, Guibing Guo, Hamid Alinejad-Rokny, Min Yang  

**一句话要点**：提出SC-Arena评估框架以解决单细胞生物学中LLM评估的碎片化与缺乏生物可解释性问题

**关键词**：单细胞生物学, 大语言模型评估, 知识增强评估, 虚拟细胞抽象, 自然语言任务

## 3 点简述
- 现有单细胞生物学LLM评估基准任务分散、格式不切实际且指标缺乏生物可解释性
- SC-Arena通过虚拟细胞抽象统一评估目标，定义五个自然语言任务并引入知识增强评估
- 实验表明该框架能确保生物正确性、提供可解释依据并克服传统指标的脆弱性

## 摘要（原文）

> Large language models (LLMs) are increasingly applied in scientific research, offering new capabilities for knowledge discovery and reasoning. In single-cell biology, however, evaluation practices for both general and specialized LLMs remain inadequate: existing benchmarks are fragmented across tasks, adopt formats such as multiple-choice classification that diverge from real-world usage, and rely on metrics lacking interpretability and biological grounding. We present SC-ARENA, a natural language evaluation framework tailored to single-cell foundation models. SC-ARENA formalizes a virtual cell abstraction that unifies evaluation targets by representing both intrinsic attributes and gene-level interactions. Within this paradigm, we define five natural language tasks (cell type annotation, captioning, generation, perturbation prediction, and scientific QA) that probe core reasoning capabilities in cellular biology. To overcome the limitations of brittle string-matching metrics, we introduce knowledge-augmented evaluation, which incorporates external ontologies, marker databases, and scientific literature to support biologically faithful and interpretable judgments. Experiments and analysis across both general-purpose and domain-specialized LLMs demonstrate that (i) under the Virtual Cell unified evaluation paradigm, current models achieve uneven performance on biologically complex tasks, particularly those demanding mechanistic or causal understanding; and (ii) our knowledge-augmented evaluation framework ensures biological correctness, provides interpretable, evidence-grounded rationales, and achieves high discriminative capacity, overcoming the brittleness and opacity of conventional metrics. SC-Arena thus provides a unified and interpretable framework for assessing LLMs in single-cell biology, pointing toward the development of biology-aligned, generalizable foundation models.

