---
layout: default
title: Neuro-Inspired Visual Pattern Recognition via Biological Reservoir Computing
---

# Neuro-Inspired Visual Pattern Recognition via Biological Reservoir Computing
**arXiv**：[2602.05737v1](https://arxiv.org/abs/2602.05737) · [PDF](https://arxiv.org/pdf/2602.05737.pdf)  
**作者**：Luca Ciampi, Ludovico Iannello, Fabrizio Tonelli, Gabriele Lagani, Angelo Di Garbo, Federico Cremisi, Giuseppe Amato  

**一句话要点**：提出基于体外培养皮层神经元的生物储层计算系统，用于静态视觉模式识别。

**关键词**：生物储层计算, 神经形态计算, 视觉模式识别, 高密度多电极阵列, 体外神经网络

## 3 点简述
- 核心问题：如何利用生物神经网络的动态特性作为计算基底，替代人工循环模型。
- 方法要点：使用高密度多电极阵列刺激和读取神经元活动，结合线性读出层进行分类。
- 实验或效果：在从简单刺激到MNIST手写数字的任务中，系统生成高维表示支持准确分类。

## 摘要（原文）

> In this paper, we present a neuro-inspired approach to reservoir computing (RC) in which a network of in vitro cultured cortical neurons serves as the physical reservoir. Rather than relying on artificial recurrent models to approximate neural dynamics, our biological reservoir computing (BRC) system leverages the spontaneous and stimulus-evoked activity of living neural circuits as its computational substrate. A high-density multi-electrode array (HD-MEA) provides simultaneous stimulation and readout across hundreds of channels: input patterns are delivered through selected electrodes, while the remaining ones capture the resulting high-dimensional neural responses, yielding a biologically grounded feature representation. A linear readout layer (single-layer perceptron) is then trained to classify these reservoir states, enabling the living neural network to perform static visual pattern-recognition tasks within a computer-vision framework. We evaluate the system across a sequence of tasks of increasing difficulty, ranging from pointwise stimuli to oriented bars, clock-digit-like shapes, and handwritten digits from the MNIST dataset. Despite the inherent variability of biological neural responses-arising from noise, spontaneous activity, and inter-session differences-the system consistently generates high-dimensional representations that support accurate classification. These results demonstrate that in vitro cortical networks can function as effective reservoirs for static visual pattern recognition, opening new avenues for integrating living neural substrates into neuromorphic computing frameworks. More broadly, this work contributes to the effort to incorporate biological principles into machine learning and supports the goals of neuro-inspired vision by illustrating how living neural systems can inform the design of efficient and biologically grounded computational models.

