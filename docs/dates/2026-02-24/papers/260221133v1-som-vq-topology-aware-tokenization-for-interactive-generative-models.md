---
layout: default
title: SOM-VQ: Topology-Aware Tokenization for Interactive Generative Models
---

# SOM-VQ: Topology-Aware Tokenization for Interactive Generative Models
**arXiv**：[2602.21133v1](https://arxiv.org/abs/2602.21133) · [PDF](https://arxiv.org/pdf/2602.21133.pdf)  
**作者**：Alessandro Londei, Denise Lanzieri, Matteo Benati  

**一句话要点**：提出SOM-VQ方法，结合自组织映射与向量量化，为交互式生成模型提供拓扑感知的离散表示。

**关键词**：向量量化, 自组织映射, 离散表示, 交互生成, 拓扑感知, 人体运动生成

## 3 点简述
- 标准向量量化缺乏语义结构，限制可解释的人机交互控制。
- SOM-VQ通过拓扑感知更新学习低维网格，使邻近令牌对应语义相似状态。
- 在人体运动生成中验证，支持基于网格的采样实现可控发散与收敛。

## 摘要（原文）

> Vector-quantized representations enable powerful discrete generative models but lack semantic structure in token space, limiting interpretable human control. We introduce SOM-VQ, a tokenization method that combines vector quantization with Self-Organizing Maps to learn discrete codebooks with explicit low-dimensional topology. Unlike standard VQ-VAE, SOM-VQ uses topology-aware updates that preserve neighborhood structure: nearby tokens on a learned grid correspond to semantically similar states, enabling direct geometric manipulation of the latent space. We demonstrate that SOM-VQ produces more learnable token sequences in the evaluated domains while providing an explicit navigable geometry in code space. Critically, the topological organization enables intuitive human-in-the-loop control: users can steer generation by manipulating distances in token space, achieving semantic alignment without frame-level constraints. We focus on human motion generation - a domain where kinematic structure, smooth temporal continuity, and interactive use cases (choreography, rehabilitation, HCI) make topology-aware control especially natural - demonstrating controlled divergence and convergence from reference sequences through simple grid-based sampling. SOM-VQ provides a general framework for interpretable discrete representations applicable to music, gesture, and other interactive generative domains.

