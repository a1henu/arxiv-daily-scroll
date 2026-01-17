---
layout: default
title: PID-Guided Partial Alignment for Multimodal Decentralized Federated Learning
---

# PID-Guided Partial Alignment for Multimodal Decentralized Federated Learning
**arXiv**：[2601.10012v1](https://arxiv.org/abs/2601.10012) · [PDF](https://arxiv.org/pdf/2601.10012.pdf)  
**作者**：Yanhang Shi, Xiaoyu Wang, Houwei Cao, Jian Li, Yong Liu  

**一句话要点**：提出PARSE框架，通过部分信息分解和切片级对齐解决多模态去中心化联邦学习中的梯度冲突问题。

**关键词**：多模态联邦学习, 去中心化学习, 部分信息分解, 梯度对齐, 异构代理, 知识共享

## 3 点简述
- 多模态去中心化联邦学习中，异构代理的模态和架构差异导致梯度错位，抑制知识共享。
- PARSE利用部分信息分解将特征分为冗余、独特和协同切片，实现切片级部分对齐以促进P2P知识交换。
- 实验表明PARSE在基准测试中优于基线方法，并通过消融研究验证了设计的效率和鲁棒性。

## 摘要（原文）

> Multimodal decentralized federated learning (DFL) is challenging because agents differ in available modalities and model architectures, yet must collaborate over peer-to-peer (P2P) networks without a central coordinator. Standard multimodal pipelines learn a single shared embedding across all modalities. In DFL, such a monolithic representation induces gradient misalignment between uni- and multimodal agents; as a result, it suppresses heterogeneous sharing and cross-modal interaction. We present PARSE, a multimodal DFL framework that operationalizes partial information decomposition (PID) in a server-free setting. Each agent performs feature fission to factorize its latent representation into redundant, unique, and synergistic slices. P2P knowledge sharing among heterogeneous agents is enabled by slice-level partial alignment: only semantically shareable branches are exchanged among agents that possess the corresponding modality. By removing the need for central coordination and gradient surgery, PARSE resolves uni-/multimodal gradient conflicts, thereby overcoming the multimodal DFL dilemma while remaining compatible with standard DFL constraints. Across benchmarks and agent mixes, PARSE yields consistent gains over task-, modality-, and hybrid-sharing DFL baselines. Ablations on fusion operators and split ratios, together with qualitative visualizations, further demonstrate the efficiency and robustness of the proposed design.

