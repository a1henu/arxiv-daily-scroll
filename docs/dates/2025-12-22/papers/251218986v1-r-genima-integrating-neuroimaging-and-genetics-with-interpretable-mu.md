---
layout: default
title: R-GenIMA: Integrating Neuroimaging and Genetics with Interpretable Multimodal AI for Alzheimer's Disease Progression
---

# R-GenIMA: Integrating Neuroimaging and Genetics with Interpretable Multimodal AI for Alzheimer's Disease Progression
**arXiv**：[2512.18986v1](https://arxiv.org/abs/2512.18986) · [PDF](https://arxiv.org/pdf/2512.18986.pdf)  
**作者**：Kun Zhao, Siyuan Dai, Yingying Zhang, Guodong Liu, Pengfei Gu, Chenghua Lin, Paul M. Thompson, Alex Leow, Heng Huang, Lifang He, Liang Zhan, Haoteng Tang  

**一句话要点**：提出R-GenIMA模型，通过可解释多模态AI整合神经影像与遗传数据以预测阿尔茨海默病进展

**关键词**：多模态人工智能, 神经影像分析, 遗传学整合, 可解释性模型, 阿尔茨海默病预测, 跨模态注意力

## 3 点简述
- 核心问题：现有方法难以对齐神经影像与遗传异质信号，影响阿尔茨海默病早期检测。
- 方法要点：结合ROI视觉Transformer与遗传提示，通过跨模态注意力链接脑区萎缩与基因因素。
- 实验或效果：在ADNI队列中实现四分类SOTA性能，提供生物学解释如阶段特异性脑区与基因关联。

## 摘要（原文）

> Early detection of Alzheimer's disease (AD) requires models capable of integrating macro-scale neuroanatomical alterations with micro-scale genetic susceptibility, yet existing multimodal approaches struggle to align these heterogeneous signals. We introduce R-GenIMA, an interpretable multimodal large language model that couples a novel ROI-wise vision transformer with genetic prompting to jointly model structural MRI and single nucleotide polymorphisms (SNPs) variations. By representing each anatomically parcellated brain region as a visual token and encoding SNP profiles as structured text, the framework enables cross-modal attention that links regional atrophy patterns to underlying genetic factors. Applied to the ADNI cohort, R-GenIMA achieves state-of-the-art performance in four-way classification across normal cognition (NC), subjective memory concerns (SMC), mild cognitive impairment (MCI), and AD. Beyond predictive accuracy, the model yields biologically meaningful explanations by identifying stage-specific brain regions and gene signatures, as well as coherent ROI-Gene association patterns across the disease continuum. Attention-based attribution revealed genes consistently enriched for established GWAS-supported AD risk loci, including APOE, BIN1, CLU, and RBFOX1. Stage-resolved neuroanatomical signatures identified shared vulnerability hubs across disease stages alongside stage-specific patterns: striatal involvement in subjective decline, frontotemporal engagement during prodromal impairment, and consolidated multimodal network disruption in AD. These results demonstrate that interpretable multimodal AI can synthesize imaging and genetics to reveal mechanistic insights, providing a foundation for clinically deployable tools that enable earlier risk stratification and inform precision therapeutic strategies in Alzheimer's disease.

