---
layout: default
title: Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression
---

# Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression
**arXiv**：[2602.17063v1](https://arxiv.org/abs/2602.17063) · [PDF](https://arxiv.org/pdf/2602.17063.pdf)  
**作者**：Akira Sakai, Yuma Ichikawa  

**一句话要点**：提出符号锁定理论及初始化与正则化方法，以缓解次比特模型压缩中的符号位瓶颈问题。

**关键词**：模型压缩, 符号锁定, 初始化方法, 正则化, 次比特存储, 权重符号

## 3 点简述
- 次比特模型压缩中，权重符号位成为固定成本瓶颈，难以通过低秩近似压缩。
- 符号矩阵在训练中保持初始化符号，翻转罕见，基于SGD噪声分析提出符号锁定理论。
- 引入间隙初始化和轻量外漂正则化，将有效翻转率降至约10^{-3}，困惑度仅轻微增加。

## 摘要（原文）

> Sub-bit model compression seeks storage below one bit per weight; as magnitudes are aggressively compressed, the sign bit becomes a fixed-cost bottleneck. Across Transformers, CNNs, and MLPs, learned sign matrices resist low-rank approximation and are spectrally indistinguishable from an i.i.d. Rademacher baseline. Despite this apparent randomness, most weights retain their initialization signs; flips primarily occur via rare near-zero boundary crossings, suggesting that sign-pattern randomness is largely inherited from initialization. We formalize this behavior with sign lock-in theory, a stopping-time analysis of sign flips under SGD noise. Under bounded updates and a rare re-entry condition into a small neighborhood around zero, the number of effective sign flips exhibits a geometric tail. Building on this mechanism, we introduce a gap-based initialization and a lightweight outward-drift regularizer, reducing the effective flip rate to approximately $10^{-3}$ with only about a one-point increase in perplexity.

