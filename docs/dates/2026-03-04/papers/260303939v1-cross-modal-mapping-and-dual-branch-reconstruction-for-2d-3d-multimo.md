---
layout: default
title: Cross-Modal Mapping and Dual-Branch Reconstruction for 2D-3D Multimodal Industrial Anomaly Detection
---

# Cross-Modal Mapping and Dual-Branch Reconstruction for 2D-3D Multimodal Industrial Anomaly Detection
**arXiv**：[2603.03939v1](https://arxiv.org/abs/2603.03939) · [PDF](https://arxiv.org/pdf/2603.03939.pdf)  
**作者**：Radia Daci, Vito Renò, Cosimo Patruno, Angelo Cardellicchio, Abdelmalik Taleb-Ahmed, Marco Leo, Cosimo Distante  

**一句话要点**：提出CMDR-IAD框架，通过跨模态映射与双分支重建实现2D-3D工业异常检测

**关键词**：工业异常检测, 跨模态映射, 双分支重建, 无监督学习, 多模态融合, 3D视觉

## 3 点简述
- 核心问题：现有无监督方法依赖内存库或脆弱融合，在噪声深度、弱纹理或模态缺失时鲁棒性不足
- 方法要点：结合双向跨模态映射建模外观-几何一致性，以及双分支重建独立捕捉正常纹理与结构
- 实验或效果：在MVTec 3D-AD基准上达到SOTA性能，并在真实工业数据集上验证有效性

## 摘要（原文）

> Multimodal industrial anomaly detection benefits from integrating RGB appearance with 3D surface geometry, yet existing \emph{unsupervised} approaches commonly rely on memory banks, teacher-student architectures, or fragile fusion schemes, limiting robustness under noisy depth, weak texture, or missing modalities. This paper introduces \textbf{CMDR-IAD}, a lightweight and modality-flexible unsupervised framework for reliable anomaly detection in 2D+3D multimodal as well as single-modality (2D-only or 3D-only) settings. \textbf{CMDR-IAD} combines bidirectional 2D$\leftrightarrow$3D cross-modal mapping to model appearance-geometry consistency with dual-branch reconstruction that independently captures normal texture and geometric structure. A two-part fusion strategy integrates these cues: a reliability-gated mapping anomaly highlights spatially consistent texture-geometry discrepancies, while a confidence-weighted reconstruction anomaly adaptively balances appearance and geometric deviations, yielding stable and precise anomaly localization even in depth-sparse or low-texture regions. On the MVTec 3D-AD benchmark, CMDR-IAD achieves state-of-the-art performance while operating without memory banks, reaching 97.3\% image-level AUROC (I-AUROC), 99.6\% pixel-level AUROC (P-AUROC), and 97.6\% AUPRO. On a real-world polyurethane cutting dataset, the 3D-only variant attains 92.6\% I-AUROC and 92.5\% P-AUROC, demonstrating strong effectiveness under practical industrial conditions. These results highlight the framework's robustness, modality flexibility, and the effectiveness of the proposed fusion strategies for industrial visual inspection. Our source code is available at https://github.com/ECGAI-Research/CMDR-IAD/

