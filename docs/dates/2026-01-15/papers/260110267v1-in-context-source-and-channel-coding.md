---
layout: default
title: In-Context Source and Channel Coding
---

# In-Context Source and Channel Coding
**arXiv**：[2601.10267v1](https://arxiv.org/abs/2601.10267) · [PDF](https://arxiv.org/pdf/2601.10267.pdf)  
**作者**：Ziqiong Wang, Tianqi Ren, Rongpeng Li, Zhifeng Zhao, Honggang Zhang  

**一句话要点**：提出接收端上下文解码框架以增强分离源信道编码在低信噪比下的鲁棒性

**关键词**：分离源信道编码, 上下文解码, 错误校正码变换器, 大语言模型, 算术编码, 信道编码

## 3 点简述
- 分离源信道编码在低信噪比下易受悬崖效应影响，导致无损源解码失败
- 利用错误校正码变换器获取比特可靠性，通过可靠性引导比特翻转构建候选池，结合大语言模型算术解码器进行选择
- 在加性高斯白噪声和瑞利衰落信道实验中，相比传统分离源信道编码和联合源信道编码方案，表现出稳定性能提升

## 摘要（原文）

> Separate Source-Channel Coding (SSCC) remains attractive for text transmission due to its modularity and compatibility with mature entropy coders and powerful channel codes. However, SSCC often suffers from a pronounced cliff effect in low Signal-to-Noise Ratio (SNR) regimes, where residual bit errors after channel decoding can catastrophically break lossless source decoding, especially for Arithmetic Coding (AC) driven by Large Language Models (LLMs). This paper proposes a receiver-side In-Context Decoding (ICD) framework that enhances SSCC robustness without modifying the transmitter. ICD leverages an Error Correction Code Transformer (ECCT) to obtain bit-wise reliability for the decoded information bits. Based on the context-consistent bitstream, ICD constructs a confidence-ranked candidate pool via reliability-guided bit flipping, samples a compact yet diverse subset of candidates, and applies an LLM-based arithmetic decoder to obtain both reconstructions and sequence-level log-likelihoods. A reliability-likelihood fusion rule then selects the final output. We further provide theoretical guarantees on the stability and convergence of the proposed sampling procedure. Extensive experiments over Additive White Gaussian Noise (AWGN) and Rayleigh fading channels demonstrate consistent gains compared with conventional SSCC baselines and representative Joint Source-Channel Coding (JSCC) schemes.

