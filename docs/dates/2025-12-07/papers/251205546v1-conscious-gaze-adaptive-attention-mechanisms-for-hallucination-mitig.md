---
layout: default
title: Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models
---

# Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models
**arXiv**：[2512.05546v1](https://arxiv.org/abs/2512.05546) · [PDF](https://arxiv.org/pdf/2512.05546.pdf)  
**作者**：Weijue Bu, Guan Yuan, Guixian Zhang  

**一句话要点**：提出Conscious Gaze框架，通过游戏论解释性实现推理时注意力控制，以缓解视觉语言模型中的幻觉问题。

**关键词**：视觉语言模型, 幻觉缓解, 注意力机制, 推理时控制, 游戏论解释性, 无训练框架

## 3 点简述
- 核心问题：视觉语言模型存在文本惯性，注意力从视觉证据漂移至语言先验，导致对象幻觉。
- 方法要点：基于Harsanyi交互构建认知需求传感器，检测视觉-文本协同；通过聚焦共识诱导模块选择性重定向中层注意力至视觉标记。
- 实验或效果：在POPE和CHAIR基准上实现SOTA，适用于多种模型，保持通用能力，无需训练。

## 摘要（原文）

> Large Vision-Language Models (VLMs) often exhibit text inertia, where attention drifts from visual evidence toward linguistic priors, resulting in object hallucinations. Existing decoding strategies intervene only at the output logits and thus cannot correct internal reasoning drift, while recent internal-control methods based on heuristic head suppression or global steering vectors lack principled grounding. We introduce Conscious Gaze (CG-VLM), a training-free, inference-time framework that converts game-theoretic interpretability into actionable decoding control. A Cognitive Demand Sensor built on Harsanyi interactions estimates instantaneous vision-text synergy and identifies moments when visual grounding is necessary. Conditioned on this signal, a Focused Consensus Induction module selectively reorients mid-layer attention toward visual tokens before collapse into text priors. CG-VLM achieves state-of-the-art results on POPE and CHAIR across InstructBLIP, LLaVA, Qwen-VL, and mPLUG, while preserving general capabilities, demonstrating that token-level sensing enables precise, context-aware intervention without compromising foundational knowledge.

