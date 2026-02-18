---
layout: default
title: A Note on Non-Composability of Layerwise Approximate Verification for Neural Inference
---

# A Note on Non-Composability of Layerwise Approximate Verification for Neural Inference
**arXiv**：[2602.15756v1](https://arxiv.org/abs/2602.15756) · [PDF](https://arxiv.org/pdf/2602.15756.pdf)  
**作者**：Or Zamir  

**一句话要点**：提出反例证明神经网络层间近似验证不可组合性

**关键词**：神经网络验证, 近似计算, 可组合性, 对抗性误差, 零知识证明, 机器学习推理

## 3 点简述
- 核心问题：层间近似验证的组合性假设在一般神经网络中不成立
- 方法要点：构造功能等价网络，展示层计算误差可任意操控最终输出
- 实验或效果：通过简单反例，揭示对抗性误差能引导输出至预设范围

## 摘要（原文）

> A natural and informal approach to verifiable (or zero-knowledge) ML inference over floating-point data is: ``prove that each layer was computed correctly up to tolerance $δ$; therefore the final output is a reasonable inference result''. This short note gives a simple counterexample showing that this inference is false in general: for any neural network, we can construct a functionally equivalent network for which adversarially chosen approximation-magnitude errors in individual layer computations suffice to steer the final output arbitrarily (within a prescribed bounded range).

