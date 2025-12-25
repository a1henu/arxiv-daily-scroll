---
layout: default
title: GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model
---

# GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model
**arXiv**：[2512.20978v1](https://arxiv.org/abs/2512.20978) · [PDF](https://arxiv.org/pdf/2512.20978.pdf)  
**作者**：Haoyang Li, Xuyi Zhuang, Azmat Adnan, Ye Ni, Wei Rao, Shreyas Gopal, Eng Siong Chng  

**一句话要点**：提出GenTSE，通过两阶段生成语言模型增强目标说话人提取，提升语音质量和一致性。

**关键词**：目标说话人提取, 生成语言模型, 两阶段解码, 冻结LM条件, DPO优化, 语音增强

## 3 点简述
- 核心问题：基于语言模型的目标说话人提取在泛化性和高保真语音方面存在挑战。
- 方法要点：采用两阶段解码器，先预测粗粒度语义令牌，再生成细粒度声学令牌，结合冻结LM条件和DPO优化。
- 实验或效果：在Libri2Mix数据集上，GenTSE在语音质量、可懂度和说话人一致性方面优于先前系统。

## 摘要（原文）

> Language Model (LM)-based generative modeling has emerged as a promising direction for TSE, offering potential for improved generalization and high-fidelity speech. We present GenTSE, a two-stage decoder-only generative LM approach for TSE: Stage-1 predicts coarse semantic tokens, and Stage-2 generates fine acoustic tokens. Separating semantics and acoustics stabilizes decoding and yields more faithful, content-aligned target speech. Both stages use continuous SSL or codec embeddings, offering richer context than discretized-prompt methods. To reduce exposure bias, we employ a Frozen-LM Conditioning training strategy that conditions the LMs on predicted tokens from earlier checkpoints to reduce the gap between teacher-forcing training and autoregressive inference. We further employ DPO to better align outputs with human perceptual preferences. Experiments on Libri2Mix show that GenTSE surpasses previous LM-based systems in speech quality, intelligibility, and speaker consistency.

