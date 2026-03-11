---
layout: default
title: The Radio-Frequency Transformer for Signal Separation
---

# The Radio-Frequency Transformer for Signal Separation
**arXiv**：[2603.09201v1](https://arxiv.org/abs/2603.09201) · [PDF](https://arxiv.org/pdf/2603.09201.pdf)  
**作者**：Egor Lifar, Semyon Savkin, Rachana Madhukara, Tejas Jayashankar, Yury Polyanskiy, Gregory W. Wornell  

**一句话要点**：提出基于Transformer的射频信号分离方法，通过交叉熵损失和量化器改进实现数据驱动分离。

**关键词**：信号分离, Transformer, 量化器, 交叉熵损失, 射频信号, 数据驱动建模

## 3 点简述
- 研究信号分离问题，估计受未知非高斯背景干扰的信号。
- 采用改进的SoundStream量化器和Transformer架构，以交叉熵损失训练。
- 在MIT RF数据集上验证，性能优于现有方法，并展示零样本泛化能力。

## 摘要（原文）

> We study a problem of signal separation: estimating a signal of interest (SOI) contaminated by an unknown non-Gaussian background/interference. Given the training data consisting of examples of SOI and interference, we show how to build a fully data-driven signal separator. To that end we learn a good discrete tokenizer for SOI and then train an end-to-end transformer on a cross-entropy loss. Training with a cross-entropy shows substantial improvements over the conventional mean-squared error (MSE). Our tokenizer is a modification of Google's SoundStream, which incorporates additional transformer layers and switches from VQVAE to finite-scalar quantization (FSQ). Across real and synthetic mixtures from the MIT RF Challenge dataset, our method achieves competitive performance, including a 122x reduction in bit-error rate (BER) over prior state-of-the-art techniques for separating a QPSK signal from 5G interference. The learned representation adapts to the interference type without side information and shows zero-shot generalization to unseen mixtures at inference time, underscoring its potential beyond RF. Although we instantiate our approach on radio-frequency mixtures, we expect the same architecture to apply to gravitational-wave data (e.g., LIGO strain) and other scientific sensing problems that require data-driven modeling of background and noise.

