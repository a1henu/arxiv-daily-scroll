---
layout: default
title: Scaling Speech Tokenizers with Diffusion Autoencoders
---

# Scaling Speech Tokenizers with Diffusion Autoencoders
**arXiv**：[2602.06602v1](https://arxiv.org/abs/2602.06602) · [PDF](https://arxiv.org/pdf/2602.06602.pdf)  
**作者**：Yuancheng Wang, Zhenyu Tang, Yun Wang, Arthur Hinsvark, Yingru Liu, Yinghao Li, Kainan Peng, Junyi Ao, Mingbo Ma, Mike Seltzer, Qing He, Xubo Liu  

**一句话要点**：提出Speech Diffusion Tokenizer以解决语音分词器在语义编码与声学重建间的权衡及低比特率挑战。

**关键词**：语音分词器, 扩散自编码器, 语义编码, 音频重建, 低比特率, 大规模训练

## 3 点简述
- 现有语音分词器面临语义编码与声学重建的权衡及低比特率挑战。
- 基于扩散自编码器，联合学习语义表示并实现高保真音频重建。
- 在1.6B参数和200万小时数据上训练，在理解、重建和生成任务中表现优异，比特率200bps，分词率12.5Hz。

## 摘要（原文）

> Speech tokenizers are foundational to speech language models, yet existing approaches face two major challenges: (1) balancing trade-offs between encoding semantics for understanding and acoustics for reconstruction, and (2) achieving low bit rates and low token rates. We propose Speech Diffusion Tokenizer (SiTok), a diffusion autoencoder that jointly learns semantic-rich representations through supervised learning and enables high-fidelity audio reconstruction with diffusion. We scale SiTok to 1.6B parameters and train it on 2 million hours of speech. Experiments show that SiTok outperforms strong baselines on understanding, reconstruction and generation tasks, at an extremely low token rate of $12.5$ Hz and a bit-rate of 200 bits-per-second.

