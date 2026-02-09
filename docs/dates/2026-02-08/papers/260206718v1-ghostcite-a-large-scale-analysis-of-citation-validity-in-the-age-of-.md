---
layout: default
title: GhostCite: A Large-Scale Analysis of Citation Validity in the Age of Large Language Models
---

# GhostCite: A Large-Scale Analysis of Citation Validity in the Age of Large Language Models
**arXiv**：[2602.06718v1](https://arxiv.org/abs/2602.06718) · [PDF](https://arxiv.org/pdf/2602.06718.pdf)  
**作者**：Zuyao Xu, Yuqi Qiu, Lu Sun, FaSheng Miao, Fubin Wu, Xinyi Wang, Xiang Li, Haozhe Lu, ZhengZe Zhang, Yuxin Hu, Jialu Li, Jin Luo, Feng Zhang, Rui Luo, Xinran Liu, Yingxian Li, Jiaji Liu  

**一句话要点**：提出CiteVerifier框架以分析大语言模型时代引文有效性危机

**关键词**：引文验证, 大语言模型, 学术诚信, 虚假引文, 科学记录污染, 验证框架

## 3 点简述
- 核心问题：大语言模型生成虚假引文威胁科学信任，需量化风险。
- 方法要点：开发CiteVerifier开源框架，进行大规模引文验证实验。
- 实验或效果：评估13个LLM引文生成，分析220万引文，调查研究者验证行为。

## 摘要（原文）

> Citations provide the basis for trusting scientific claims; when they are invalid or fabricated, this trust collapses. With the advent of Large Language Models (LLMs), this risk has intensified: LLMs are increasingly used for academic writing, yet their tendency to fabricate citations (``ghost citations'') poses a systemic threat to citation validity.
>   To quantify this threat and inform mitigation, we develop CiteVerifier, an open-source framework for large-scale citation verification, and conduct the first comprehensive study of citation validity in the LLM era through three experiments built on it. We benchmark 13 state-of-the-art LLMs on citation generation across 40 research domains, finding that all models hallucinate citations at rates from 14.23\% to 94.93\%, with significant variation across research domains. Moreover, we analyze 2.2 million citations from 56,381 papers published at top-tier AI/ML and Security venues (2020--2025), confirming that 1.07\% of papers contain invalid or fabricated citations (604 papers), with an 80.9\% increase in 2025 alone. Furthermore, we survey 97 researchers and analyze 94 valid responses after removing 3 conflicting samples, revealing a critical ``verification gap'': 41.5\% of researchers copy-paste BibTeX without checking and 44.4\% choose no-action responses when encountering suspicious references; meanwhile, 76.7\% of reviewers do not thoroughly check references and 80.0\% never suspect fake citations. Our findings reveal an accelerating crisis where unreliable AI tools, combined with inadequate human verification by researchers and insufficient peer review scrutiny, enable fabricated citations to contaminate the scientific record. We propose interventions for researchers, venues, and tool developers to protect citation integrity.

