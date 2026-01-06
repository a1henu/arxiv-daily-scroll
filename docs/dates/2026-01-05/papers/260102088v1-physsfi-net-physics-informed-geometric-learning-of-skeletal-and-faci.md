---
layout: default
title: PhysSFI-Net: Physics-informed Geometric Learning of Skeletal and Facial Interactions for Orthognathic Surgical Outcome Prediction
---

# PhysSFI-Net: Physics-informed Geometric Learning of Skeletal and Facial Interactions for Orthognathic Surgical Outcome Prediction
**arXiv**：[2601.02088v1](https://arxiv.org/abs/2601.02088) · [PDF](https://arxiv.org/pdf/2601.02088.pdf)  
**作者**：Jiahao Bao, Huazhen Liu, Yu Zhuang, Leran Tao, Xinyu Xu, Yongtao Shi, Mengjia Cheng, Yiming Wang, Congshuang Ku, Ting Zeng, Yilang Du, Siyi Chen, Shunyao Shen, Suncheng Xiang, Hongbo Yu  

**一句话要点**：提出PhysSFI-Net以解决正颌手术后面部软组织变形预测的准确性与可解释性问题。

**关键词**：正颌手术预测, 几何深度学习, 物理信息学习, 软组织变形, 分层图网络, 生物力学建模

## 3 点简述
- 核心问题：传统生物力学模型计算成本高，几何深度学习方法缺乏可解释性，影响术后面部形态预测精度。
- 方法要点：结合物理信息与几何深度学习，通过分层图模块、LSTM序列预测器和生物力学模块实现高分辨率预测。
- 实验或效果：在135名患者数据上验证，PhysSFI-Net在点云形状误差、表面偏差误差和标志点定位误差上优于现有方法。

## 摘要（原文）

> Orthognathic surgery repositions jaw bones to restore occlusion and enhance facial aesthetics. Accurate simulation of postoperative facial morphology is essential for preoperative planning. However, traditional biomechanical models are computationally expensive, while geometric deep learning approaches often lack interpretability. In this study, we develop and validate a physics-informed geometric deep learning framework named PhysSFI-Net for precise prediction of soft tissue deformation following orthognathic surgery. PhysSFI-Net consists of three components: a hierarchical graph module with craniofacial and surgical plan encoders combined with attention mechanisms to extract skeletal-facial interaction features; a Long Short-Term Memory (LSTM)-based sequential predictor for incremental soft tissue deformation; and a biomechanics-inspired module for high-resolution facial surface reconstruction. Model performance was assessed using point cloud shape error (Hausdorff distance), surface deviation error, and landmark localization error (Euclidean distances of craniomaxillofacial landmarks) between predicted facial shapes and corresponding ground truths. A total of 135 patients who underwent combined orthodontic and orthognathic treatment were included for model training and validation. Quantitative analysis demonstrated that PhysSFI-Net achieved a point cloud shape error of 1.070 +/- 0.088 mm, a surface deviation error of 1.296 +/- 0.349 mm, and a landmark localization error of 2.445 +/- 1.326 mm. Comparative experiments indicated that PhysSFI-Net outperformed the state-of-the-art method ACMT-Net in prediction accuracy. In conclusion, PhysSFI-Net enables interpretable, high-resolution prediction of postoperative facial morphology with superior accuracy, showing strong potential for clinical application in orthognathic surgical planning and simulation.

