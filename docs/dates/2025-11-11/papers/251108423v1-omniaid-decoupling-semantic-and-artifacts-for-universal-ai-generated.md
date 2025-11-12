---
layout: default
title: OmniAID: Decoupling Semantic and Artifacts for Universal AI-Generated Image Detection in the Wild
---

# OmniAID: Decoupling Semantic and Artifacts for Universal AI-Generated Image Detection in the Wild
**arXiv**：[2511.08423v1](https://arxiv.org/abs/2511.08423) · [PDF](https://arxiv.org/pdf/2511.08423.pdf)  
**作者**：Yuncheng Guo, Junyan Ye, Chenjue Zhang, Hengrui Kang, Haohuan Fu, Conghui He, Weijia Li  

**一句话要点**：提出OmniAID框架，通过解耦语义与伪影实现通用AI生成图像检测

**关键词**：AI生成图像检测, 混合专家架构, 语义解耦, 通用伪影, 大规模数据集, 鲁棒泛化

## 3 点简述
- 当前AI生成图像检测方法泛化性差，因语义与伪影特征纠缠且基准过时
- 采用解耦混合专家架构，分离内容相关缺陷与通用伪影，提升鲁棒性
- 实验显示在传统基准和新数据集Mirage上优于现有方法，验证通用性

## 摘要（原文）

> A truly universal AI-Generated Image (AIGI) detector must simultaneously generalize across diverse generative models and varied semantic content. Current state-of-the-art methods learn a single, entangled forgery representation--conflating content-dependent flaws with content-agnostic artifacts--and are further constrained by outdated benchmarks. To overcome these limitations, we propose OmniAID, a novel framework centered on a decoupled Mixture-of-Experts (MoE) architecture. The core of our method is a hybrid expert system engineered to decouple: (1) semantic flaws across distinct content domains, and (2) these content-dependent flaws from content-agnostic universal artifacts. This system employs a set of Routable Specialized Semantic Experts, each for a distinct domain (e.g., human, animal), complemented by a Fixed Universal Artifact Expert. This architecture is trained using a bespoke two-stage strategy: we first train the experts independently with domain-specific hard-sampling to ensure specialization, and subsequently train a lightweight gating network for effective input routing. By explicitly decoupling "what is generated" (content-specific flaws) from "how it is generated" (universal artifacts), OmniAID achieves robust generalization. To address outdated benchmarks and validate real-world applicability, we introduce Mirage, a new large-scale, contemporary dataset. Extensive experiments, using both traditional benchmarks and our Mirage dataset, demonstrate our model surpasses existing monolithic detectors, establishing a new, robust standard for AIGI authentication against modern, in-the-wild threats.

