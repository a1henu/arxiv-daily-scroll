---
layout: default
title: DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity
---

# DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity
**arXiv**：[2602.11685v1](https://arxiv.org/abs/2602.11685) · [PDF](https://arxiv.org/pdf/2602.11685.pdf)  
**作者**：Joey Zhong, Hao Zhang, Clare Southern, Jeremy Yang, Thomas Wang, Kate Jung, Shu Zhang, Denis Yarats, Johnny Ho, Jerry Ma  

**一句话要点**：提出DRACO基准以评估跨领域深度研究任务的准确性、完整性和客观性。

**关键词**：深度研究基准, 跨领域评估, 任务匿名化, 客观评分, 公开数据集

## 3 点简述
- 核心问题：缺乏评估复杂深度研究任务性能的标准化基准。
- 方法要点：基于真实使用模式构建跨10个领域、40个国家信息源的匿名任务集。
- 实验或效果：通过四维度评分标准（如事实准确性）进行客观评估，并公开可用。

## 摘要（原文）

> We present DRACO (Deep Research Accuracy, Completeness, and Objectivity), a benchmark of complex deep research tasks. These tasks, which span 10 domains and draw on information sources from 40 countries, originate from anonymized real-world usage patterns within a large-scale deep research system. Tasks are sampled from a de-identified dataset of Perplexity Deep Research requests, then filtered and augmented to ensure that the tasks are anonymized, open-ended and complex, objectively evaluable, and representative of the broad scope of real-world deep research use cases. Outputs are graded against task-specific rubrics along four dimensions: factual accuracy (accuracy), breadth and depth of analysis (including completeness), presentation quality (including objectivity), and citation quality. DRACO is publicly available at https://hf.co/datasets/perplexity-ai/draco.

