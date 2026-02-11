---
layout: default
title: A Behavioral Fingerprint for Large Language Models: Provenance Tracking via Refusal Vectors
---

# A Behavioral Fingerprint for Large Language Models: Provenance Tracking via Refusal Vectors
**arXiv**：[2602.09434v1](https://arxiv.org/abs/2602.09434) · [PDF](https://arxiv.org/pdf/2602.09434.pdf)  
**作者**：Zhenyu Xu, Victor S. Sheng  

**一句话要点**：提出基于拒绝向量的行为指纹框架，用于大语言模型溯源以保护知识产权。

**关键词**：大语言模型, 知识产权保护, 行为指纹, 拒绝向量, 模型溯源, 安全对齐

## 3 点简述
- 核心问题：大语言模型知识产权保护面临未授权衍生模型泛滥的挑战。
- 方法要点：利用安全对齐诱导的行为模式，从内部表示中提取拒绝向量作为行为指纹。
- 实验或效果：在76个衍生模型上实现100%准确识别，指纹对微调、合并和量化具有鲁棒性。

## 摘要（原文）

> Protecting the intellectual property of large language models (LLMs) is a critical challenge due to the proliferation of unauthorized derivative models. We introduce a novel fingerprinting framework that leverages the behavioral patterns induced by safety alignment, applying the concept of refusal vectors for LLM provenance tracking. These vectors, extracted from directional patterns in a model's internal representations when processing harmful versus harmless prompts, serve as robust behavioral fingerprints. Our contribution lies in developing a fingerprinting system around this concept and conducting extensive validation of its effectiveness for IP protection. We demonstrate that these behavioral fingerprints are highly robust against common modifications, including finetunes, merges, and quantization. Our experiments show that the fingerprint is unique to each model family, with low cosine similarity between independently trained models. In a large-scale identification task across 76 offspring models, our method achieves 100\% accuracy in identifying the correct base model family. Furthermore, we analyze the fingerprint's behavior under alignment-breaking attacks, finding that while performance degrades significantly, detectable traces remain. Finally, we propose a theoretical framework to transform this private fingerprint into a publicly verifiable, privacy-preserving artifact using locality-sensitive hashing and zero-knowledge proofs.

