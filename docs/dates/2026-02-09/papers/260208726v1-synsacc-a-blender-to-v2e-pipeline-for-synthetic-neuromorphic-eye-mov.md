---
layout: default
title: SynSacc: A Blender-to-V2E Pipeline for Synthetic Neuromorphic Eye-Movement Data and Sim-to-Real Spiking Model Training
---

# SynSacc: A Blender-to-V2E Pipeline for Synthetic Neuromorphic Eye-Movement Data and Sim-to-Real Spiking Model Training
**arXiv**：[2602.08726v1](https://arxiv.org/abs/2602.08726) · [PDF](https://arxiv.org/pdf/2602.08726.pdf)  
**作者**：Khadija Iddrisu, Waseem Shariff, Suzanne Little, Noel OConnor  

**一句话要点**：提出SynSacc合成数据集与SNN模型，用于基于事件相机的眼动分类，提升模拟到真实训练效率。

**关键词**：事件相机, 合成数据集, 脉冲神经网络, 眼动分类, 模拟到真实训练

## 3 点简述
- 核心问题：眼动分类需高时间分辨率传感器，传统相机易产生运动模糊。
- 方法要点：使用Blender生成合成事件数据，结合SNN进行训练和微调。
- 实验或效果：模型准确率达0.83，在变时间分辨率下保持稳定，计算效率优于ANN。

## 摘要（原文）

> The study of eye movements, particularly saccades and fixations, are fundamental to understanding the mechanisms of human cognition and perception. Accurate classification of these movements requires sensing technologies capable of capturing rapid dynamics without distortion. Event cameras, also known as Dynamic Vision Sensors (DVS), provide asynchronous recordings of changes in light intensity, thereby eliminating motion blur inherent in conventional frame-based cameras and offering superior temporal resolution and data efficiency. In this study, we introduce a synthetic dataset generated with Blender to simulate saccades and fixations under controlled conditions. Leveraging Spiking Neural Networks (SNNs), we evaluate its robustness by training two architectures and finetuning on real event data. The proposed models achieve up to 0.83 accuracy and maintain consistent performance across varying temporal resolutions, demonstrating stability in eye movement classification. Moreover, the use of SNNs with synthetic event streams yields substantial computational efficiency gains over artificial neural network (ANN) counterparts, underscoring the utility of synthetic data augmentation in advancing event-based vision. All code and datasets associated with this work is available at https: //github.com/Ikhadija-5/SynSacc-Dataset.

