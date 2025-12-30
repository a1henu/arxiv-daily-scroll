---
layout: default
title: Energy and Memory-Efficient Federated Learning With Ordered Layer Freezing
---

# Energy and Memory-Efficient Federated Learning With Ordered Layer Freezing
**arXiv**：[2512.23200v1](https://arxiv.org/abs/2512.23200) · [PDF](https://arxiv.org/pdf/2512.23200.pdf)  
**作者**：Ziru Niu, Hai Dong, A. K. Qin, Tao Gu, Pengcheng Zhang  

**一句话要点**：提出FedOLF以解决联邦学习中边缘设备计算、内存和带宽限制问题

**关键词**：联邦学习, 层冻结, 边缘计算, 能效优化, 内存效率, 非独立同分布数据

## 3 点简述
- 核心问题：联邦学习在物联网边缘设备上受限于计算能力、内存和带宽，影响效率和可扩展性。
- 方法要点：FedOLF通过预定义顺序冻结层减少计算和内存需求，并引入Tensor Operation Approximation降低通信和能耗。
- 实验或效果：在非独立同分布数据上，FedOLF在多个数据集和模型上实现更高准确率、能效和更低内存占用。

## 摘要（原文）

> Federated Learning (FL) has emerged as a privacy-preserving paradigm for training machine learning models across distributed edge devices in the Internet of Things (IoT). By keeping data local and coordinating model training through a central server, FL effectively addresses privacy concerns and reduces communication overhead. However, the limited computational power, memory, and bandwidth of IoT edge devices pose significant challenges to the efficiency and scalability of FL, especially when training deep neural networks. Various FL frameworks have been proposed to reduce computation and communication overheads through dropout or layer freezing. However, these approaches often sacrifice accuracy or neglect memory constraints. To this end, in this work, we introduce Federated Learning with Ordered Layer Freezing (FedOLF). FedOLF consistently freezes layers in a predefined order before training, significantly mitigating computation and memory requirements. To further reduce communication and energy costs, we incorporate Tensor Operation Approximation (TOA), a lightweight alternative to conventional quantization that better preserves model accuracy. Experimental results demonstrate that over non-iid data, FedOLF achieves at least 0.3%, 6.4%, 5.81%, 4.4%, 6.27% and 1.29% higher accuracy than existing works respectively on EMNIST (with CNN), CIFAR-10 (with AlexNet), CIFAR-100 (with ResNet20 and ResNet44), and CINIC-10 (with ResNet20 and ResNet44), along with higher energy efficiency and lower memory footprint.

