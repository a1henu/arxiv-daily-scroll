---
layout: default
title: How Close Are We? Limitations and Progress of AI Models in Banff Lesion Scoring
---

# How Close Are We? Limitations and Progress of AI Models in Banff Lesion Scoring
**arXiv**：[2510.27158v1](https://arxiv.org/abs/2510.27158) · [PDF](https://arxiv.org/pdf/2510.27158.pdf)  
**作者**：Yanfan Zhu, Juming Xiong, Ruining Deng, Yu Wang, Yaohong Wang, Shilin Zhao, Mengmeng Yin, Yuqing Liu, Haichun Yang, Yuankai Huo  

**一句话要点**：评估AI模型在Banff病变评分中的可行性，揭示其局限与进展

**关键词**：Banff病变评分, 深度学习模型, 模块化框架, 肾移植病理, AI评估, 检测分割

## 3 点简述
- 核心问题：Banff分类标准半定量、复杂且存在观察者间差异，AI复制困难。
- 方法要点：采用模块化规则框架，分解病变指标，映射模型输出到Banff评分。
- 实验或效果：模型部分成功，但存在结构遗漏、幻觉和检测模糊等失败模式。

## 摘要（原文）

> The Banff Classification provides the global standard for evaluating renal
> transplant biopsies, yet its semi-quantitative nature, complex criteria, and
> inter-observer variability present significant challenges for computational
> replication. In this study, we explore the feasibility of approximating Banff
> lesion scores using existing deep learning models through a modular, rule-based
> framework. We decompose each Banff indicator - such as glomerulitis (g),
> peritubular capillaritis (ptc), and intimal arteritis (v) - into its
> constituent structural and inflammatory components, and assess whether current
> segmentation and detection tools can support their computation. Model outputs
> are mapped to Banff scores using heuristic rules aligned with expert
> guidelines, and evaluated against expert-annotated ground truths. Our findings
> highlight both partial successes and critical failure modes, including
> structural omission, hallucination, and detection ambiguity. Even when final
> scores match expert annotations, inconsistencies in intermediate
> representations often undermine interpretability. These results reveal the
> limitations of current AI pipelines in replicating computational expert-level
> grading, and emphasize the importance of modular evaluation and computational
> Banff grading standard in guiding future model development for transplant
> pathology.

