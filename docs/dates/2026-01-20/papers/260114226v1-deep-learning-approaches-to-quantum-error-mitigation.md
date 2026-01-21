---
layout: default
title: Deep Learning Approaches to Quantum Error Mitigation
---

# Deep Learning Approaches to Quantum Error Mitigation
**arXiv**：[2601.14226v1](https://arxiv.org/abs/2601.14226) · [PDF](https://arxiv.org/pdf/2601.14226.pdf)  
**作者**：Leonardo Placidi, Ifan Williams, Enrico Rinaldi, Daniel Mills, Cristina Cîrstoiu, Vanya Eccles, Ross Duncan  

**一句话要点**：提出基于深度学习的量子误差缓解方法，用于处理量子电路输出概率分布中的噪声。

**关键词**：量子误差缓解, 深度学习, 注意力模型, 量子电路, 噪声分布, 泛化性能

## 3 点简述
- 核心问题：量子电路输出概率分布受噪声影响，需有效缓解以接近理想结果。
- 方法要点：系统比较不同深度学习架构，发现序列到序列注意力模型在数据集上最有效。
- 实验或效果：在模拟和真实IBM量子设备数据上测试，优于基线方法，并验证跨设备泛化能力。

## 摘要（原文）

> We present a systematic investigation of deep learning methods applied to quantum error mitigation of noisy output probability distributions from measured quantum circuits. We compare different architectures, from fully connected neural networks to transformers, and we test different design/training modalities, identifying sequence-to-sequence, attention-based models as the most effective on our datasets. These models consistently produce mitigated distributions that are closer to the ideal outputs when tested on both simulated and real device data obtained from IBM superconducting quantum processing units (QPU) up to five qubits. Across several different circuit depths, our approach outperforms other baseline error mitigation techniques. We perform a series of ablation studies to examine: how different input features (circuit, device properties, noisy output statistics) affect performance; cross-dataset generalization across circuit families; and transfer learning to a different IBM QPU. We observe that generalization performance across similar devices with the same architecture works effectively, without needing to fully retrain models.

