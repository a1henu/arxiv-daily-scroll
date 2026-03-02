---
layout: default
title: Quant Experts: Token-aware Adaptive Error Reconstruction with Mixture of Experts for Large Vision-Language Models Quantization
---

# Quant Experts: Token-aware Adaptive Error Reconstruction with Mixture of Experts for Large Vision-Language Models Quantization
**arXiv**：[2602.24059v1](https://arxiv.org/abs/2602.24059) · [PDF](https://arxiv.org/pdf/2602.24059.pdf)  
**作者**：Chenwei Jia, Baoting Li, Xuchong Zhang, Mingzhuo Wei, Bochen Lin, Hongbin Sun  

**一句话要点**：提出Quant Experts，通过令牌感知自适应误差补偿与专家混合，提升大视觉语言模型量化性能。

**关键词**：视觉语言模型量化, 后训练量化, 令牌感知补偿, 专家混合, 低秩适配器

## 3 点简述
- 现有后训练量化方法忽视重要通道在输入间的分布差异，导致量化效果不佳。
- Quant Experts将重要通道分组，使用共享专家补偿全局误差，路由专家补偿令牌相关局部误差。
- 实验表明，该方法在2B至70B参数模型中提升任务精度，接近全精度模型性能。

## 摘要（原文）

> Post-Training Quantization (PTQ) has emerged as an effective technique for alleviating the substantial computational and memory overheads of Vision-Language Models (VLMs) by compressing both weights and activations without retraining the full model. Existing PTQ methods primarily rely on static identification and global compensation of sensitive or outlier channels, yet they often overlook the distributional differences of these important channels across inputs, leading to unsatisfactory quantization. In this work, we observe that the distributions and occurrence frequencies of important channels vary significantly both across modalities and among tokens, even within the same modality. Accordingly, we propose \textbf{Quant Experts (QE)}, a token-aware adaptive error compensation with mixture-of-experts for VLMs quantization. QE divides the important channels into token-independent and token-dependent groups. For the former, a shared expert is designed for most tokens to compensate for global quantization error using a low-rank adapter. For the latter, routed experts including multiple routed low-rank adapters are elaborated to compensate for local quantization error related to specific tokens. Extensive experiments demonstrate that QE consistently enhances task accuracy across various quantization settings and model scales, ranging from 2B to 70B parameters, while maintaining performance comparable to full-precision models.

