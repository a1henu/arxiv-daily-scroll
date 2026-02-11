---
layout: default
title: Bladder Vessel Segmentation using a Hybrid Attention-Convolution Framework
---

# Bladder Vessel Segmentation using a Hybrid Attention-Convolution Framework
**arXiv**：[2602.09949v1](https://arxiv.org/abs/2602.09949) · [PDF](https://arxiv.org/pdf/2602.09949.pdf)  
**作者**：Franziska Krauß, Matthias Ege, Zoltan Lovasz, Albrecht Bartz-Schmidt, Igor Tsaur, Oliver Sawodny, Carina Veil  

**一句话要点**：提出混合注意力-卷积框架以解决膀胱内窥镜血管分割中的复杂挑战

**关键词**：血管分割, 混合注意力-卷积框架, 膀胱内窥镜, 自监督预训练, 结构连通性优化

## 3 点简述
- 核心问题：膀胱内窥镜血管分割面临数据缺陷、动态变形和黏膜褶皱干扰等临床特定复杂性。
- 方法要点：结合Transformer捕获全局血管拓扑先验和CNN学习残差细化图，以精确恢复细血管细节。
- 实验或效果：在BlaVeS数据集上实现高精度（0.94），有效抑制动态黏膜褶皱的假阳性，提升临床导航可靠性。

## 摘要（原文）

> Urinary bladder cancer surveillance requires tracking tumor sites across repeated interventions, yet the deformable and hollow bladder lacks stable landmarks for orientation. While blood vessels visible during endoscopy offer a patient-specific "vascular fingerprint" for navigation, automated segmentation is challenged by imperfect endoscopic data, including sparse labels, artifacts like bubbles or variable lighting, continuous deformation, and mucosal folds that mimic vessels. State-of-the-art vessel segmentation methods often fail to address these domain-specific complexities. We introduce a Hybrid Attention-Convolution (HAC) architecture that combines Transformers to capture global vessel topology prior with a CNN that learns a residual refinement map to precisely recover thin-vessel details. To prioritize structural connectivity, the Transformer is trained on optimized ground truth data that exclude short and terminal branches. Furthermore, to address data scarcity, we employ a physics-aware pretraining, that is a self-supervised strategy using clinically grounded augmentations on unlabeled data. Evaluated on the BlaVeS dataset, consisting of endoscopic video frames, our approach achieves high accuracy (0.94) and superior precision (0.61) and clDice (0.66) compared to state-of-the-art medical segmentation models. Crucially, our method successfully suppresses false positives from mucosal folds that dynamically appear and vanish as the bladder fills and empties during surgery. Hence, HAC provides the reliable structural stability required for clinical navigation.

