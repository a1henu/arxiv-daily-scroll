---
layout: default
title: Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification
---

# Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification
**arXiv**：[2603.01511v1](https://arxiv.org/abs/2603.01511) · [PDF](https://arxiv.org/pdf/2603.01511.pdf)  
**作者**：Jiayang Wu, Jiale Zhou, Xingyi Zhang, Xun Lin, Tianxu Lv, Leong Hou U, Rubo Wang, Yefeng Zheng  

**一句话要点**：提出MERA框架，通过检索增强与可靠性感知融合解决蛋白质活性位点识别中的稀疏数据与模态不可靠问题。

**关键词**：蛋白质活性位点识别, 多模态融合, 检索增强, 可靠性感知, Dempster-Shafer证据理论, 分层多专家模型

## 3 点简述
- 核心问题：蛋白质活性位点识别面临训练数据稀疏和模态可靠性估计不足，导致单实例预测脆弱和融合性能下降。
- 方法要点：采用分层多专家检索动态聚合上下文信息，并基于Dempster-Shafer证据理论进行可靠性感知融合，量化模态可信度。
- 实验或效果：在ProTAD-Gen和TS125数据集上实现SOTA性能，活性位点预测AUPRC达90%，肽结合位点识别显著提升。

## 摘要（原文）

> Accurate identification of protein active sites at the residue level is crucial for understanding protein function and advancing drug discovery. However, current methods face two critical challenges: vulnerability in single-instance prediction due to sparse training data, and inadequate modality reliability estimation that leads to performance degradation when unreliable modalities dominate fusion processes. To address these challenges, we introduce Multimodal Mixture-of-Experts with Retrieval Augmentation (MERA), the first retrieval-augmented framework for protein active site identification. MERA employs hierarchical multi-expert retrieval that dynamically aggregates contextual information from chain, sequence, and active-site perspectives through residue-level mixture-of-experts gating. To prevent modality degradation, we propose a reliability-aware fusion strategy based on Dempster-Shafer evidence theory that quantifies modality trustworthiness through belief mass functions and learnable discounting coefficients, enabling principled multimodal integration. Extensive experiments on ProTAD-Gen and TS125 datasets demonstrate that MERA achieves state-of-the-art performance, with 90% AUPRC on active site prediction and significant gains on peptide-binding site identification, validating the effectiveness of retrieval-augmented multi-expert modeling and reliability-guided fusion.

