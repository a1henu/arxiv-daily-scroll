---
layout: default
title: Permissive-Washing in the Open AI Supply Chain: A Large-Scale Audit of License Integrity
---

# Permissive-Washing in the Open AI Supply Chain: A Large-Scale Audit of License Integrity
**arXiv**：[2602.08816v1](https://arxiv.org/abs/2602.08816) · [PDF](https://arxiv.org/pdf/2602.08816.pdf)  
**作者**：James Jewitt, Gopi Krishnan Rajbahadur, Hao Li, Bram Adams, Ahmed E. Hassan  

**一句话要点**：提出许可清洗概念并大规模审计AI供应链中的许可证完整性

**关键词**：开源许可证, AI供应链, 许可清洗, 大规模审计, 法律合规, 下游传播

## 3 点简述
- 核心问题：AI开源许可中普遍存在许可清洗现象，即标注为宽松许可但缺失必要法律文档，导致下游使用可能侵权。
- 方法要点：通过自动化管道审计Hugging Face和GitHub上的数据集、模型和应用供应链，验证许可证文本和版权要求。
- 实验或效果：发现超过95%的数据集和模型缺乏许可证文本，仅少数满足完整要求，且上游合规信息很少向下游传播。

## 摘要（原文）

> Permissive licenses like MIT, Apache-2.0, and BSD-3-Clause dominate open-source AI, signaling that artifacts like models, datasets, and code can be freely used, modified, and redistributed. However, these licenses carry mandatory requirements: include the full license text, provide a copyright notice, and preserve upstream attribution, that remain unverified at scale. Failure to meet these conditions can place reuse outside the scope of the license, effectively leaving AI artifacts under default copyright for those uses and exposing downstream users to litigation. We call this phenomenon ``permissive washing'': labeling AI artifacts as free to use, while omitting the legal documentation required to make that label actionable. To assess how widespread permissive washing is in the AI supply chain, we empirically audit 124,278 dataset $\rightarrow$ model $\rightarrow$ application supply chains, spanning 3,338 datasets, 6,664 models, and 28,516 applications across Hugging Face and GitHub. We find that an astonishing 96.5\% of datasets and 95.8\% of models lack the required license text, only 2.3\% of datasets and 3.2\% of models satisfy both license text and copyright requirements, and even when upstream artifacts provide complete licensing evidence, attribution rarely propagates downstream: only 27.59\% of models preserve compliant dataset notices and only 5.75\% of applications preserve compliant model notices (with just 6.38\% preserving any linked upstream notice). Practitioners cannot assume permissive labels confer the rights they claim: license files and notices, not metadata, are the source of legal truth. To support future research, we release our full audit dataset and reproducible pipeline.

