---
layout: default
title: Three factor delay learning rules for spiking neural networks
---

# Three factor delay learning rules for spiking neural networks
**arXiv**：[2601.00668v1](https://arxiv.org/abs/2601.00668) · [PDF](https://arxiv.org/pdf/2601.00668.pdf)  
**作者**：Luke Vassallo, Nima Taherinejad  

**一句话要点**：提出三因子延迟学习规则，以在线方式联合学习脉冲神经网络中的权重和延迟参数，提升时序任务性能并降低资源需求。

**关键词**：脉冲神经网络, 延迟学习, 在线学习, 时序模式识别, 资源受限环境, 高斯代理

## 3 点简述
- 核心问题：脉冲神经网络参数多限于突触权重，对时序模式识别贡献有限，现有延迟学习方法依赖大网络和离线学习，不适合资源受限环境。
- 方法要点：在基于LIF的前馈和循环SNN中引入突触和轴突延迟，使用高斯代理平滑近似脉冲导数计算资格迹，结合自上而下误差信号在线更新参数。
- 实验或效果：延迟加入使准确率比仅权重基线提升达20%，联合学习权重和延迟在相似参数下准确率提升达14%，在SHD数据集上接近离线方法，模型大小减少6.6倍，推理延迟降低67%，准确率仅下降2.4%。

## 摘要（原文）

> Spiking Neural Networks (SNNs) are dynamical systems that operate on spatiotemporal data, yet their learnable parameters are often limited to synaptic weights, contributing little to temporal pattern recognition. Learnable parameters that delay spike times can improve classification performance in temporal tasks, but existing methods rely on large networks and offline learning, making them unsuitable for real-time operation in resource-constrained environments. In this paper, we introduce synaptic and axonal delays to leaky integrate and fire (LIF)-based feedforward and recurrent SNNs, and propose three-factor learning rules to simultaneously learn delay parameters online. We employ a smooth Gaussian surrogate to approximate spike derivatives exclusively for the eligibility trace calculation, and together with a top-down error signal determine parameter updates. Our experiments show that incorporating delays improves accuracy by up to 20% over a weights-only baseline, and for networks with similar parameter counts, jointly learning weights and delays yields up to 14% higher accuracy. On the SHD speech recognition dataset, our method achieves similar accuracy to offline backpropagation-based approaches. Compared to state-of-the-art methods, it reduces model size by 6.6x and inference latency by 67%, with only a 2.4% drop in classification accuracy. Our findings benefit the design of power and area-constrained neuromorphic processors by enabling on-device learning and lowering memory requirements.

