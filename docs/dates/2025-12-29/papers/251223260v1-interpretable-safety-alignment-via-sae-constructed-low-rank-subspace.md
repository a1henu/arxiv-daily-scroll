---
layout: default
title: Interpretable Safety Alignment via SAE-Constructed Low-Rank Subspace Adaptation
---

# Interpretable Safety Alignment via SAE-Constructed Low-Rank Subspace Adaptation
**arXiv**：[2512.23260v1](https://arxiv.org/abs/2512.23260) · [PDF](https://arxiv.org/pdf/2512.23260.pdf)  
**作者**：Dianyun Wang, Qingsen Ma, Yuhu Shang, Zhifeng Lu, Lechen Ning, Zhenbo Xu, Huijia Wu, Zhaofeng He  

**一句话要点**：提出基于稀疏自编码器构建可解释低秩子空间的方法，以提升大语言模型安全对齐的透明性与性能。

**关键词**：稀疏自编码器, 低秩适配, 安全对齐, 可解释性, 参数高效微调, 大语言模型

## 3 点简述
- 核心问题：现有低秩适配方法如LoRA在隐式学习子空间时缺乏可解释性，难以直接控制任务相关更新。
- 方法要点：利用预训练稀疏自编码器在解耦特征空间中识别任务相关特征，构建显式可解释低秩子空间指导适配器初始化。
- 实验或效果：在安全对齐任务中达到99.6%安全率，仅更新0.19-0.24%参数，性能接近基于RLHF的方法。

## 摘要（原文）

> Parameter-efficient fine-tuning has become the dominant paradigm for adapting large language models to downstream tasks. Low-rank adaptation methods such as LoRA operate under the assumption that task-relevant weight updates reside in a low-rank subspace, yet this subspace is learned implicitly from data in a black-box manner, offering no interpretability or direct control. We hypothesize that this difficulty stems from polysemanticity--individual dimensions encoding multiple entangled concepts. To address this, we leverage pre-trained Sparse Autoencoders (SAEs) to identify task-relevant features in a disentangled feature space, then construct an explicit, interpretable low-rank subspace to guide adapter initialization. We provide theoretical analysis proving that under monosemanticity assumptions, SAE-based subspace identification achieves arbitrarily small recovery error, while direct identification in polysemantic space suffers an irreducible error floor. On safety alignment, our method achieves up to 99.6% safety rate--exceeding full fine-tuning by 7.4 percentage points and approaching RLHF-based methods--while updating only 0.19-0.24% of parameters. Crucially, our method provides interpretable insights into the learned alignment subspace through the semantic grounding of SAE features. Our work demonstrates that incorporating mechanistic interpretability into the fine-tuning process can simultaneously improve both performance and transparency.

