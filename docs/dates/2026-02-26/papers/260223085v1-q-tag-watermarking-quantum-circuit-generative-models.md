---
layout: default
title: Q-Tag: Watermarking Quantum Circuit Generative Models
---

# Q-Tag: Watermarking Quantum Circuit Generative Models
**arXiv**：[2602.23085v1](https://arxiv.org/abs/2602.23085) · [PDF](https://arxiv.org/pdf/2602.23085.pdf)  
**作者**：Yang Yang, Yuzhu Long, Han Fang, Zhaoyun Chen, Zhonghui Li, Weiming Zhang, Guoping Guo  

**一句话要点**：提出Q-Tag框架以保护量子电路生成模型的知识产权

**关键词**：量子电路生成模型, 数字水印, 知识产权保护, 对称采样, 同步机制, 量子云安全

## 3 点简述
- 量子云平台中电路面临未授权访问风险，现有水印方法不适用于生成模型
- 集成对称采样和同步机制，在生成过程中嵌入水印并保持电路保真度
- 实验验证方法在多种扰动下实现高保真生成和鲁棒水印检测

## 摘要（原文）

> Quantum cloud platforms have become the most widely adopted and mainstream approach for accessing quantum computing resources, due to the scarcity and operational complexity of quantum hardware. In this service-oriented paradigm, quantum circuits, which constitute high-value intellectual property, are exposed to risks of unauthorized access, reuse, and misuse. Digital watermarking has been explored as a promising mechanism for protecting quantum circuits by embedding ownership information for tracing and verification. However, driven by recent advances in generative artificial intelligence, the paradigm of quantum circuit design is shifting from individually and manually constructed circuits to automated synthesis based on quantum circuit generative models (QCGMs). In such generative settings, protecting only individual output circuits is insufficient, and existing post hoc, circuit-centric watermarking methods are not designed to integrate with the generative process, often failing to simultaneously ensure stealthiness, functional correctness, and robustness at scale. These limitations highlight the need for a new watermarking paradigm that is natively integrated with quantum circuit generative models. In this work, we present the first watermarking framework for QCGMs, which embeds ownership signals into the generation process while preserving circuit fidelity. We introduce a symmetric sampling strategy that aligns watermark encoding with the model's Gaussian prior, and a synchronization mechanism that counteracts adversarial watermark attack through latent drift correction. Empirical results confirm that our method achieves high-fidelity circuit generation and robust watermark detection across a range of perturbations, paving the way for scalable, secure copyright protection in AI-powered quantum design.

