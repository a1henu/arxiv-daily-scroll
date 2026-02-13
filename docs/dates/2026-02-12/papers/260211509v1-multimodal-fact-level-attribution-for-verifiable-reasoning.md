---
layout: default
title: Multimodal Fact-Level Attribution for Verifiable Reasoning
---

# Multimodal Fact-Level Attribution for Verifiable Reasoning
**arXiv**：[2602.11509v1](https://arxiv.org/abs/2602.11509) · [PDF](https://arxiv.org/pdf/2602.11509.pdf)  
**作者**：David Wan, Han Wang, Ziyang Wang, Elias Stengel-Eskin, Hyunji Lee, Mohit Bansal  

**一句话要点**：提出MuRGAt基准以评估多模态推理中的事实级归因，支持视频音频等多模态输入。

**关键词**：多模态推理, 事实归因, 基准评估, 视频音频处理, 自动验证

## 3 点简述
- 现有基准无法评估复杂多模态推理中的事实归因，聚焦简化观察场景。
- 引入MuRGAt基准，要求模型生成带明确推理和精确引用的答案，引用需指定模态和时间段。
- 自动评估框架与人类判断强相关，实验显示强MLLMs常产生幻觉引用，推理深度增加可能降低准确性。

## 摘要（原文）

> Multimodal large language models (MLLMs) are increasingly used for real-world tasks involving multi-step reasoning and long-form generation, where reliability requires grounding model outputs in heterogeneous input sources and verifying individual factual claims. However, existing multimodal grounding benchmarks and evaluation methods focus on simplified, observation-based scenarios or limited modalities and fail to assess attribution in complex multimodal reasoning. We introduce MuRGAt (Multimodal Reasoning with Grounded Attribution), a benchmark for evaluating fact-level multimodal attribution in settings that require reasoning beyond direct observation. Given inputs spanning video, audio, and other modalities, MuRGAt requires models to generate answers with explicit reasoning and precise citations, where each citation specifies both modality and temporal segments. To enable reliable assessment, we introduce an automatic evaluation framework that strongly correlates with human judgments. Benchmarking with human and automated scores reveals that even strong MLLMs frequently hallucinate citations despite correct reasoning. Moreover, we observe a key trade-off: increasing reasoning depth or enforcing structured grounding often degrades accuracy, highlighting a significant gap between internal reasoning and verifiable attribution.

