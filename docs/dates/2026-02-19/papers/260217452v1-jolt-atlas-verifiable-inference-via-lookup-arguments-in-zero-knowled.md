---
layout: default
title: Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge
---

# Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge
**arXiv**：[2602.17452v1](https://arxiv.org/abs/2602.17452) · [PDF](https://arxiv.org/pdf/2602.17452.pdf)  
**作者**：Wyatt Benno, Alberto Centelles, Antoine Douchet, Khalil Gibran  

**一句话要点**：提出Jolt Atlas零知识机器学习框架，通过查找参数实现可验证推理，适用于隐私和对抗环境。

**关键词**：零知识机器学习, 可验证推理, 查找参数, ONNX张量操作, 隐私保护

## 3 点简述
- 核心问题：现有zkML框架在模型推理验证中面临效率低和硬件依赖问题。
- 方法要点：基于Jolt证明系统，直接应用ONNX张量操作，利用查找参数和优化技术如神经传送。
- 实验或效果：在分类、嵌入、自动推理和小语言模型上展示实用证明时间，支持内存受限环境。

## 摘要（原文）

> We present Jolt Atlas, a zero-knowledge machine learning (zkML) framework that extends the Jolt proving system to model inference. Unlike zkVMs (zero-knowledge virtual machines), which emulate CPU instruction execution, Jolt Atlas adapts Jolt's lookup-centric approach and applies it directly to ONNX tensor operations. The ONNX computational model eliminates the need for CPU registers and simplifies memory consistency verification. In addition, ONNX is an open-source, portable format, which makes it easy to share and deploy models across different frameworks, hardware platforms, and runtime environments without requiring framework-specific conversions.
>   Our lookup arguments, which use sumcheck protocol, are well-suited for non-linear functions -- key building blocks in modern ML. We apply optimisations such as neural teleportation to reduce the size of lookup tables while preserving model accuracy, as well as several tensor-level verification optimisations detailed in this paper. We demonstrate that Jolt Atlas can prove model inference in memory-constrained environments -- a prover property commonly referred to as \textit{streaming}. Furthermore, we discuss how Jolt Atlas achieves zero-knowledge through the BlindFold technique, as introduced in Vega. In contrast to existing zkML frameworks, we show practical proving times for classification, embedding, automated reasoning, and small language models.
>   Jolt Atlas enables cryptographic verification that can be run on-device, without specialised hardware. The resulting proofs are succinctly verifiable. This makes Jolt Atlas well-suited for privacy-centric and adversarial environments. In a companion work, we outline various use cases of Jolt Atlas, including how it serves as guardrails in agentic commerce and for trustless AI context (often referred to as \textit{AI memory}).

