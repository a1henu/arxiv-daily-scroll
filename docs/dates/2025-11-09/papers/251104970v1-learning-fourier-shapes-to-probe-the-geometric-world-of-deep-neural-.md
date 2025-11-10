---
layout: default
title: Learning Fourier shapes to probe the geometric world of deep neural networks
---

# Learning Fourier shapes to probe the geometric world of deep neural networks
**arXiv**：[2511.04970v1](https://arxiv.org/abs/2511.04970) · [PDF](https://arxiv.org/pdf/2511.04970.pdf)  
**作者**：Jian Wang, Yixing Yong, Haixia Bi, Lijun He, Fan Li  

**一句话要点**：提出傅里叶形状学习框架以探索深度神经网络的几何理解

**关键词**：几何理解, 傅里叶形状, 深度神经网络, 可解释性, 对抗攻击

## 3 点简述
- 核心问题：深度神经网络几何理解研究不足，偏向纹理分析。
- 方法要点：使用傅里叶级数参数化形状，结合缠绕数映射和能量约束优化。
- 实验或效果：形状可生成高置信分类、精确解释模型区域和通用对抗攻击。

## 摘要（原文）

> While both shape and texture are fundamental to visual recognition, research
> on deep neural networks (DNNs) has predominantly focused on the latter, leaving
> their geometric understanding poorly probed. Here, we show: first, that
> optimized shapes can act as potent semantic carriers, generating
> high-confidence classifications from inputs defined purely by their geometry;
> second, that they are high-fidelity interpretability tools that precisely
> isolate a model's salient regions; and third, that they constitute a new,
> generalizable adversarial paradigm capable of deceiving downstream visual
> tasks. This is achieved through an end-to-end differentiable framework that
> unifies a powerful Fourier series to parameterize arbitrary shapes, a winding
> number-based mapping to translate them into the pixel grid required by DNNs,
> and signal energy constraints that enhance optimization efficiency while
> ensuring physically plausible shapes. Our work provides a versatile framework
> for probing the geometric world of DNNs and opens new frontiers for challenging
> and understanding machine perception.

