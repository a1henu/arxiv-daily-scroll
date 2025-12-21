---
layout: default
title: GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation
---

# GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation
**arXiv**：[2512.16853v1](https://arxiv.org/abs/2512.16853) · [PDF](https://arxiv.org/pdf/2512.16853.pdf)  
**作者**：Amita Kamath, Kai-Wei Chang, Ranjay Krishna, Luke Zettlemoyer, Yushi Hu, Marjan Ghazvininejad  

**一句话要点**：提出GenEval 2基准和Soft-TIFA方法以解决文本到图像评估中的基准漂移问题

**关键词**：文本到图像评估, 基准漂移, GenEval 2, Soft-TIFA, 视觉基元, 组合性

## 3 点简述
- 核心问题：GenEval基准随时间漂移，与人类判断偏差高达17.7%，导致评估失效
- 方法要点：引入GenEval 2基准，增强视觉基元覆盖和组合性，并开发Soft-TIFA评估方法
- 实验或效果：通过大规模人类研究验证漂移，新基准对当前模型更具挑战性，评估更接近人类判断

## 摘要（原文）

> Automating Text-to-Image (T2I) model evaluation is challenging; a judge model must be used to score correctness, and test prompts must be selected to be challenging for current T2I models but not the judge. We argue that satisfying these constraints can lead to benchmark drift over time, where the static benchmark judges fail to keep up with newer model capabilities. We show that benchmark drift is a significant problem for GenEval, one of the most popular T2I benchmarks. Although GenEval was well-aligned with human judgment at the time of its release, it has drifted far from human judgment over time -- resulting in an absolute error of as much as 17.7% for current models. This level of drift strongly suggests that GenEval has been saturated for some time, as we verify via a large-scale human study. To help fill this benchmarking gap, we introduce a new benchmark, GenEval 2, with improved coverage of primitive visual concepts and higher degrees of compositionality, which we show is more challenging for current models. We also introduce Soft-TIFA, an evaluation method for GenEval 2 that combines judgments for visual primitives, which we show is more well-aligned with human judgment and argue is less likely to drift from human-alignment over time (as compared to more holistic judges such as VQAScore). Although we hope GenEval 2 will provide a strong benchmark for many years, avoiding benchmark drift is far from guaranteed and our work, more generally, highlights the importance of continual audits and improvement for T2I and related automated model evaluation benchmarks.

