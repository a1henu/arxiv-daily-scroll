---
layout: default
title: IRSDE-Despeckle: A Physics-Grounded Diffusion Model for Generalizable Ultrasound Despeckling
---

# IRSDE-Despeckle: A Physics-Grounded Diffusion Model for Generalizable Ultrasound Despeckling
**arXiv**：[2602.22717v1](https://arxiv.org/abs/2602.22717) · [PDF](https://arxiv.org/pdf/2602.22717.pdf)  
**作者**：Shuoqi Chen, Yujia Wu, Geoffrey P. Luke  

**一句话要点**：提出基于扩散模型的超声去斑方法，提升图像质量并评估不确定性。

**关键词**：超声去斑, 扩散模型, 图像恢复, 不确定性评估, 模拟训练

## 3 点简述
- 超声成像中斑点噪声降低图像质量，影响诊断准确性。
- 采用扩散模型框架，通过模拟配对数据集进行监督训练，重建去斑图像并保留解剖结构。
- 在模拟测试集上优于传统和基于学习的方法，量化不确定性以指示重建误差区域。

## 摘要（原文）

> Ultrasound imaging is widely used for real-time, noninvasive diagnosis, but speckle and related artifacts reduce image quality and can hinder interpretation. We present a diffusion-based ultrasound despeckling method built on the Image Restoration Stochastic Differential Equations framework. To enable supervised training, we curate large paired datasets by simulating ultrasound images from speckle-free magnetic resonance images using the Matlab UltraSound Toolbox. The proposed model reconstructs speckle-suppressed images while preserving anatomically meaningful edges and contrast. On a held-out simulated test set, our approach consistently outperforms classical filters and recent learning-based despeckling baselines. We quantify prediction uncertainty via cross-model variance and show that higher uncertainty correlates with higher reconstruction error, providing a practical indicator of difficult or failure-prone regions. Finally, we evaluate sensitivity to simulation probe settings and observe domain shift, motivating diversified training and adaptation for robust clinical deployment.

