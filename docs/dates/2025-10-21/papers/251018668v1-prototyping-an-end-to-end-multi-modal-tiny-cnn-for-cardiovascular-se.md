---
layout: default
title: Prototyping an End-to-End Multi-Modal Tiny-CNN for Cardiovascular Sensor Patches
---

# Prototyping an End-to-End Multi-Modal Tiny-CNN for Cardiovascular Sensor Patches
**arXiv**：[2510.18668v1](https://arxiv.org/abs/2510.18668) · [PDF](https://arxiv.org/pdf/2510.18668.pdf)  
**作者**：Mustafa Fuad Rifet Ibrahim, Tunc Alkanat, Maurice Meijer, Felix Manthey, Alexander Schlaefer, Peer Stelldinger  

**一句话要点**：提出多模态微型CNN以在资源受限医疗设备上分类心电和心音信号

**关键词**：多模态融合, 微型卷积神经网络, 医疗边缘计算, 心电信号分类, 心音信号分类, 资源优化

## 3 点简述
- 心血管疾病早期检测需可靠高效分析体戴传感器数据
- 采用早期融合卷积神经网络处理同步ECG和PCG二分类问题
- 模型在Physionet数据集验证，内存和计算成本降低千倍，精度保持竞争性

## 摘要（原文）

> The vast majority of cardiovascular diseases may be preventable if early
> signs and risk factors are detected. Cardiovascular monitoring with body-worn
> sensor devices like sensor patches allows for the detection of such signs while
> preserving the freedom and comfort of patients. However, the analysis of the
> sensor data must be robust, reliable, efficient, and highly accurate. Deep
> learning methods can automate data interpretation, reducing the workload of
> clinicians. In this work, we analyze the feasibility of applying deep learning
> models to the classification of synchronized electrocardiogram (ECG) and
> phonocardiogram (PCG) recordings on resource-constrained medical edge devices.
> We propose a convolutional neural network with early fusion of data to solve a
> binary classification problem. We train and validate our model on the
> synchronized ECG and PCG recordings from the Physionet Challenge 2016 dataset.
> Our approach reduces memory footprint and compute cost by three orders of
> magnitude compared to the state-of-the-art while maintaining competitive
> accuracy. We demonstrate the applicability of our proposed model on medical
> edge devices by analyzing energy consumption on a microcontroller and an
> experimental sensor device setup, confirming that on-device inference can be
> more energy-efficient than continuous data streaming.

