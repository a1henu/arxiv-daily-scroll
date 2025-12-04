---
layout: default
title: AlignCheck: a Semantic Open-Domain Metric for Factual Consistency Assessment
---

# AlignCheck: a Semantic Open-Domain Metric for Factual Consistency Assessment
**arXiv**：[2512.03634v1](https://arxiv.org/abs/2512.03634) · [PDF](https://arxiv.org/pdf/2512.03634.pdf)  
**作者**：Ahmad Aghaebrahimian  

**一句话要点**：提出AlignCheck框架以评估开放领域文本的事实一致性，增强可解释性。

**关键词**：事实一致性评估, 开放领域文本, 可解释框架, 原子事实分解, 加权度量, 临床应用

## 3 点简述
- 核心问题：大语言模型易产生幻觉，现有评估指标缺乏事实一致性和可解释性。
- 方法要点：将文本分解为原子事实，采用无模式加权度量，控制评估复杂度。
- 实验或效果：在通用和临床数据集上基准测试，发布代码支持事实感知模型训练。

## 摘要（原文）

> Large Language Models have significantly advanced natural language processing tasks, but remain prone to generating incorrect or misleading but plausible arguments. This issue, known as hallucination, is particularly concerning in high-stakes domains like clinical applications, where factual inaccuracies can have severe consequences. Existing evaluation metrics fail to adequately assess factual consistency and lack interpretability, making diagnosing and mitigating errors difficult. We propose an interpretable framework for factual consistency assessment for in-domain and open-domain texts to address these limitations. Our approach decomposes text into atomic facts and introduces a flexible, schema-free methodology. Unlike previous methods with an absolute metric, we incorporate a weighted metric to enhance factual evaluation. Additionally, we propose a mechanism to control assessment complexity in intricate domains. We benchmark our approach on popular general and clinical datasets and release our code to support fact-aware model training in future research.

