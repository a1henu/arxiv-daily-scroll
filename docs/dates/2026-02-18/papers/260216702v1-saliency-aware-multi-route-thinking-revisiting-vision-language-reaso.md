---
layout: default
title: Saliency-Aware Multi-Route Thinking: Revisiting Vision-Language Reasoning
---

# Saliency-Aware Multi-Route Thinking: Revisiting Vision-Language Reasoning
**arXiv**：[2602.16702v1](https://arxiv.org/abs/2602.16702) · [PDF](https://arxiv.org/pdf/2602.16702.pdf)  
**作者**：Mingjia Shi, Yinhan He, Yaochen Zhu, Jundong Li  

**一句话要点**：提出SAP原则以解决视觉语言推理中视觉信息利用不足和错误累积问题。

**关键词**：视觉语言推理, 多路径推理, 物体幻觉减少, 推理稳定性, 模型无关方法

## 3 点简述
- 核心问题：视觉语言模型推理时视觉输入仅初始提供，导致文本主导和早期视觉错误累积。
- 方法要点：SAP基于高层推理原则而非词元轨迹，支持稳定控制和多路径推理，无需额外训练。
- 实验或效果：在可比词元预算下减少物体幻觉，推理更稳定且延迟低于长序列推理方法。

## 摘要（原文）

> Vision-language models (VLMs) aim to reason by jointly leveraging visual and textual modalities. While allocating additional inference-time computation has proven effective for large language models (LLMs), achieving similar scaling in VLMs remains challenging. A key obstacle is that visual inputs are typically provided only once at the start of generation, while textual reasoning (e.g., early visual summaries) is generated autoregressively, causing reasoning to become increasingly text-dominated and allowing early visual grounding errors to accumulate. Moreover, vanilla guidance for visual grounding during inference is often coarse and noisy, making it difficult to steer reasoning over long texts. To address these challenges, we propose \emph{Saliency-Aware Principle} (SAP) selection. SAP operates on high-level reasoning principles rather than token-level trajectories, which enable stable control over discrete generation under noisy feedback while allowing later reasoning steps to re-consult visual evidence when renewed grounding is required. In addition, SAP supports multi-route inference, enabling parallel exploration of diverse reasoning behaviors. SAP is model-agnostic and data-free, requiring no additional training. Empirical results show that SAP achieves competitive performance, especially in reducing object hallucination, under comparable token-generation budgets while yielding more stable reasoning and lower response latency than CoT-style long sequential reasoning.

