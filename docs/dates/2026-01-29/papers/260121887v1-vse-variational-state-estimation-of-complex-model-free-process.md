---
layout: default
title: VSE: Variational state estimation of complex model-free process
---

# VSE: Variational state estimation of complex model-free process
**arXiv**：[2601.21887v1](https://arxiv.org/abs/2601.21887) · [PDF](https://arxiv.org/pdf/2601.21887.pdf)  
**作者**：Gustav Norén, Anubhab Ghosh, Fredrik Cumlin, Saikat Chatterjee  

**一句话要点**：提出变分状态估计方法，用于无模型复杂动态过程的状态估计

**关键词**：变分状态估计, 无模型动态过程, 循环神经网络, 高斯后验, 非线性测量, 跟踪应用

## 3 点简述
- 核心问题：从非线性测量中估计无模型复杂动态过程的状态，缺乏物理模型描述状态演化
- 方法要点：使用两个循环神经网络基于变分推断提供闭式高斯后验，推理阶段计算简单
- 实验或效果：在随机洛伦兹系统跟踪应用中，与已知模型的粒子滤波和未知模型的数据驱动方法竞争

## 摘要（原文）

> We design a variational state estimation (VSE) method that provides a closed-form Gaussian posterior of an underlying complex dynamical process from (noisy) nonlinear measurements. The complex process is model-free. That is, we do not have a suitable physics-based model characterizing the temporal evolution of the process state. The closed-form Gaussian posterior is provided by a recurrent neural network (RNN). The use of RNN is computationally simple in the inference phase. For learning the RNN, an additional RNN is used in the learning phase. Both RNNs help each other learn better based on variational inference principles. The VSE is demonstrated for a tracking application - state estimation of a stochastic Lorenz system (a benchmark process) using a 2-D camera measurement model. The VSE is shown to be competitive against a particle filter that knows the Lorenz system model and a recently proposed data-driven state estimation method that does not know the Lorenz system model.

