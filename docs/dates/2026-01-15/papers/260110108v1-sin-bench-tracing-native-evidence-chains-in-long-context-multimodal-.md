---
layout: default
title: SIN-Bench: Tracing Native Evidence Chains in Long-Context Multimodal Scientific Interleaved Literature
---

# SIN-Bench: Tracing Native Evidence Chains in Long-Context Multimodal Scientific Interleaved Literature
**arXiv**：[2601.10108v1](https://arxiv.org/abs/2601.10108) · [PDF](https://arxiv.org/pdf/2601.10108.pdf)  
**作者**：Yiming Ren, Junjie Wang, Yuxin Meng, Yihang Shi, Zhiqiang Lin, Ruihang Chu, Yiran Xu, Ziming Li, Yunfei Zhao, Zihan Wang, Yu Qiao, Ruiming Tang, Minghao Liu, Yujiu Yang  

**一句话要点**：提出SIN-Bench基准以评估多模态大模型在长上下文科学文献中的证据链追踪能力

**关键词**：多模态大语言模型, 长上下文理解, 科学文献分析, 证据链追踪, 基准评估

## 3 点简述
- 核心问题：现有评估方法难以衡量多模态大模型对长科学文献的因果证据链理解
- 方法要点：基于FITO范式构建SIN-Data语料和SIN-Bench基准，包含四个渐进任务
- 实验或效果：在八个模型上测试，发现证据锚定是主要瓶颈，模型在正确性与可追溯支持间存在差距

## 摘要（原文）

> Evaluating whether multimodal large language models truly understand long-form scientific papers remains challenging: answer-only metrics and synthetic "Needle-In-A-Haystack" tests often reward answer matching without requiring a causal, evidence-linked reasoning trace in the document. We propose the "Fish-in-the-Ocean" (FITO) paradigm, which requires models to construct explicit cross-modal evidence chains within native scientific documents. To operationalize FITO, we build SIN-Data, a scientific interleaved corpus that preserves the native interleaving of text and figures. On top of it, we construct SIN-Bench with four progressive tasks covering evidence discovery (SIN-Find), hypothesis verification (SIN-Verify), grounded QA (SIN-QA), and evidence-anchored synthesis (SIN-Summary). We further introduce "No Evidence, No Score", scoring predictions when grounded to verifiable anchors and diagnosing evidence quality via matching, relevance, and logic. Experiments on eight MLLMs show that grounding is the primary bottleneck: Gemini-3-pro achieves the best average overall score (0.573), while GPT-5 attains the highest SIN-QA answer accuracy (0.767) but underperforms on evidence-aligned overall scores, exposing a gap between correctness and traceable support.

