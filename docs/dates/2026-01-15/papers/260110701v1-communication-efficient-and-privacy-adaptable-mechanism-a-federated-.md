---
layout: default
title: Communication-Efficient and Privacy-Adaptable Mechanism -- a Federated Learning Scheme with Convergence Analysis
---

# Communication-Efficient and Privacy-Adaptable Mechanism -- a Federated Learning Scheme with Convergence Analysis
**arXiv**：[2601.10701v1](https://arxiv.org/abs/2601.10701) · [PDF](https://arxiv.org/pdf/2601.10701.pdf)  
**作者**：Chun Hei Michael Shiu, Chih Wei Ling  

**一句话要点**：提出通信高效与隐私可调机制，以解决联邦学习中的通信效率和隐私保护问题。

**关键词**：联邦学习, 通信效率, 隐私保护, 量化器, 收敛分析, 隐私权衡

## 3 点简述
- 核心问题：联邦学习面临通信效率低和参与者间隐私保护不足的挑战。
- 方法要点：利用拒绝采样通用量化器，量化误差等效于预设噪声，可定制隐私保护。
- 实验或效果：理论分析隐私保证和收敛性，实验评估收敛曲线和准确率-隐私权衡。

## 摘要（原文）

> Federated learning enables multiple parties to jointly train learning models without sharing their own underlying data, offering a practical pathway to privacy-preserving collaboration under data-governance constraints. Continued study of federated learning is essential to address key challenges in it, including communication efficiency and privacy protection between parties. A recent line of work introduced a novel approach called the Communication-Efficient and Privacy-Adaptable Mechanism (CEPAM), which achieves both objectives simultaneously. CEPAM leverages the rejection-sampled universal quantizer (RSUQ), a randomized vector quantizer whose quantization error is equivalent to a prescribed noise, which can be tuned to customize privacy protection between parties. In this work, we theoretically analyze the privacy guarantees and convergence properties of CEPAM. Moreover, we assess CEPAM's utility performance through experimental evaluations, including convergence profiles compared with other baselines, and accuracy-privacy trade-offs between different parties.

