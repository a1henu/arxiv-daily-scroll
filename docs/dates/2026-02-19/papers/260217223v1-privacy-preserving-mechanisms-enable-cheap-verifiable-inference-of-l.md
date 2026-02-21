---
layout: default
title: Privacy-Preserving Mechanisms Enable Cheap Verifiable Inference of LLMs
---

# Privacy-Preserving Mechanisms Enable Cheap Verifiable Inference of LLMs
**arXiv**：[2602.17223v1](https://arxiv.org/abs/2602.17223) · [PDF](https://arxiv.org/pdf/2602.17223.pdf)  
**作者**：Arka Pal, Louai Zahran, William Gvozdjak, Akilesh Potti, Micah Goldblum  

**一句话要点**：提出基于隐私保护机制的廉价可验证LLM推理协议，以解决第三方托管中的计算保证问题。

**关键词**：隐私保护推理, 可验证计算, 大语言模型, 第三方托管, 计算保证

## 3 点简述
- 核心问题：第三方LLM托管缺乏计算保证，提供商可能用廉价弱模型替代昂贵大模型。
- 方法要点：利用隐私保护推理方法，设计两种协议实现廉价可验证推理，仅需少量额外计算开销。
- 实验或效果：协议计算成本低，对下游任务影响小，验证运行时间优于零知识证明方法。

## 摘要（原文）

> As large language models (LLMs) continue to grow in size, fewer users are able to host and run models locally. This has led to increased use of third-party hosting services. However, in this setting, there is a lack of guarantees on the computation performed by the inference provider. For example, a dishonest provider may replace an expensive large model with a cheaper-to-run weaker model and return the results from the weaker model to the user. Existing tools to verify inference typically rely on methods from cryptography such as zero-knowledge proofs (ZKPs), but these add significant computational overhead, and remain infeasible for use for large models. In this work, we develop a new insight -- that given a method for performing private LLM inference, one can obtain forms of verified inference at marginal extra cost. Specifically, we propose two new protocols which leverage privacy-preserving LLM inference in order to provide guarantees over the inference that was carried out. Our approaches are cheap, requiring the addition of a few extra tokens of computation, and have little to no downstream impact. As the fastest privacy-preserving inference methods are typically faster than ZK methods, the proposed protocols also improve verification runtime. Our work provides novel insights into the connections between privacy and verifiability in LLM inference.

