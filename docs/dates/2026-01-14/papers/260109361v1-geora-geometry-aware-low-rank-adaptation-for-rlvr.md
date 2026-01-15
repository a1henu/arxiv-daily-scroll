---
layout: default
title: GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR
---

# GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR
**arXiv**：[2601.09361v1](https://arxiv.org/abs/2601.09361) · [PDF](https://arxiv.org/pdf/2601.09361.pdf)  
**作者**：Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He  

**一句话要点**：提出GeoRA以解决RLVR中几何结构错配导致的优化不稳定问题

**关键词**：强化学习可验证奖励, 低秩适应, 几何感知优化, 参数高效微调, 奇异值分解, 模型泛化

## 3 点简述
- 现有参数高效方法如PiSSA和MiLoRA针对SFT设计，不适用于RLVR的优化动态和几何结构，导致谱崩溃和优化不稳定。
- GeoRA利用RL更新子空间的各向异性和可压缩性，通过SVD在几何约束子空间中提取主方向初始化适配器，冻结残差组件以保持预训练几何结构。
- 在Qwen和Llama上的实验显示，GeoRA缓解几何错配引起的优化瓶颈，在数学基准上超越低秩基线，实现SOTA结果，并展现优越泛化性和抗灾难性遗忘能力。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is crucial for advancing large-scale reasoning models. However, existing parameter-efficient methods, such as PiSSA and MiLoRA, are designed for Supervised Fine-Tuning (SFT) and do not account for the distinct optimization dynamics and geometric structures of RLVR. Applying these methods directly leads to spectral collapse and optimization instability, which severely limit model performance. Meanwhile, alternative approaches that leverage update sparsity encounter significant efficiency bottlenecks on modern hardware due to unstructured computations. To address these challenges, we propose GeoRA (Geometry-Aware Low-Rank Adaptation), which exploits the anisotropic and compressible nature of RL update subspaces. GeoRA initializes adapters by extracting principal directions via Singular Value Decomposition (SVD) within a geometrically constrained subspace while freezing the residual components. This method preserves the pre-trained geometric structure and enables efficient GPU computation through dense operators. Experiments on Qwen and Llama demonstrate that GeoRA mitigates optimization bottlenecks caused by geometric misalignment. It consistently outperforms established low-rank baselines on key mathematical benchmarks, achieving state-of-the-art (SOTA) results. Moreover, GeoRA shows superior generalization and resilience to catastrophic forgetting in out-of-domain tasks.

