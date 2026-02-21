---
layout: default
title: Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning
---

# Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning
**arXiv**：[2602.17546v1](https://arxiv.org/abs/2602.17546) · [PDF](https://arxiv.org/pdf/2602.17546.pdf)  
**作者**：Jyotin Goel, Souvik Maji, Pratik Mazumder  

**一句话要点**：提出自适应正则化框架以解决指令微调中安全行为退化问题

**关键词**：语言模型安全, 自适应正则化, 微调防御, 风险估计, 安全对齐

## 3 点简述
- 核心问题：指令微调可能导致语言模型安全行为退化，现有防御方法在安全与效用间存在权衡
- 方法要点：通过安全风险估计（基于评判器或激活分类器）自适应调整正则化强度，约束高风险更新
- 实验或效果：在多种模型和攻击场景下降低攻击成功率，保持下游性能，无推理开销

## 摘要（原文）

> Instruction-following language models are trained to be helpful and safe, yet their safety behavior can deteriorate under benign fine-tuning and worsen under adversarial updates. Existing defenses often offer limited protection or force a trade-off between safety and utility. We introduce a training framework that adapts regularization in response to safety risk, enabling models to remain aligned throughout fine-tuning. To estimate safety risk at training time, we explore two distinct approaches: a judge-based Safety Critic that assigns high-level harm scores to training batches, and an activation-based risk predictor built with a lightweight classifier trained on intermediate model activations to estimate harmful intent. Each approach provides a risk signal that is used to constrain updates deemed higher risk to remain close to a safe reference policy, while lower-risk updates proceed with standard training. We empirically verify that harmful intent signals are predictable from pre-generation activations and that judge scores provide effective high-recall safety guidance. Across multiple model families and attack scenarios, adaptive regularization with either risk estimation approach consistently lowers attack success rate compared to standard fine-tuning, preserves downstream performance, and adds no inference-time cost. This work demonstrates a principled mechanism for maintaining safety without sacrificing utility.

