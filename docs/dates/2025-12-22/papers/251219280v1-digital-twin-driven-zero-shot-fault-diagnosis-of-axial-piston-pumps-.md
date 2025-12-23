---
layout: default
title: Digital Twin-Driven Zero-Shot Fault Diagnosis of Axial Piston Pumps Using Fluid-Borne Noise Signals
---

# Digital Twin-Driven Zero-Shot Fault Diagnosis of Axial Piston Pumps Using Fluid-Borne Noise Signals
**arXiv**：[2512.19280v1](https://arxiv.org/abs/2512.19280) · [PDF](https://arxiv.org/pdf/2512.19280.pdf)  
**作者**：Chang Dong, Jianfeng Tao, Chengliang Liu  

**一句话要点**：提出数字孪生驱动的零样本故障诊断框架，利用流体噪声信号诊断轴向柱塞泵故障。

**关键词**：数字孪生, 零样本故障诊断, 流体噪声信号, 轴向柱塞泵, 物理信息神经网络, 梯度加权类激活映射

## 3 点简述
- 核心问题：传统方法需大量标注故障数据或受参数不确定性限制，难以在数据稀缺场景下实现可靠诊断。
- 方法要点：仅用健康数据校准高保真数字孪生模型，生成合成故障信号训练深度学习分类器，并集成物理信息神经网络作为虚拟传感器。
- 实验或效果：校准模型在真实基准测试中诊断准确率超95%，未校准模型性能显著降低，验证框架有效性。

## 摘要（原文）

> Axial piston pumps are crucial components in fluid power systems, where reliable fault diagnosis is essential for ensuring operational safety and efficiency. Traditional data-driven methods require extensive labeled fault data, which is often impractical to obtain, while model-based approaches suffer from parameter uncertainties. This paper proposes a digital twin (DT)-driven zero-shot fault diagnosis framework utilizing fluid-borne noise (FBN) signals. The framework calibrates a high-fidelity DT model using only healthy-state data, generates synthetic fault signals for training deep learning classifiers, and employs a physics-informed neural network (PINN) as a virtual sensor for flow ripple estimation. Gradient-weighted class activation mapping (Grad-CAM) is integrated to visualize the decision-making process of neural networks, revealing that large kernels matching the subsequence length in time-domain inputs and small kernels in time-frequency domain inputs enable higher diagnostic accuracy by focusing on physically meaningful features. Experimental validations demonstrate that training on signals from the calibrated DT model yields diagnostic accuracies exceeding 95\% on real-world benchmarks, while uncalibrated models result in significantly lower performance, highlighting the framework's effectiveness in data-scarce scenarios.

