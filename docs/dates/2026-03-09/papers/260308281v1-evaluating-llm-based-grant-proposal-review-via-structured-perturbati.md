---
layout: default
title: Evaluating LLM-Based Grant Proposal Review via Structured Perturbations
---

# Evaluating LLM-Based Grant Proposal Review via Structured Perturbations
**arXiv**：[2603.08281v1](https://arxiv.org/abs/2603.08281) · [PDF](https://arxiv.org/pdf/2603.08281.pdf)  
**作者**：William Thorne, Joseph James, Yang Wang, Chenghua Lin, Diana Maynard  

**一句话要点**：提出基于结构化扰动的框架，评估LLM在EPSRC资助提案评审中的能力与局限性。

**关键词**：LLM评估, 资助提案评审, 结构化扰动, 评审架构, 质量维度, EPSRC

## 3 点简述
- 核心问题：AI辅助提案增长超出人工评审能力，需评估LLM在高风险评审中的表现。
- 方法要点：开发扰动框架，测试LLM在六个质量维度上的敏感性，比较三种评审架构。
- 实验或效果：逐节分析法在检测率和评分可靠性上显著优于其他方法，但LLM反馈偏向合规检查。

## 摘要（原文）

> As AI-assisted grant proposals outpace manual review capacity in a kind of ``Malthusian trap'' for the research ecosystem, this paper investigates the capabilities and limitations of LLM-based grant reviewing for high-stakes evaluation. Using six EPSRC proposals, we develop a perturbation-based framework probing LLM sensitivity across six quality axes: funding, timeline, competency, alignment, clarity, and impact. We compare three review architectures: single-pass review, section-by-section analysis, and a 'Council of Personas' ensemble emulating expert panels. The section-level approach significantly outperforms alternatives in both detection rate and scoring reliability, while the computationally expensive council method performs no better than baseline. Detection varies substantially by perturbation type, with alignment issues readily identified but clarity flaws largely missed by all systems. Human evaluation shows LLM feedback is largely valid but skewed toward compliance checking over holistic assessment. We conclude that current LLMs may provide supplementary value within EPSRC review but exhibit high variability and misaligned review priorities. We release our code and any non-protected data.

