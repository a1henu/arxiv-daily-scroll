---
layout: default
title: Benchmarking Document Parsers on Mathematical Formula Extraction from PDFs
---

# Benchmarking Document Parsers on Mathematical Formula Extraction from PDFs
**arXiv**：[2512.09874v1](https://arxiv.org/abs/2512.09874) · [PDF](https://arxiv.org/pdf/2512.09874.pdf)  
**作者**：Pius Horn, Janis Keuper  

**一句话要点**：提出基于合成PDF与LLM评估的基准框架，以解决数学公式提取的评测难题。

**关键词**：PDF解析基准, 数学公式提取, LLM评估, 合成数据生成, 语义匹配

## 3 点简述
- 核心问题：现有PDF解析器评测基准缺乏对数学公式的语义评估，影响下游应用。
- 方法要点：使用合成PDF生成精确LaTeX真值，并引入LLM作为语义评估器，结合两阶段匹配处理输出不一致性。
- 实验或效果：通过人类验证，LLM评估与人类判断相关性高（Pearson r=0.78），评测20+解析器揭示性能差异。

## 摘要（原文）

> Correctly parsing mathematical formulas from PDFs is critical for training large language models and building scientific knowledge bases from academic literature, yet existing benchmarks either exclude formulas entirely or lack semantically-aware evaluation metrics. We introduce a novel benchmarking framework centered on synthetically generated PDFs with precise LaTeX ground truth, enabling systematic control over layout, formulas, and content characteristics. A key methodological contribution is pioneering LLM-as-a-judge for semantic formula assessment, combined with a robust two-stage matching pipeline that handles parser output inconsistencies. Through human validation on 250 formula pairs (750 ratings from 30 evaluators), we demonstrate that LLM-based evaluation achieves substantially higher correlation with human judgment (Pearson r=0.78) compared to CDM (r=0.34) and text similarity (r~0). Evaluating 20+ contemporary PDF parsers (including specialized OCR models, vision-language models, and rule-based approaches) across 100 synthetic documents with 2,000+ formulas reveals significant performance disparities. Our findings provide crucial insights for practitioners selecting parsers for downstream applications and establish a robust, scalable methodology that enables reproducible evaluation of PDF formula extraction quality. Code and benchmark data: https://github.com/phorn1/pdf-parse-bench

