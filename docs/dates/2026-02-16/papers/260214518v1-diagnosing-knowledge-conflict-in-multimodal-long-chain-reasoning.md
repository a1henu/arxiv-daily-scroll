---
layout: default
title: Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning
---

# Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning
**arXiv**：[2602.14518v1](https://arxiv.org/abs/2602.14518) · [PDF](https://arxiv.org/pdf/2602.14518.pdf)  
**作者**：Jing Tang, Kun Wang, Haolang Lu, Hongjin Chen, KaiTao Chen, Zhongxiang Sun, Qiankun Li, Lingjuan Lyu, Guoshun Nan, Zhigang Zeng  

**一句话要点**：提出知识冲突诊断框架，以解决多模态长链推理中的失败问题。

**关键词**：多模态推理, 知识冲突, 长链推理, 内部表示分析, 模型诊断

## 3 点简述
- 核心问题：多模态大语言模型在长链推理中因知识源冲突而失败。
- 方法要点：通过探测内部表示，揭示冲突的线性可分性、深度定位等机制。
- 实验或效果：发现强化模型隐式源偏好比强制相反源更容易，支持诊断与控制。

## 摘要（原文）

> Multimodal large language models (MLLMs) in long chain-of-thought reasoning often fail when different knowledge sources provide conflicting signals. We formalize these failures under a unified notion of knowledge conflict, distinguishing input-level objective conflict from process-level effective conflict. Through probing internal representations, we reveal that: (I) Linear Separability: different conflict types are explicitly encoded as linearly separable features rather than entangled; (II) Depth Localization: conflict signals concentrate in mid-to-late layers, indicating a distinct processing stage for conflict encoding; (III) Hierarchical Consistency: aggregating noisy token-level signals along trajectories robustly recovers input-level conflict types; and (IV) Directional Asymmetry: reinforcing the model's implicit source preference under conflict is far easier than enforcing the opposite source. Our findings provide a mechanism-level view of multimodal reasoning under knowledge conflict and enable principled diagnosis and control of long-CoT failures.

