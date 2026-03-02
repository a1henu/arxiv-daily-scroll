---
layout: default
title: FedNSAM:Consistency of Local and Global Flatness for Federated Learning
---

# FedNSAM:Consistency of Local and Global Flatness for Federated Learning
**arXiv**：[2602.23827v1](https://arxiv.org/abs/2602.23827) · [PDF](https://arxiv.org/pdf/2602.23827.pdf)  
**作者**：Junkang Liu, Fanhua Shang, Yuxuan Tian, Hongying Liu, Yuanyuan Liu  

**一句话要点**：提出FedNSAM算法，通过全局Nesterov动量协调联邦学习中全局与局部平坦度一致性

**关键词**：联邦学习, 平坦度距离, Nesterov动量, 泛化能力, 收敛分析

## 3 点简述
- 联邦学习中数据异构和多步本地更新导致全局模型陷入尖锐最小值，降低泛化性能
- 引入全局Nesterov动量到本地训练，加速SAM算法并协调全局与局部平坦度一致性
- 理论证明收敛界更紧，实验在CNN和Transformer模型上验证了性能与效率优势

## 摘要（原文）

> In federated learning (FL), multi-step local updates and data heterogeneity usually lead to sharper global minima, which degrades the performance of the global model. Popular FL algorithms integrate sharpness-aware minimization (SAM) into local training to address this issue. However, in the high data heterogeneity setting, the flatness in local training does not imply the flatness of the global model. Therefore, minimizing the sharpness of the local loss surfaces on the client data does not enable the effectiveness of SAM in FL to improve the generalization ability of the global model. We define the \textbf{flatness distance} to explain this phenomenon. By rethinking the SAM in FL and theoretically analyzing the \textbf{flatness distance}, we propose a novel \textbf{FedNSAM} algorithm that accelerates the SAM algorithm by introducing global Nesterov momentum into the local update to harmonize the consistency of global and local flatness. \textbf{FedNSAM} uses the global Nesterov momentum as the direction of local estimation of client global perturbations and extrapolation. Theoretically, we prove a tighter convergence bound than FedSAM by Nesterov extrapolation. Empirically, we conduct comprehensive experiments on CNN and Transformer models to verify the superior performance and efficiency of \textbf{FedNSAM}. The code is available at https://github.com/junkangLiu0/FedNSAM.

