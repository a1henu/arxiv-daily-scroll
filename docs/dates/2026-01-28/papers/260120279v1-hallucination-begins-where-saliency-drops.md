---
layout: default
title: Hallucination Begins Where Saliency Drops
---

# Hallucination Begins Where Saliency Drops
**arXiv**：[2601.20279v1](https://arxiv.org/abs/2601.20279) · [PDF](https://arxiv.org/pdf/2601.20279.pdf)  
**作者**：Xiaofeng Zhang, Yuanchao Zhu, Chaochen Gu, Xiaosong Yuan, Qiyan Zhao, Jiawei Cao, Feilong Tang, Sinan Fan, Yaomin Shen, Chen Shen, Hao Tang  

**一句话要点**：提出LVLMs-Saliency框架以缓解大型视觉语言模型中的幻觉问题

**关键词**：大型视觉语言模型, 幻觉检测, 梯度感知诊断, 推理时缓解, 注意力机制, 视觉基础

## 3 点简述
- 核心问题：现有方法依赖前向注意力，难以可靠区分幻觉与事实输出。
- 方法要点：融合注意力权重与输入梯度，量化输出令牌的视觉基础强度。
- 实验或效果：通过SGRS和LocoRE机制，显著降低幻觉率，保持流畅性和任务性能。

## 摘要（原文）

> Recent studies have examined attention dynamics in large vision-language models (LVLMs) to detect hallucinations. However, existing approaches remain limited in reliably distinguishing hallucinated from factually grounded outputs, as they rely solely on forward-pass attention patterns and neglect gradient-based signals that reveal how token influence propagates through the network. To bridge this gap, we introduce LVLMs-Saliency, a gradient-aware diagnostic framework that quantifies the visual grounding strength of each output token by fusing attention weights with their input gradients. Our analysis uncovers a decisive pattern: hallucinations frequently arise when preceding output tokens exhibit low saliency toward the prediction of the next token, signaling a breakdown in contextual memory retention. Leveraging this insight, we propose a dual-mechanism inference-time framework to mitigate hallucinations: (1) Saliency-Guided Rejection Sampling (SGRS), which dynamically filters candidate tokens during autoregressive decoding by rejecting those whose saliency falls below a context-adaptive threshold, thereby preventing coherence-breaking tokens from entering the output sequence; and (2) Local Coherence Reinforcement (LocoRE), a lightweight, plug-and-play module that strengthens attention from the current token to its most recent predecessors, actively counteracting the contextual forgetting behavior identified by LVLMs-Saliency. Extensive experiments across multiple LVLMs demonstrate that our method significantly reduces hallucination rates while preserving fluency and task performance, offering a robust and interpretable solution for enhancing model reliability. Code is available at: https://github.com/zhangbaijin/LVLMs-Saliency

