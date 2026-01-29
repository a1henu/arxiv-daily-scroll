---
layout: default
title: Visual Prompt-Agnostic Evolution
---

# Visual Prompt-Agnostic Evolution
**arXiv**：[2601.20232v1](https://arxiv.org/abs/2601.20232) · [PDF](https://arxiv.org/pdf/2601.20232.pdf)  
**作者**：Junze Wang, Lei Fan, Dezheng Zhang, Weipeng Jing, Donglin Di, Yang Song, Sidong Liu, Cong Cong  

**一句话要点**：提出Prompt-Agnostic Evolution以解决视觉提示调优中的训练不稳定和跨层不匹配问题。

**关键词**：视觉提示调优, 训练稳定性, 频域分析, Koopman算子, Lyapunov正则化, 下游任务适应

## 3 点简述
- 核心问题：现有视觉提示调优方法存在梯度振荡，浅层提示停滞和深层提示高方差导致跨层不匹配。
- 方法要点：从频域角度初始化任务感知提示，使用共享Koopman算子确保跨层一致演化，引入Lyapunov稳定性正则化约束误差放大。
- 实验或效果：在25个数据集上平均加速1.41倍，准确率提升1-3%，无需修改主干网络或推理过程。

## 摘要（原文）

> Visual Prompt Tuning (VPT) adapts a frozen Vision Transformer (ViT) to downstream tasks by inserting a small number of learnable prompt tokens into the token sequence at each layer. However, we observe that existing VPT variants often suffer from unstable training dynamics, characterized by gradient oscillations. A layer-wise analysis reveals that shallow-layer prompts tend to stagnate early, while deeper-layer prompts exhibit high-variance oscillations, leading to cross-layer mismatch. These issues slow convergence and degrade final performance. To address these challenges, we propose Prompt-Agnostic Evolution ($\mathtt{PAE}$), which strengthens vision prompt tuning by explicitly modeling prompt dynamics. From a frequency-domain perspective, we initialize prompts in a task-aware direction by uncovering and propagating frequency shortcut patterns that the backbone inherently exploits for recognition. To ensure coherent evolution across layers, we employ a shared Koopman operator that imposes a global linear transformation instead of uncoordinated, layer-specific updates. Finally, inspired by Lyapunov stability theory, we introduce a regularizer that constrains error amplification during evolution. Extensive experiments show that $\mathtt{PAE}$ accelerates convergence with an average $1.41\times$ speedup and improves accuracy by 1--3% on 25 datasets across multiple downstream tasks. Beyond performance, $\mathtt{PAE}$ is prompt-agnostic and lightweight, and it integrates seamlessly with diverse VPT variants without backbone modification or inference-time changes.

