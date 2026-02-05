---
layout: default
title: Knowledge Distillation for mmWave Beam Prediction Using Sub-6 GHz Channels
---

# Knowledge Distillation for mmWave Beam Prediction Using Sub-6 GHz Channels
**arXiv**：[2602.04703v1](https://arxiv.org/abs/2602.04703) · [PDF](https://arxiv.org/pdf/2602.04703.pdf)  
**作者**：Sina Tavakolian, Nhan Thanh Nguyen, Ahmed Alkhateeb, Markku Juntti  

**一句话要点**：提出基于知识蒸馏的毫米波波束预测框架，利用Sub-6 GHz信道降低计算开销

**关键词**：毫米波通信, 波束预测, 知识蒸馏, Sub-6 GHz信道, 深度学习模型压缩

## 3 点简述
- 毫米波高移动性环境中波束成形训练开销大，现有方法依赖计算密集型深度学习模型
- 采用知识蒸馏技术，设计紧凑学生模型，通过个体和关系蒸馏策略模仿教师模型性能
- 仿真显示学生模型在保持波束预测精度和频谱效率的同时，减少99%参数和计算复杂度

## 摘要（原文）

> Beamforming in millimeter-wave (mmWave) high-mobility environments typically incurs substantial training overhead. While prior studies suggest that sub-6 GHz channels can be exploited to predict optimal mmWave beams, existing methods depend on large deep learning (DL) models with prohibitive computational and memory requirements. In this paper, we propose a computationally efficient framework for sub-6 GHz channel-mmWave beam mapping based on the knowledge distillation (KD) technique. We develop two compact student DL architectures based on individual and relational distillation strategies, which retain only a few hidden layers yet closely mimic the performance of large teacher DL models. Extensive simulations demonstrate that the proposed student models achieve the teacher's beam prediction accuracy and spectral efficiency while reducing trainable parameters and computational complexity by 99%.

