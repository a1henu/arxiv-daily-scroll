---
layout: default
title: Error Bound Analysis of Physics-Informed Neural Networks-Driven T2 Quantification in Cardiac Magnetic Resonance Imaging
---

# Error Bound Analysis of Physics-Informed Neural Networks-Driven T2 Quantification in Cardiac Magnetic Resonance Imaging
**arXiv**：[2512.14211v1](https://arxiv.org/abs/2512.14211) · [PDF](https://arxiv.org/pdf/2512.14211.pdf)  
**作者**：Mengxue Zhang, Qingrui Cai, Yinyin Chen, Hang Jin, Jianjun Zhou, Qiu Guo, Peijun Zhao, Zhiping Mao, Xingxing Zhang, Yuyu Xia, Xianwang Jiang, Qin Xu, Chunyan Xiong, Yirong Zhou, Chengyan Wang, Xiaobo Qu  

**一句话要点**：提出基于物理信息神经网络的T2量化误差界分析方法，用于心脏磁共振成像。

**关键词**：物理信息神经网络, 磁共振成像, T2量化, 误差界分析, 心脏成像, Bloch方程

## 3 点简述
- 核心问题：现有深度学习方法需大量训练数据且缺乏理论支持，T2量化无公认金标准。
- 方法要点：将MRI物理模型（Bloch方程）嵌入PINN损失，无需预定义训练数据库，推导T2估计误差和泛化误差的严格上界。
- 实验或效果：在数值心脏模型、水模和94例急性心肌梗死患者中验证，实现低误差T2估计，符合理论误差界。

## 摘要（原文）

> Physics-Informed Neural Networks (PINN) are emerging as a promising approach for quantitative parameter estimation of Magnetic Resonance Imaging (MRI). While existing deep learning methods can provide an accurate quantitative estimation of the T2 parameter, they still require large amounts of training data and lack theoretical support and a recognized gold standard. Thus, given the absence of PINN-based approaches for T2 estimation, we propose embedding the fundamental physics of MRI, the Bloch equation, in the loss of PINN, which is solely based on target scan data and does not require a pre-defined training database. Furthermore, by deriving rigorous upper bounds for both the T2 estimation error and the generalization error of the Bloch equation solution, we establish a theoretical foundation for evaluating the PINN's quantitative accuracy. Even without access to the ground truth or a gold standard, this theory enables us to estimate the error with respect to the real quantitative parameter T2. The accuracy of T2 mapping and the validity of the theoretical analysis are demonstrated on a numerical cardiac model and a water phantom, where our method exhibits excellent quantitative precision in the myocardial T2 range. Clinical applicability is confirmed in 94 acute myocardial infarction (AMI) patients, achieving low-error quantitative T2 estimation under the theoretical error bound, highlighting the robustness and potential of PINN.

