---
layout: default
title: Federated Latent Space Alignment for Multi-user Semantic Communications
---

# Federated Latent Space Alignment for Multi-user Semantic Communications
**arXiv**：[2602.17271v1](https://arxiv.org/abs/2602.17271) · [PDF](https://arxiv.org/pdf/2602.17271.pdf)  
**作者**：Giuseppe Di Poce, Mario Edoardo Pandolfo, Emilio Calvanese Strinati, Paolo Di Lorenzo  

**一句话要点**：提出联邦潜在空间对齐方法以解决多用户语义通信中的语义不匹配问题

**关键词**：语义通信, 联邦学习, 潜在空间对齐, 多用户系统, 任务导向通信

## 3 点简述
- 核心问题：AI原生设备潜在表示差异导致语义不匹配，阻碍任务执行
- 方法要点：通过联邦优化训练AP和用户端的语义均衡器，实现潜在空间对齐
- 实验或效果：数值结果验证了准确性、通信开销、复杂度和语义邻近度之间的权衡

## 摘要（原文）

> Semantic communication aims to convey meaning for effective task execution, but differing latent representations in AI-native devices can cause semantic mismatches that hinder mutual understanding. This paper introduces a novel approach to mitigating latent space misalignment in multi-agent AI- native semantic communications. In a downlink scenario, we consider an access point (AP) communicating with multiple users to accomplish a specific AI-driven task. Our method implements a protocol that shares a semantic pre-equalizer at the AP and local semantic equalizers at user devices, fostering mutual understanding and task-oriented communication while considering power and complexity constraints. To achieve this, we employ a federated optimization for the decentralized training of the semantic equalizers at the AP and user sides. Numerical results validate the proposed approach in goal-oriented semantic communication, revealing key trade-offs among accuracy, com- munication overhead, complexity, and the semantic proximity of AI-native communication devices.

