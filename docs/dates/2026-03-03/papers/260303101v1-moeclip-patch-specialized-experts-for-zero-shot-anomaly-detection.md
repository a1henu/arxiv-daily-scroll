---
layout: default
title: MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection
---

# MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection
**arXiv**：[2603.03101v1](https://arxiv.org/abs/2603.03101) · [PDF](https://arxiv.org/pdf/2603.03101.pdf)  
**作者**：Jun Yeong Park, JunYoung Seo, Minji Kang, Yu Rang Park  

**一句话要点**：提出MoECLIP，通过专家混合架构实现零样本异常检测的补丁级自适应。

**关键词**：零样本异常检测, 专家混合架构, 补丁级自适应, 低秩适应, 特征正交分离, 等角紧框架损失

## 3 点简述
- 核心问题：现有零样本异常检测方法采用补丁无关设计，无法处理补丁的独特特性。
- 方法要点：引入MoE架构，动态路由补丁到专用LoRA专家，并采用FOFS和ETF损失防止专家冗余。
- 实验或效果：在14个工业和医学基准数据集上超越现有方法，代码已开源。

## 摘要（原文）

> The CLIP model's outstanding generalization has driven recent success in Zero-Shot Anomaly Detection (ZSAD) for detecting anomalies in unseen categories. The core challenge in ZSAD is to specialize the model for anomaly detection tasks while preserving CLIP's powerful generalization capability. Existing approaches attempting to solve this challenge share the fundamental limitation of a patch-agnostic design that processes all patches monolithically without regard for their unique characteristics. To address this limitation, we propose \textbf{MoECLIP}, a Mixture-of-Experts (MoE) architecture for the ZSAD task, which achieves patch-level adaptation by dynamically routing each image patch to a specialized Low-Rank Adaptation (LoRA) expert based on its unique characteristics. Furthermore, to prevent functional redundancy among the LoRA experts, we introduce (1) Frozen Orthogonal Feature Separation (FOFS), which orthogonally separates the input feature space to force experts to focus on distinct information, and (2) a simplex equiangular tight frame (ETF) loss to regulate the expert outputs to form maximally equiangular representations. Comprehensive experimental results across 14 benchmark datasets spanning industrial and medical domains demonstrate that MoECLIP outperforms existing state-of-the-art methods. The code is available at https://github.com/CoCoRessa/MoECLIP.

