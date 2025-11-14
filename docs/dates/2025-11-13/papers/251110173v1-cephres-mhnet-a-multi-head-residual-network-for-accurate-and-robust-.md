---
layout: default
title: CephRes-MHNet: A Multi-Head Residual Network for Accurate and Robust Cephalometric Landmark Detection
---

# CephRes-MHNet: A Multi-Head Residual Network for Accurate and Robust Cephalometric Landmark Detection
**arXiv**：[2511.10173v1](https://arxiv.org/abs/2511.10173) · [PDF](https://arxiv.org/pdf/2511.10173.pdf)  
**作者**：Ahmed Jaheen, Islam Hassan, Mohanad Abouserie, Abdelaty Rehab, Adham Elasfar, Knzy Elmasry, Mostafa El-Dawlatly, Seif Eldawlatly  

**一句话要点**：提出CephRes-MHNet多头残差网络，用于精确鲁棒的头影测量标志点检测。

**关键词**：头影测量标志点检测, 多头残差网络, 双注意力机制, X射线图像分析, 解剖定位

## 3 点简述
- 问题：2D侧位头颅X射线中头影测量标志点定位困难，手动标注耗时且易错。
- 方法：集成残差编码、双注意力机制和多头解码器，提升上下文推理和解剖精度。
- 效果：在Aariz数据集上MRE为1.23 mm，SDR@2.0 mm达85.5%，优于基线模型。

## 摘要（原文）

> Accurate localization of cephalometric landmarks from 2D lateral skull X-rays is vital for orthodontic diagnosis and treatment. Manual annotation is time-consuming and error-prone, whereas automated approaches often struggle with low contrast and anatomical complexity. This paper introduces CephRes-MHNet, a multi-head residual convolutional network for robust and efficient cephalometric landmark detection. The architecture integrates residual encoding, dual-attention mechanisms, and multi-head decoders to enhance contextual reasoning and anatomical precision. Trained on the Aariz Cephalometric dataset of 1,000 radiographs, CephRes-MHNet achieved a mean radial error (MRE) of 1.23 mm and a success detection rate (SDR) @ 2.0 mm of 85.5%, outperforming all evaluated models. In particular, it exceeded the strongest baseline, the attention-driven AFPF-Net (MRE = 1.25 mm, SDR @ 2.0 mm = 84.1%), while using less than 25% of its parameters. These results demonstrate that CephRes-MHNet attains state-of-the-art accuracy through architectural efficiency, providing a practical solution for real-world orthodontic analysis.

