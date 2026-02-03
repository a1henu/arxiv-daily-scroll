---
layout: default
title: Mixture-of-Experts with Intermediate CTC Supervision for Accented Speech Recognition
---

# Mixture-of-Experts with Intermediate CTC Supervision for Accented Speech Recognition
**arXiv**：[2602.01967v1](https://arxiv.org/abs/2602.01967) · [PDF](https://arxiv.org/pdf/2602.01967.pdf)  
**作者**：Wonjun Lee, Hyounghun Kim, Gary Geunbae Lee  

**一句话要点**：提出Moe-Ctc，一种带中间CTC监督的混合专家架构，以提升带口音语音识别的鲁棒性。

**关键词**：带口音语音识别, 混合专家架构, CTC监督, 路由机制, 鲁棒性提升

## 3 点简述
- 核心问题：带口音语音识别因训练数据偏向高资源英语变体，导致性能下降。
- 方法要点：采用混合专家架构，通过口音感知路由和CTC监督促进专家专业化和泛化。
- 实验或效果：在Mcv-Accent基准上，相比FastConformer基线，相对WER降低达29.3%。

## 摘要（原文）

> Accented speech remains a persistent challenge for automatic speech recognition (ASR), as most models are trained on data dominated by a few high-resource English varieties, leading to substantial performance degradation for other accents. Accent-agnostic approaches improve robustness yet struggle with heavily accented or unseen varieties, while accent-specific methods rely on limited and often noisy labels. We introduce Moe-Ctc, a Mixture-of-Experts architecture with intermediate CTC supervision that jointly promotes expert specialization and generalization. During training, accent-aware routing encourages experts to capture accent-specific patterns, which gradually transitions to label-free routing for inference. Each expert is equipped with its own CTC head to align routing with transcription quality, and a routing-augmented loss further stabilizes optimization. Experiments on the Mcv-Accent benchmark demonstrate consistent gains across both seen and unseen accents in low- and high-resource conditions, achieving up to 29.3% relative WER reduction over strong FastConformer baselines.

