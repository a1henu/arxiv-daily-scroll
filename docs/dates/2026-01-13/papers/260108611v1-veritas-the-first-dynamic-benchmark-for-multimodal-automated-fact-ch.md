---
layout: default
title: VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking
---

# VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking
**arXiv**：[2601.08611v1](https://arxiv.org/abs/2601.08611) · [PDF](https://arxiv.org/pdf/2601.08611.pdf)  
**作者**：Mark Rothermel, Marcus Kornmann, Marcus Rohrbach, Anna Rohrbach  

**一句话要点**：提出首个动态多模态自动事实核查基准VeriTaS，以应对大模型预训练中的数据泄露问题。

**关键词**：自动事实核查, 动态基准, 多模态评估, 数据泄露, 标准化评分, 多语言处理

## 3 点简述
- 现有自动事实核查基准多为静态，易受大模型预训练数据泄露影响，导致评估不可靠。
- VeriTaS通过自动化流水线动态更新，涵盖多语言、多模态真实世界声明，并标准化评分方案。
- 人类评估验证自动化标注准确性，承诺定期更新以支持稳健的自动事实核查评估。

## 摘要（原文）

> The growing scale of online misinformation urgently demands Automated Fact-Checking (AFC). Existing benchmarks for evaluating AFC systems, however, are largely limited in terms of task scope, modalities, domain, language diversity, realism, or coverage of misinformation types. Critically, they are static, thus subject to data leakage as their claims enter the pretraining corpora of LLMs. As a result, benchmark performance no longer reliably reflects the actual ability to verify claims. We introduce Verified Theses and Statements (VeriTaS), the first dynamic benchmark for multimodal AFC, designed to remain robust under ongoing large-scale pretraining of foundation models. VeriTaS currently comprises 24,000 real-world claims from 108 professional fact-checking organizations across 54 languages, covering textual and audiovisual content. Claims are added quarterly via a fully automated seven-stage pipeline that normalizes claim formulation, retrieves original media, and maps heterogeneous expert verdicts to a novel, standardized, and disentangled scoring scheme with textual justifications. Through human evaluation, we demonstrate that the automated annotations closely match human judgments. We commit to update VeriTaS in the future, establishing a leakage-resistant benchmark, supporting meaningful AFC evaluation in the era of rapidly evolving foundation models. We will make the code and data publicly available.

