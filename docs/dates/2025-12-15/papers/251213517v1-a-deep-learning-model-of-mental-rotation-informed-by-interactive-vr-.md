---
layout: default
title: A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments
---

# A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments
**arXiv**：[2512.13517v1](https://arxiv.org/abs/2512.13517) · [PDF](https://arxiv.org/pdf/2512.13517.pdf)  
**作者**：Raymond Khazoum, Daniela Fernandes, Aleksandr Krylov, Qin Li, Stephane Deny  

**一句话要点**：提出基于深度、等变和神经符号学习的心理旋转机制模型，结合VR实验验证

**关键词**：心理旋转建模, 等变神经网络, 神经符号学习, 空间推理, 虚拟现实实验, 机制模型

## 3 点简述
- 核心问题：建模人类心理旋转能力，即从不同视角比较物体的空间推理过程
- 方法要点：模型包含等变神经编码器、神经符号对象编码器和神经决策代理，集成深度、等变和符号表示
- 实验或效果：通过VR实验和系统消融验证模型性能，能捕捉实验参与者的表现、反应时间和行为

## 摘要（原文）

> Mental rotation -- the ability to compare objects seen from different viewpoints -- is a fundamental example of mental simulation and spatial world modelling in humans. Here we propose a mechanistic model of human mental rotation, leveraging advances in deep, equivariant, and neuro-symbolic learning. Our model consists of three stacked components: (1) an equivariant neural encoder, taking images as input and producing 3D spatial representations of objects, (2) a neuro-symbolic object encoder, deriving symbolic descriptions of objects from these spatial representations, and (3) a neural decision agent, comparing these symbolic descriptions to prescribe rotation simulations in 3D latent space via a recurrent pathway. Our model design is guided by the abundant experimental literature on mental rotation, which we complemented with experiments in VR where participants could at times manipulate the objects to compare, providing us with additional insights into the cognitive process of mental rotation. Our model captures well the performance, response times and behavior of participants in our and others' experiments. The necessity of each model component is shown through systematic ablations. Our work adds to a recent collection of deep neural models of human spatial reasoning, further demonstrating the potency of integrating deep, equivariant, and symbolic representations to model the human mind.

