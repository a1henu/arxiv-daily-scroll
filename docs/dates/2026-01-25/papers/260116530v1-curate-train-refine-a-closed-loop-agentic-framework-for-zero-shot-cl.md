---
layout: default
title: Curate-Train-Refine: A Closed-Loop Agentic Framework for Zero Shot Classification
---

# Curate-Train-Refine: A Closed-Loop Agentic Framework for Zero Shot Classification
**arXiv**：[2601.16530v1](https://arxiv.org/abs/2601.16530) · [PDF](https://arxiv.org/pdf/2601.16530.pdf)  
**作者**：Gaurav Maheshwari, Kevin El Haddad  

**一句话要点**：提出Curate-Train-Refine闭环代理框架，利用LLM动态生成监督训练轻量级文本分类器以解决零样本分类部署成本问题。

**关键词**：零样本分类, 轻量级文本分类器, LLM数据策划, 闭环代理框架, 动态监督生成

## 3 点简述
- 核心问题：LLM和高容量编码器在零样本分类中推理成本高、延迟大，限制实际部署。
- 方法要点：采用迭代代理循环，LLM负责数据策划、分析模型表现并合成针对性示例以改进数据质量。
- 实验或效果：在四个基准测试中，该方法持续优于标准零样本和少样本基线，表明LLM可作为有效数据策划者。

## 摘要（原文）

> Large language models (LLMs) and high-capacity encoders have advanced zero and few-shot classification, but their inference cost and latency limit practical deployment. We propose training lightweight text classifiers using dynamically generated supervision from an LLM. Our method employs an iterative, agentic loop in which the LLM curates training data, analyzes model successes and failures, and synthesizes targeted examples to address observed errors. This closed-loop generation and evaluation process progressively improves data quality and adapts it to the downstream classifier and task. Across four widely used benchmarks, our approach consistently outperforms standard zero and few-shot baselines. These results indicate that LLMs can serve effectively as data curators, enabling accurate and efficient classification without the operational cost of large-model deployment.

