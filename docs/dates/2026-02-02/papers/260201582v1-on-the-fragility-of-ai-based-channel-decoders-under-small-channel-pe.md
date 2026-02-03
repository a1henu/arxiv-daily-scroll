---
layout: default
title: On the Fragility of AI-Based Channel Decoders under Small Channel Perturbations
---

# On the Fragility of AI-Based Channel Decoders under Small Channel Perturbations
**arXiv**：[2602.01582v1](https://arxiv.org/abs/2602.01582) · [PDF](https://arxiv.org/pdf/2602.01582.pdf)  
**作者**：Haoyu Lei, Mohammad Jalali, Chin Wa Lau, Farzan Farnia  

**一句话要点**：揭示AI信道解码器在小扰动下的脆弱性，分析其鲁棒性成本

**关键词**：信道解码, 对抗扰动, 鲁棒性分析, 深度学习, AWGN信道, 性能评估

## 3 点简述
- 核心问题：AI解码器在AWGN信道上的性能提升是否以鲁棒性为代价
- 方法要点：评估输入依赖和通用对抗扰动对AI解码器的影响
- 实验或效果：AI解码器在扰动下性能显著下降，对抗扰动在AI解码器间转移性强

## 摘要（原文）

> Recent advances in deep learning have led to AI-based error correction decoders that report empirical performance improvements over traditional belief-propagation (BP) decoding on AWGN channels. While such gains are promising, a fundamental question remains: where do these improvements come from, and what cost is paid to achieve them? In this work, we study this question through the lens of robustness to distributional shifts at the channel output. We evaluate both input-dependent adversarial perturbations (FGM and projected gradient methods under $\ell_2$ constraints) and universal adversarial perturbations that apply a single norm-bounded shift to all received vectors. Our results show that recent AI decoders, including ECCT and CrossMPT, could suffer significant performance degradation under such perturbations, despite superior nominal performance under i.i.d. AWGN. Moreover, adversarial perturbations transfer relatively strongly between AI decoders but weakly to BP-based decoders, and universal perturbations are substantially more harmful than random perturbations of equal norm. These numerical findings suggest a potential robustness cost and higher sensitivity to channel distribution underlying recent AI decoding gains.

