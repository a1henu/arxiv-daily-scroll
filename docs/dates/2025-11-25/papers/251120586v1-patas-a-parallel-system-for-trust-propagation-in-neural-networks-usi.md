---
layout: default
title: PaTAS: A Parallel System for Trust Propagation in Neural Networks Using Subjective Logic
---

# PaTAS: A Parallel System for Trust Propagation in Neural Networks Using Subjective Logic
**arXiv**：[2511.20586v1](https://arxiv.org/abs/2511.20586) · [PDF](https://arxiv.org/pdf/2511.20586.pdf)  
**作者**：Koffi Ismael Ouattara, Ioannis Krontiris, Theo Dimitrakos, Dennis Eisermann, Frank Kargl  

**一句话要点**：提出PaTAS并行系统，使用主观逻辑在神经网络中传播信任以评估模型可靠性

**关键词**：信任传播, 主观逻辑, 神经网络可靠性, 并行系统, 对抗鲁棒性, 不确定性评估

## 3 点简述
- 核心问题：传统指标如准确率无法捕捉模型预测的不确定性和可靠性，尤其在对抗或退化条件下
- 方法要点：通过信任节点和信任函数并行传播输入、参数和激活信任，定义参数信任更新和推理路径信任评估
- 实验或效果：在真实和对抗数据集上，PaTAS产生可解释、对称和收敛的信任估计，区分良性输入和对抗输入

## 摘要（原文）

> Trustworthiness has become a key requirement for the deployment of artificial intelligence systems in safety-critical applications. Conventional evaluation metrics such as accuracy and precision fail to capture uncertainty or the reliability of model predictions, particularly under adversarial or degraded conditions. This paper introduces the \emph{Parallel Trust Assessment System (PaTAS)}, a framework for modeling and propagating trust in neural networks using Subjective Logic (SL). PaTAS operates in parallel with standard neural computation through \emph{Trust Nodes} and \emph{Trust Functions} that propagate input, parameter, and activation trust across the network. The framework defines a \emph{Parameter Trust Update} mechanism to refine parameter reliability during training and an \emph{Inference-Path Trust Assessment (IPTA)} method to compute instance-specific trust at inference. Experiments on real-world and adversarial datasets demonstrate that PaTAS produces interpretable, symmetric, and convergent trust estimates that complement accuracy and expose reliability gaps in poisoned, biased, or uncertain data scenarios. The results show that PaTAS effectively distinguishes between benign and adversarial inputs and identifies cases where model confidence diverges from actual reliability. By enabling transparent and quantifiable trust reasoning within neural architectures, PaTAS provides a principled foundation for evaluating model reliability across the AI lifecycle.

