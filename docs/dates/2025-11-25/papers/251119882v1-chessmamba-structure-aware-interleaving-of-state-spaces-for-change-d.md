---
layout: default
title: ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images
---

# ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images
**arXiv**：[2511.19882v1](https://arxiv.org/abs/2511.19882) · [PDF](https://arxiv.org/pdf/2511.19882.pdf)  
**作者**：Lei Ding, Tong Liu, Xuanguang Liu, Xiangyun Liu, Haitao Guo, Jun Lu  

**一句话要点**：提出ChessMamba框架以解决多时相遥感图像变化检测中的结构一致性问题

**关键词**：变化检测, 遥感图像, 状态空间模型, 结构感知, 多时相分析, 棋盘交错

## 3 点简述
- 核心问题：多时相遥感图像异质性和时空错位破坏局部结构，影响变化定位准确性
- 方法要点：采用棋盘交错和蛇形扫描序列化多时相特征，结合多空洞卷积实现结构感知融合
- 实验或效果：在二元变化检测、语义变化检测和多模态建筑损伤评估任务中，精度显著优于现有方法

## 摘要（原文）

> Change detection (CD) in multitemporal remote sensing imagery presents significant challenges for fine-grained recognition, owing to heterogeneity and spatiotemporal misalignment. However, existing methodologies based on vision transformers or state-space models typically disrupt local structural consistency during temporal serialization, obscuring discriminative cues under misalignment and hindering reliable change localization. To address this, we introduce ChessMamba, a structure-aware framework leveraging interleaved state-space modeling for robust CD with multi-temporal inputs. ChessMamba integrates a SpatialMamba encoder with a lightweight cross-source interaction module, featuring two key innovations: (i) Chessboard interleaving with snake scanning order, which serializes multi-temporal features into a unified sequence within a single forward pass, thereby shortening interaction paths and enabling direct comparison for accurate change localization; and (ii) Structure-aware fusion via multi-dilated convolutions, selectively capturing center-and-corner neighborhood contexts within each mono-temporal. Comprehensive evaluations on three CD tasks, including binary CD, semantic CD and multimodal building damage assessment, demonstrate that ChessMamba effectively fuses heterogeneous features and achieves substantial accuracy improvements over state-of-the-art methods.The relevant code will be available at: github.com/DingLei14/ChessMamba.

