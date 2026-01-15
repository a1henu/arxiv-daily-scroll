---
layout: default
title: SoK: Enhancing Cryptographic Collaborative Learning with Differential Privacy
---

# SoK: Enhancing Cryptographic Collaborative Learning with Differential Privacy
**arXiv**：[2601.09460v1](https://arxiv.org/abs/2601.09460) · [PDF](https://arxiv.org/pdf/2601.09460.pdf)  
**作者**：Francesco Capano, Jonas Böhler, Benjamin Weggenmann  

**一句话要点**：系统化分析密码学与差分隐私在协作学习中的结合，提出统一框架并评估安全噪声采样技术。

**关键词**：密码学协作学习, 差分隐私, 安全噪声采样, 多方计算, 隐私保护机器学习, 性能评估

## 3 点简述
- 核心问题：密码学协作学习面临隐私-准确性-性能权衡，需高效结合密码学与差分隐私。
- 方法要点：引入统一框架，识别安全噪声采样为关键阶段，分析不同技术与DP机制。
- 实验或效果：在MPC中实现安全噪声采样选项，评估WAN和LAN下的计算与通信成本。

## 摘要（原文）

> In collaborative learning (CL), multiple parties jointly train a machine learning model on their private datasets. However, data can not be shared directly due to privacy concerns. To ensure input confidentiality, cryptographic techniques, e.g., multi-party computation (MPC), enable training on encrypted data. Yet, even securely trained models are vulnerable to inference attacks aiming to extract memorized data from model outputs. To ensure output privacy and mitigate inference attacks, differential privacy (DP) injects calibrated noise during training. While cryptography and DP offer complementary guarantees, combining them efficiently for cryptographic and differentially private CL (CPCL) is challenging. Cryptography incurs performance overheads, while DP degrades accuracy, creating a privacy-accuracy-performance trade-off that needs careful design considerations. This work systematizes the CPCL landscape. We introduce a unified framework that generalizes common phases across CPCL paradigms, and identify secure noise sampling as the foundational phase to achieve CPCL. We analyze trade-offs of different secure noise sampling techniques, noise types, and DP mechanisms discussing their implementation challenges and evaluating their accuracy and cryptographic overhead across CPCL paradigms. Additionally, we implement identified secure noise sampling options in MPC and evaluate their computation and communication costs in WAN and LAN. Finally, we propose future research directions based on identified key observations, gaps and possible enhancements in the literature.

