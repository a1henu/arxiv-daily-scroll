---
layout: default
title: Hardware-accelerated graph neural networks: an alternative approach for neuromorphic event-based audio classification and keyword spotting on SoC FPGA
---

# Hardware-accelerated graph neural networks: an alternative approach for neuromorphic event-based audio classification and keyword spotting on SoC FPGA
**arXiv**：[2602.16442v1](https://arxiv.org/abs/2602.16442) · [PDF](https://arxiv.org/pdf/2602.16442.pdf)  
**作者**：Kamil Jeziorek, Piotr Wzorek, Krzysztof Blachut, Hiroshi Nakano, Manon Dampfhoffer, Thomas Mesquida, Hiroaki Nishi, Thomas Dalgaty, Tomasz Kryjak  

**一句话要点**：提出基于SoC FPGA的硬件加速图神经网络，用于神经形态事件音频分类与关键词检测

**关键词**：硬件加速图神经网络, 神经形态音频处理, SoC FPGA实现, 事件驱动关键词检测, 低功耗边缘计算

## 3 点简述
- 针对神经形态设备产生的事件流数据，设计硬件感知架构以实现高效低延迟边缘处理
- 利用人工耳蜗将时序信号转换为稀疏事件数据，降低内存和计算成本
- 在SHD和SSC数据集上评估，量化模型准确率达92.3%，功耗1.18W，延迟仅10.53微秒

## 摘要（原文）

> As the volume of data recorded by embedded edge sensors increases, particularly from neuromorphic devices producing discrete event streams, there is a growing need for hardware-aware neural architectures that enable efficient, low-latency, and energy-conscious local processing. We present an FPGA implementation of event-graph neural networks for audio processing. We utilise an artificial cochlea that converts time-series signals into sparse event data, reducing memory and computation costs. Our architecture was implemented on a SoC FPGA and evaluated on two open-source datasets. For classification task, our baseline floating-point model achieves 92.7% accuracy on SHD dataset - only 2.4% below the state of the art - while requiring over 10x and 67x fewer parameters. On SSC, our models achieve 66.9-71.0% accuracy. Compared to FPGA-based spiking neural networks, our quantised model reaches 92.3% accuracy, outperforming them by up to 19.3% while reducing resource usage and latency. For SSC, we report the first hardware-accelerated evaluation. We further demonstrate the first end-to-end FPGA implementation of event-audio keyword spotting, combining graph convolutional layers with recurrent sequence modelling. The system achieves up to 95% word-end detection accuracy, with only 10.53 microsecond latency and 1.18 W power consumption, establishing a strong benchmark for energy-efficient event-driven KWS.

