---
layout: default
title: Conceptual Cultural Index: A Metric for Cultural Specificity via Relative Generality
---

# Conceptual Cultural Index: A Metric for Cultural Specificity via Relative Generality
**arXiv**：[2602.09444v1](https://arxiv.org/abs/2602.09444) · [PDF](https://arxiv.org/pdf/2602.09444.pdf)  
**作者**：Takumi Ohashi, Hitoshi Iyatomi  

**一句话要点**：提出概念文化指数以评估句子级文化特异性，适用于多文化环境下的LLM部署。

**关键词**：文化特异性评估, 句子级度量, 多文化LLM部署, 泛化度差异, 概念文化指数

## 3 点简述
- 核心问题：多文化环境中，句子级文化特异性评估缺乏系统方法。
- 方法要点：基于目标文化内与跨文化平均的泛化度差异定义指数，支持操作控制与可解释性。
- 实验或效果：在400句数据集上验证，指数分布符合预期，AUC提升超10点优于直接LLM评分。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed in multicultural settings; however, systematic evaluation of cultural specificity at the sentence level remains underexplored. We propose the Conceptual Cultural Index (CCI), which estimates cultural specificity at the sentence level. CCI is defined as the difference between the generality estimate within the target culture and the average generality estimate across other cultures. This formulation enables users to operationally control the scope of culture via comparison settings and provides interpretability, since the score derives from the underlying generality estimates. We validate CCI on 400 sentences (200 culture-specific and 200 general), and the resulting score distribution exhibits the anticipated pattern: higher for culture-specific sentences and lower for general ones. For binary separability, CCI outperforms direct LLM scoring, yielding more than a 10-point improvement in AUC for models specialized to the target culture. Our code is available at https://github.com/IyatomiLab/CCI .

