---
layout: default
title: PoseMoE: Mixture-of-Experts Network for Monocular 3D Human Pose Estimation
---

# PoseMoE: Mixture-of-Experts Network for Monocular 3D Human Pose Estimation
**arXiv**：[2512.16494v1](https://arxiv.org/abs/2512.16494) · [PDF](https://arxiv.org/pdf/2512.16494.pdf)  
**作者**：Mengyuan Liu, Jiajie Liu, Jinyan Zhang, Wenhao Li, Junsong Yuan  

**一句话要点**：提出PoseMoE混合专家网络以解决单目3D人体姿态估计中深度特征与2D姿态特征纠缠的问题

**关键词**：单目3D人体姿态估计, 混合专家网络, 特征解纠缠, 深度估计, 2D姿态检测, 跨专家知识聚合

## 3 点简述
- 核心问题：基于提升的方法中，深度特征与2D姿态特征在编码时纠缠，深度不确定性影响2D姿态准确性。
- 方法要点：设计混合专家网络，分离2D姿态和深度特征编码，减少不确定深度对2D特征的影响。
- 实验或效果：在Human3.6M、MPI-INF-3DHP和3DPW数据集上优于传统提升方法。

## 摘要（原文）

> The lifting-based methods have dominated monocular 3D human pose estimation by leveraging detected 2D poses as intermediate representations. The 2D component of the final 3D human pose benefits from the detected 2D poses, whereas its depth counterpart must be estimated from scratch. The lifting-based methods encode the detected 2D pose and unknown depth in an entangled feature space, explicitly introducing depth uncertainty to the detected 2D pose, thereby limiting overall estimation accuracy. This work reveals that the depth representation is pivotal for the estimation process. Specifically, when depth is in an initial, completely unknown state, jointly encoding depth features with 2D pose features is detrimental to the estimation process. In contrast, when depth is initially refined to a more dependable state via network-based estimation, encoding it together with 2D pose information is beneficial. To address this limitation, we present a Mixture-of-Experts network for monocular 3D pose estimation named PoseMoE. Our approach introduces: (1) A mixture-of-experts network where specialized expert modules refine the well-detected 2D pose features and learn the depth features. This mixture-of-experts design disentangles the feature encoding process for 2D pose and depth, therefore reducing the explicit influence of uncertain depth features on 2D pose features. (2) A cross-expert knowledge aggregation module is proposed to aggregate cross-expert spatio-temporal contextual information. This step enhances features through bidirectional mapping between 2D pose and depth. Extensive experiments show that our proposed PoseMoE outperforms the conventional lifting-based methods on three widely used datasets: Human3.6M, MPI-INF-3DHP, and 3DPW.

