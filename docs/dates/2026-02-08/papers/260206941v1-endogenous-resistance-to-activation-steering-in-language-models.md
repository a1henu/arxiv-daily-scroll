---
layout: default
title: Endogenous Resistance to Activation Steering in Language Models
---

# Endogenous Resistance to Activation Steering in Language Models
**arXiv**：[2602.06941v1](https://arxiv.org/abs/2602.06941) · [PDF](https://arxiv.org/pdf/2602.06941.pdf)  
**作者**：Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, Michael S. A. Graziano  

**一句话要点**：提出内源性转向抵抗（ESR）概念，揭示大语言模型在推理中抵抗任务不匹配激活转向的能力。

**关键词**：内源性转向抵抗, 激活转向, 稀疏自编码器, 语言模型鲁棒性, 因果分析

## 3 点简述
- 核心问题：大语言模型在激活转向干预下可能恢复并改进响应，称为内源性转向抵抗（ESR）。
- 方法要点：使用稀疏自编码器（SAE）潜在变量进行激活转向，识别与ESR因果相关的潜在变量。
- 实验或效果：在Llama-3.3-70B中，零消融相关潜在变量使多尝试率降低25%，通过提示和训练增强ESR。

## 摘要（原文）

> Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate differentially during off-topic content and are causally linked to ESR in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25%, providing causal evidence for dedicated internal consistency-checking circuits. We demonstrate that ESR can be deliberately enhanced through both prompting and training: meta-prompts instructing the model to self-monitor increase the multi-attempt rate by 4x for Llama-3.3-70B, and fine-tuning on self-correction examples successfully induces ESR-like behavior in smaller models. These findings have dual implications: ESR could protect against adversarial manipulation but might also interfere with beneficial safety interventions that rely on activation steering. Understanding and controlling these resistance mechanisms is important for developing transparent and controllable AI systems. Code is available at github.com/agencyenterprise/endogenous-steering-resistance.

