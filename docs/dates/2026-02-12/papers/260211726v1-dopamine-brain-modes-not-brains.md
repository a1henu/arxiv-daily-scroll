---
layout: default
title: Dopamine: Brain Modes, Not Brains
---

# Dopamine: Brain Modes, Not Brains
**arXiv**：[2602.11726v1](https://arxiv.org/abs/2602.11726) · [PDF](https://arxiv.org/pdf/2602.11726.pdf)  
**作者**：Shervin Ghasemlou  

**一句话要点**：提出Dopamine方法，通过激活空间参数高效微调实现任务模式切换

**关键词**：参数高效微调, 激活空间学习, 神经元门控, 模式切换, 可解释性

## 3 点简述
- 核心问题：传统权重空间微调方法如LoRA难以解释内部计算重用机制
- 方法要点：冻结基础权重，学习神经元阈值和增益，通过门控选择激活参与
- 实验或效果：在旋转MNIST任务中，以少量参数提升准确率，实现部分激活稀疏性

## 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) methods such as \lora{} adapt large pretrained models by adding small weight-space updates. While effective, weight deltas are hard to interpret mechanistically, and they do not directly expose \emph{which} internal computations are reused versus bypassed for a new task. We explore an alternative view inspired by neuromodulation: adaptation as a change in \emph{mode} -- selecting and rescaling existing computations -- rather than rewriting the underlying weights. We propose \methodname{}, a simple activation-space PEFT technique that freezes base weights and learns per-neuron \emph{thresholds} and \emph{gains}. During training, a smooth gate decides whether a neuron's activation participates; at inference the gate can be hardened to yield explicit conditional computation and neuron-level attributions.
>   As a proof of concept, we study ``mode specialization'' on MNIST (0$^\circ$) versus rotated MNIST (45$^\circ$). We pretrain a small MLP on a 50/50 mixture (foundation), freeze its weights, and then specialize to the rotated mode using \methodname{}. Across seeds, \methodname{} improves rotated accuracy over the frozen baseline while using only a few hundred trainable parameters per layer, and exhibits partial activation sparsity (a minority of units strongly active). Compared to \lora{}, \methodname{} trades some accuracy for substantially fewer trainable parameters and a more interpretable ``which-neurons-fire'' mechanism. We discuss limitations, including reduced expressivity when the frozen base lacks features needed for the target mode.

