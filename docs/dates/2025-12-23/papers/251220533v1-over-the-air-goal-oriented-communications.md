---
layout: default
title: Over-the-Air Goal-Oriented Communications
---

# Over-the-Air Goal-Oriented Communications
**arXiv**：[2512.20533v1](https://arxiv.org/abs/2512.20533) · [PDF](https://arxiv.org/pdf/2512.20533.pdf)  
**作者**：Kyriakos Stylianopoulos, Paolo Di Lorenzo, George C. Alexandropoulos  

**一句话要点**：提出基于可编程超表面的目标导向通信系统，通过无线信道执行计算以实现边缘推理。

**关键词**：目标导向通信, 可编程超表面, 边缘推理, 深度神经网络, 无线信道计算, 能耗优化

## 3 点简述
- 核心问题：传统香农通信范式在边缘推理中需重建数据，目标导向通信直接交换特征以预测未知属性。
- 方法要点：将发射机、接收机和超表面信道视为单一深度神经网络，通过反向传播训练进行推理。
- 实验或效果：使用堆叠智能超表面，在多种系统参数和数据集下性能接近全数字神经网络，降低能耗。

## 摘要（原文）

> Goal-oriented communications offer an attractive alternative to the Shannon-based communication paradigm, where the data is never reconstructed at the Receiver (RX) side. Rather, focusing on the case of edge inference, the Transmitter (TX) and the RX cooperate to exchange features of the input data that will be used to predict an unseen attribute of them, leveraging information from collected data sets. This chapter demonstrates that the wireless channel can be used to perform computations over the data, when equipped with programmable metasurfaces. The end-to-end system of the TX, RX, and MS-based channel is treated as a single deep neural network which is trained through backpropagation to perform inference on unseen data. Using Stacked Intelligent Metasurfaces (SIM), it is shown that this Metasurfaces-Integrated Neural Network (MINN) can achieve performance comparable to fully digital neural networks under various system parameters and data sets. By offloading computations onto the channel itself, important benefits may be achieved in terms of energy consumption, arising from reduced computations at the transceivers and smaller transmission power required for successful inference.

