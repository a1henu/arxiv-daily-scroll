---
layout: default
title: Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
---

# Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
**arXiv**：[2603.09221v1](https://arxiv.org/abs/2603.09221) · [PDF](https://arxiv.org/pdf/2603.09221.pdf)  
**作者**：Peihao Wang, Shan Yang, Xijun Wang, Tesi Xiao, Xin Liu, Changlong Yu, Yu Lou, Pan Li, Zhangyang Wang, Ming Lin, René Vidal  

**一句话要点**：提出测试时控制层，将推理建模为最优控制以增强语言模型推理能力

**关键词**：最优控制, 推理增强, 硬件高效LQR, 测试时训练, 语言模型适配器, 数学推理

## 3 点简述
- 核心问题：现代语言模型缺乏原生推理能力，无法像人类一样规划未来状态和行动
- 方法要点：引入TTC层，在推理时执行有限时域LQR规划，将价值函数嵌入神经网络架构
- 实验或效果：集成到预训练LLM中，在MATH-500等数学推理任务上性能提升显著

## 摘要（原文）

> Associative memory has long underpinned the design of sequential models. Beyond recall, humans reason by projecting future states and selecting goal-directed actions, a capability that modern language models increasingly require but do not natively encode. While prior work uses reinforcement learning or test-time training, planning remains external to the model architecture. We formulate reasoning as optimal control and introduce the Test-Time Control (TTC) layer, which performs finite-horizon LQR planning over latent states at inference time, represents a value function within neural architectures, and leverages it as the nested objective to enable planning before prediction. To ensure scalability, we derive a hardware-efficient LQR solver based on a symplectic formulation and implement it as a fused CUDA kernel, enabling parallel execution with minimal overhead. Integrated as an adapter into pretrained LLMs, TTC layers improve mathematical reasoning performance by up to +27.8% on MATH-500 and 2-3x Pass@8 improvements on AMC and AIME, demonstrating that embedding optimal control as an architectural component provides an effective and scalable mechanism for reasoning beyond test-time training.

