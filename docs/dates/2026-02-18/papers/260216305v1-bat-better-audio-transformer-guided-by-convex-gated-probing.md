---
layout: default
title: BAT: Better Audio Transformer Guided by Convex Gated Probing
---

# BAT: Better Audio Transformer Guided by Convex Gated Probing
**arXiv**：[2602.16305v1](https://arxiv.org/abs/2602.16305) · [PDF](https://arxiv.org/pdf/2602.16305.pdf)  
**作者**：Houtan Ghaffari, Lukas Rauch, Christoph Scholz, Paul Devos  

**一句话要点**：提出凸门控探测以解决音频自监督学习中探测与微调性能差距问题，并基于此改进音频Transformer模型。

**关键词**：音频自监督学习, 凸门控探测, 音频Transformer, 模型评估, 预训练优化

## 3 点简述
- 音频自监督学习依赖微调评估，但简单探测方法无法充分挖掘模型潜力且改变模型排名。
- 引入凸门控探测，通过门控机制高效利用冻结层，缩小探测与微调性能差距。
- 基于凸门控探测指导，改进数据预处理、模型架构和预训练流程，提出BAT模型并在音频基准上取得新SOTA。

## 摘要（原文）

> Probing is widely adopted in computer vision to faithfully evaluate self-supervised learning (SSL) embeddings, as fine-tuning may misrepresent their inherent quality. In contrast, audio SSL models still rely on fine-tuning because simple probing fails to unlock their full potential and alters their rankings when competing for SOTA on AudioSet. Hence, a robust and efficient probing mechanism is required to guide the trajectory of audio SSL towards reliable and reproducible methods. We introduce Convex Gated Probing (CGP), a prototype-based method that drastically closes the gap between fine-tuning and probing in audio. CGP efficiently utilizes all frozen layers via a gating mechanism and exposes the location of latent task-relevant information. Guided by CGP, we rework the entire SSL pipeline of current SOTA audio models that use legacy implementations of prior SSL methods. By refining data preprocessing, model architecture, and pre-training recipe, we introduce Better Audio Transformer (BAT), and establish new SOTA on audio benchmarks.

