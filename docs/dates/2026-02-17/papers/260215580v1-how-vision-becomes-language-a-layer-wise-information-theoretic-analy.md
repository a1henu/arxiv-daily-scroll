---
layout: default
title: How Vision Becomes Language: A Layer-wise Information-Theoretic Analysis of Multimodal Reasoning
---

# How Vision Becomes Language: A Layer-wise Information-Theoretic Analysis of Multimodal Reasoning
**arXiv**：[2602.15580v1](https://arxiv.org/abs/2602.15580) · [PDF](https://arxiv.org/pdf/2602.15580.pdf)  
**作者**：Hongxuan Wu, Yukun Zhang, Xueqing Zhou  

**一句话要点**：提出基于部分信息分解的层间分析框架，揭示多模态Transformer中视觉信息向语言转换的模式。

**关键词**：多模态推理, 信息论分析, Transformer层间分析, 部分信息分解, 视觉语言转换, 模态转导

## 3 点简述
- 核心问题：多模态Transformer预测时视觉、语言和跨模态计算的作用及层间演化。
- 方法要点：引入PID Flow结合降维、高斯化和高斯PID估计，分解预测信息为冗余、视觉独特、语言独特和协同成分。
- 实验或效果：在LLaVA模型上发现视觉独特信息早峰衰减，语言独特信息晚层主导，跨模态协同低于2%，且模式稳定但任务依赖。

## 摘要（原文）

> When a multimodal Transformer answers a visual question, is the prediction driven by visual evidence, linguistic reasoning, or genuinely fused cross-modal computation -- and how does this structure evolve across layers? We address this question with a layer-wise framework based on Partial Information Decomposition (PID) that decomposes the predictive information at each Transformer layer into redundant, vision-unique, language-unique, and synergistic components. To make PID tractable for high-dimensional neural representations, we introduce \emph{PID Flow}, a pipeline combining dimensionality reduction, normalizing-flow Gaussianization, and closed-form Gaussian PID estimation. Applying this framework to LLaVA-1.5-7B and LLaVA-1.6-7B across six GQA reasoning tasks, we uncover a consistent \emph{modal transduction} pattern: visual-unique information peaks early and decays with depth, language-unique information surges in late layers to account for roughly 82\% of the final prediction, and cross-modal synergy remains below 2\%. This trajectory is highly stable across model variants (layer-wise correlations $>$0.96) yet strongly task-dependent, with semantic redundancy governing the detailed information fingerprint. To establish causality, we perform targeted Image$\rightarrow$Question attention knockouts and show that disrupting the primary transduction pathway induces predictable increases in trapped visual-unique information, compensatory synergy, and total information cost -- effects that are strongest in vision-dependent tasks and weakest in high-redundancy tasks. Together, these results provide an information-theoretic, causal account of how vision becomes language in multimodal Transformers, and offer quantitative guidance for identifying architectural bottlenecks where modality-specific information is lost.

