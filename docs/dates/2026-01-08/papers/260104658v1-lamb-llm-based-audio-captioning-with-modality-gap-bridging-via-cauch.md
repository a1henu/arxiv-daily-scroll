---
layout: default
title: LAMB: LLM-based Audio Captioning with Modality Gap Bridging via Cauchy-Schwarz Divergence
---

# LAMB: LLM-based Audio Captioning with Modality Gap Bridging via Cauchy-Schwarz Divergence
**arXiv**：[2601.04658v1](https://arxiv.org/abs/2601.04658) · [PDF](https://arxiv.org/pdf/2601.04658.pdf)  
**作者**：Hyeongkeun Lee, Jongmin Choi, KiHyun Nam, Joon Son Chung  

**一句话要点**：提出LAMB框架，通过柯西-施瓦茨散度桥接音频与文本模态间隙，以增强LLM在音频描述中的推理能力。

**关键词**：音频描述, 跨模态对齐, 柯西-施瓦茨散度, 大语言模型, 模态间隙桥接, 双流适配器

## 3 点简述
- 核心问题：现有方法未考虑跨模态对齐，导致LLM在音频描述中推理能力未充分利用。
- 方法要点：设计跨模态对齐器最小化柯西-施瓦茨散度并最大化互信息，结合双流适配器提取语义丰富音频嵌入。
- 实验或效果：在AudioCaps数据集上实现最先进性能，验证了框架提升LLM解码器推理能力。

## 摘要（原文）

> Automated Audio Captioning aims to describe the semantic content of input audio. Recent works have employed large language models (LLMs) as a text decoder to leverage their reasoning capabilities. However, prior approaches that project audio features into the LLM embedding space without considering cross-modal alignment fail to fully utilize these capabilities. To address this, we propose LAMB, an LLM-based audio captioning framework that bridges the modality gap between audio embeddings and the LLM text embedding space. LAMB incorporates a Cross-Modal Aligner that minimizes Cauchy-Schwarz divergence while maximizing mutual information, yielding tighter alignment between audio and text at both global and token levels. We further design a Two-Stream Adapter that extracts semantically enriched audio embeddings, thereby delivering richer information to the Cross-Modal Aligner. Finally, leveraging the aligned audio embeddings, a proposed Token Guide directly computes scores within the LLM text embedding space to steer the output logits of generated captions. Experimental results confirm that our framework strengthens the reasoning capabilities of the LLM decoder, achieving state-of-the-art performance on AudioCaps.

