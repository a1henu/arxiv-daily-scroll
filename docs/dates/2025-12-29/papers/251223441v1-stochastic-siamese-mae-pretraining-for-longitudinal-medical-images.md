---
layout: default
title: Stochastic Siamese MAE Pretraining for Longitudinal Medical Images
---

# Stochastic Siamese MAE Pretraining for Longitudinal Medical Images
**arXiv**：[2512.23441v1](https://arxiv.org/abs/2512.23441) · [PDF](https://arxiv.org/pdf/2512.23441.pdf)  
**作者**：Taha Emre, Arunava Chakravarty, Thomas Pinetz, Dmitrii Lachinov, Martin J. Menten, Hendrik Scholl, Sobha Sivaprasad, Daniel Rueckert, Andrew Lotery, Stefan Sacu, Ursula Schmidt-Erfurth, Hrvoje Bogunović  

**一句话要点**：提出STAMP框架，通过随机条件变分推理学习纵向医学图像的非确定性时序动态

**关键词**：纵向医学图像, 随机自监督学习, 条件变分推理, 时序动态建模, 疾病进展预测

## 3 点简述
- 问题：现有自监督方法如MAE缺乏时序感知，难以捕捉疾病进展的不确定性
- 方法：基于孪生MAE，引入时间差条件，将重建损失重构为条件变分推理目标
- 效果：在OCT和MRI数据集上，STAMP预训练模型优于现有时序MAE和基础模型

## 摘要（原文）

> Temporally aware image representations are crucial for capturing disease progression in 3D volumes of longitudinal medical datasets. However, recent state-of-the-art self-supervised learning approaches like Masked Autoencoding (MAE), despite their strong representation learning capabilities, lack temporal awareness. In this paper, we propose STAMP (Stochastic Temporal Autoencoder with Masked Pretraining), a Siamese MAE framework that encodes temporal information through a stochastic process by conditioning on the time difference between the 2 input volumes. Unlike deterministic Siamese approaches, which compare scans from different time points but fail to account for the inherent uncertainty in disease evolution, STAMP learns temporal dynamics stochastically by reframing the MAE reconstruction loss as a conditional variational inference objective. We evaluated STAMP on two OCT and one MRI datasets with multiple visits per patient. STAMP pretrained ViT models outperformed both existing temporal MAE methods and foundation models on different late stage Age-Related Macular Degeneration and Alzheimer's Disease progression prediction which require models to learn the underlying non-deterministic temporal dynamics of the diseases.

