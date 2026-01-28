---
layout: default
title: LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment
---

# LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment
**arXiv**：[2601.19487v1](https://arxiv.org/abs/2601.19487) · [PDF](https://arxiv.org/pdf/2601.19487.pdf)  
**作者**：Haonan Zhang, Dongxia Wang, Yi Liu, Kexin Chen, Wenhai Wang  

**一句话要点**：提出LLM-VA通过向量对齐解决安全对齐LLM的越狱与过度拒绝权衡问题

**关键词**：向量对齐, 安全对齐, 越狱缓解, 过度拒绝减少, 闭式更新, LLM安全

## 3 点简述
- 核心问题：安全对齐LLM存在越狱（回答有害输入）和过度拒绝（拒绝良性查询）的权衡，源于回答向量与安全向量正交。
- 方法要点：通过闭式权重更新对齐回答向量与安全向量，无需微调或架构改动，使回答意愿因果依赖于安全评估。
- 实验效果：在12个LLM上，LLM-VA比最佳基线F1提高11.45%，保持95.92%实用性，自动适应模型安全偏差。

## 摘要（原文）

> Safety-aligned LLMs suffer from two failure modes: jailbreak (answering harmful inputs) and over-refusal (declining benign queries). Existing vector steering methods adjust the magnitude of answer vectors, but this creates a fundamental trade-off -- reducing jailbreak increases over-refusal and vice versa. We identify the root cause: LLMs encode the decision to answer (answer vector $v_a$) and the judgment of input safety (benign vector $v_b$) as nearly orthogonal directions, treating them as independent processes. We propose LLM-VA, which aligns $v_a$ with $v_b$ through closed-form weight updates, making the model's willingness to answer causally dependent on its safety assessment -- without fine-tuning or architectural changes. Our method identifies vectors at each layer using SVMs, selects safety-relevant layers, and iteratively aligns vectors via minimum-norm weight modifications. Experiments on 12 LLMs demonstrate that LLM-VA achieves 11.45% higher F1 than the best baseline while preserving 95.92% utility, and automatically adapts to each model's safety bias without manual tuning. Code and models are available at https://hotbento.github.io/LLM-VA-Web/.

