---
layout: default
title: Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling
---

# Resolving Blind Inverse Problems under Dynamic Range Compression via Structured Forward Operator Modeling
**arXiv**：[2603.01890v1](https://arxiv.org/abs/2603.01890) · [PDF](https://arxiv.org/pdf/2603.01890.pdf)  
**作者**：Muyu Liu, Xuanyu Tian, Chenhe Du, Qing Wu, Hongjiang Wei, Yuyao Zhang  

**一句话要点**：提出CaMB-Diff方法，通过结构化前向算子建模解决未知动态范围压缩下的盲逆问题。

**关键词**：盲逆问题, 动态范围压缩, 单调性建模, 扩散模型, 零样本学习, 辐射保真度恢复

## 3 点简述
- 核心问题：未知动态范围压缩导致前向模型未知和信息损失，恢复辐射保真度是挑战。
- 方法要点：利用单调性作为物理不变量，设计CaMB算子参数化前向模型，结合扩散模型作为几何先验。
- 实验或效果：在零样本任务中，CaMB-Diff在信号保真度和物理一致性上优于现有方法。

## 摘要（原文）

> Recovering radiometric fidelity from unknown dynamic range compression (UDRC), such as low-light enhancement and HDR reconstruction, is a challenging blind inverse problem, due to the unknown forward model and irreversible information loss introduced by compression. To address this challenge, we first identify monotonicity as the fundamental physical invariant shared across UDRC tasks. Leveraging this insight, we introduce the \textbf{cascaded monotonic Bernstein} (CaMB) operator to parameterize the unknown forward model. CaMB enforces monotonicity as a hard architectural inductive bias, constraining optimization to physically consistent mappings and enabling robust and stable operator estimation. We further integrate CaMB with a plug-and-play diffusion framework, proposing \textbf{CaMB-Diff}. Within this framework, the diffusion model serves as a powerful geometric prior for structural and semantic recovery, while CaMB explicitly models and corrects radiometric distortions through a physically grounded forward operator. Extensive experiments on a variety of zero-shot UDRC tasks, including low-light enhancement, low-field MRI enhancement, and HDR reconstruction, demonstrate that CaMB-Diff significantly outperforms state-of-the-art zero-shot baselines in terms of both signal fidelity and physical consistency. Moreover, we empirically validate the effectiveness of the proposed CaMB parameterization in accurately modeling the unknown forward operator.

