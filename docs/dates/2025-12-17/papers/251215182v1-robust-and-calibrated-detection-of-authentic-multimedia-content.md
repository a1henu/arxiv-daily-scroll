---
layout: default
title: Robust and Calibrated Detection of Authentic Multimedia Content
---

# Robust and Calibrated Detection of Authentic Multimedia Content
**arXiv**：[2512.15182v1](https://arxiv.org/abs/2512.15182) · [PDF](https://arxiv.org/pdf/2512.15182.pdf)  
**作者**：Sarim Hashmi, Abdelrahman Elsayed, Mohammed Talha Alam, Samuele Poppi, Nils Lukas  

**一句话要点**：提出重合成框架以解决深度伪造检测中假阳性率高和对抗鲁棒性差的问题。

**关键词**：深度伪造检测, 对抗鲁棒性, 假阳性率控制, 重合成框架, 多模态验证

## 3 点简述
- 核心问题：深度伪造检测存在假阳性率无界和对抗攻击下鲁棒性不足的挑战。
- 方法要点：采用校准重合成方法验证真实样本，控制假阳性率并提升对抗鲁棒性。
- 实验或效果：在高精度低召回设置下，优于现有方法，支持多模态并利用先进反演技术。

## 摘要（原文）

> Generative models can synthesize highly realistic content, so-called deepfakes, that are already being misused at scale to undermine digital media authenticity. Current deepfake detection methods are unreliable for two reasons: (i) distinguishing inauthentic content post-hoc is often impossible (e.g., with memorized samples), leading to an unbounded false positive rate (FPR); and (ii) detection lacks robustness, as adversaries can adapt to known detectors with near-perfect accuracy using minimal computational resources. To address these limitations, we propose a resynthesis framework to determine if a sample is authentic or if its authenticity can be plausibly denied. We make two key contributions focusing on the high-precision, low-recall setting against efficient (i.e., compute-restricted) adversaries. First, we demonstrate that our calibrated resynthesis method is the most reliable approach for verifying authentic samples while maintaining controllable, low FPRs. Second, we show that our method achieves adversarial robustness against efficient adversaries, whereas prior methods are easily evaded under identical compute budgets. Our approach supports multiple modalities and leverages state-of-the-art inversion techniques.

