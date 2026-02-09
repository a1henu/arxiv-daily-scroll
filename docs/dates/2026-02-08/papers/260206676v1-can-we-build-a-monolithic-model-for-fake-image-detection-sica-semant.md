---
layout: default
title: Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction
---

# Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction
**arXiv**：[2602.06676v1](https://arxiv.org/abs/2602.06676) · [PDF](https://arxiv.org/pdf/2602.06676.pdf)  
**作者**：Bo Du, Xiaochen Ma, Xuekang Zhu, Zhe Yang, Chaogun Niu, Jian Liu, Ji-Zhe Zhou  

**一句话要点**：提出SICA方法，通过语义诱导约束适应重构统一且可区分的伪造图像检测特征空间

**关键词**：伪造图像检测, 特征空间重构, 语义诱导, 单一模型, 异构现象, OpenMMSec数据集

## 3 点简述
- 核心问题：异构现象导致伪造图像检测中单一模型性能不佳，特征空间崩溃
- 方法要点：利用高层语义作为结构先验，设计语义诱导约束适应范式重构特征空间
- 实验或效果：在OpenMMSec数据集上超越15种先进方法，验证假设并实现近正交重构

## 摘要（原文）

> Fake Image Detection (FID), aiming at unified detection across four image forensic subdomains, is critical in real-world forensic scenarios. Compared with ensemble approaches, monolithic FID models are theoretically more promising, but to date, consistently yield inferior performance in practice. In this work, by discovering the ``heterogeneous phenomenon'', which is the intrinsic distinctness of artifacts across subdomains, we diagnose the cause of this underperformance for the first time: the collapse of the artifact feature space driven by such phenomenon. The core challenge for developing a practical monolithic FID model thus boils down to the ``unified-yet-discriminative" reconstruction of the artifact feature space. To address this paradoxical challenge, we hypothesize that high-level semantics can serve as a structural prior for the reconstruction, and further propose Semantic-Induced Constrained Adaptation (SICA), the first monolithic FID paradigm. Extensive experiments on our OpenMMSec dataset demonstrate that SICA outperforms 15 state-of-the-art methods and reconstructs the target unified-yet-discriminative artifact feature space in a near-orthogonal manner, thus firmly validating our hypothesis. The code and dataset are available at:https: //github.com/scu-zjz/SICA_OpenMMSec.

