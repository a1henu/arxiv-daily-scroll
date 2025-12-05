---
layout: default
title: WiFi-based Cross-Domain Gesture Recognition Using Attention Mechanism
---

# WiFi-based Cross-Domain Gesture Recognition Using Attention Mechanism
**arXiv**：[2512.04521v1](https://arxiv.org/abs/2512.04521) · [PDF](https://arxiv.org/pdf/2512.04521.pdf)  
**作者**：Ruijing Liu, Cunhua Pan, Jiaming Zeng, Hong Ren, Kezhi Wang, Lei Kong, Jiangzhou Wang  

**一句话要点**：提出基于注意力机制的WiFi跨域手势识别网络，以提升未训练环境下的识别性能。

**关键词**：WiFi手势识别, 跨域识别, 注意力机制, 多普勒谱, ResNet18, Widar3数据集

## 3 点简述
- 核心问题：现有WiFi手势识别方案在跨域（未训练环境）中性能不足。
- 方法要点：从CSI提取多普勒谱生成融合图像，结合空间与通道注意力机制提取域无关特征。
- 实验或效果：在Widar3数据集上，域内准确率99.72%，跨域准确率97.61%，优于现有方案。

## 摘要（原文）

> While fulfilling communication tasks, wireless signals can also be used to sense the environment. Among various types of sensing media, WiFi signals offer advantages such as widespread availability, low hardware cost, and strong robustness to environmental conditions like light, temperature, and humidity. By analyzing Wi-Fi signals in the environment, it is possible to capture dynamic changes of the human body and accomplish sensing applications such as gesture recognition. Although many existing gesture sensing solutions perform well in-domain but lack cross-domain capabilities (i.e., recognition performance in untrained environments). To address this, we extract Doppler spectra from the channel state information (CSI) received by all receivers and concatenate each Doppler spectrum along the same time axis to generate fused images with multi-angle information as input features. Furthermore, inspired by the convolutional block attention module (CBAM), we propose a gesture recognition network that integrates a multi-semantic spatial attention mechanism with a self-attention-based channel mechanism. This network constructs attention maps to quantify the spatiotemporal features of gestures in images, enabling the extraction of key domain-independent features. Additionally, ResNet18 is employed as the backbone network to further capture deep-level features. To validate the network performance, we evaluate the proposed network on the public Widar3 dataset, and the results show that it not only maintains high in-domain accuracy of 99.72%, but also achieves high performance in cross-domain recognition of 97.61%, significantly outperforming existing best solutions.

