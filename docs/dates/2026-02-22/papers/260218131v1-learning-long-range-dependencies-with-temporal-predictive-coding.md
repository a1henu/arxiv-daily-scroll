---
layout: default
title: Learning Long-Range Dependencies with Temporal Predictive Coding
---

# Learning Long-Range Dependencies with Temporal Predictive Coding
**arXiv**：[2602.18131v1](https://arxiv.org/abs/2602.18131) · [PDF](https://arxiv.org/pdf/2602.18131.pdf)  
**作者**：Tom Potter, Oliver Rhodes  

**一句话要点**：提出结合时间预测编码与近似实时循环学习的方法，以解决循环神经网络中长程依赖学习的高能耗问题。

**关键词**：时间预测编码, 循环神经网络, 长程依赖学习, 实时循环学习, 节能学习系统, 机器翻译

## 3 点简述
- 核心问题：传统反向传播通过时间训练循环神经网络存在非局部计算、高能耗和存储需求大的问题。
- 方法要点：结合时间预测编码与近似实时循环学习，实现有效的时空信用分配，保持局部和并行化特性。
- 实验或效果：在合成基准和真实任务中性能接近反向传播通过时间，机器翻译任务测试困惑度达7.62。

## 摘要（原文）

> Predictive Coding (PC) is a biologically-inspired learning framework characterised by local, parallelisable operations, properties that enable energy-efficient implementation on neuromorphic hardware. Despite this, extending PC effectively to recurrent neural networks (RNNs) has been challenging, particularly for tasks involving long-range temporal dependencies. Backpropagation Through Time (BPTT) remains the dominant method for training RNNs, but its non-local computation, lack of spatial parallelism, and requirement to store extensive activation histories results in significant energy consumption. This work introduces a novel method combining Temporal Predictive Coding (tPC) with approximate Real-Time Recurrent Learning (RTRL), enabling effective spatio-temporal credit assignment. Results indicate that the proposed method can closely match the performance of BPTT on both synthetic benchmarks and real-world tasks. On a challenging machine translation task, with a 15-million parameter model, the proposed method achieves a test perplexity of 7.62 (vs. 7.49 for BPTT), marking one of the first applications of tPC to tasks of this scale. These findings demonstrate the potential of this method to learn complex temporal dependencies whilst retaining the local, parallelisable, and flexible properties of the original PC framework, paving the way for more energy-efficient learning systems.

