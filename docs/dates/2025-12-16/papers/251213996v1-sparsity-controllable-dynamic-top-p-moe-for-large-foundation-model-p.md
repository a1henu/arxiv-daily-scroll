---
layout: default
title: Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training
---

# Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training
**arXiv**：[2512.13996v1](https://arxiv.org/abs/2512.13996) · [PDF](https://arxiv.org/pdf/2512.13996.pdf)  
**作者**：Can Jin, Hongwu Peng, Mingcan Xiang, Qixin Zhang, Xiangchi Yuan, Amit Hasan, Ohiremen Dibua, Yifan Gong, Yan Kang, Dimitris N. Metaxas  

**一句话要点**：提出动态Top-p稀疏MoE路由机制，以可控稀疏性优化大模型预训练效率。

**关键词**：稀疏混合专家, 动态路由机制, 大模型预训练, 计算效率优化, PI控制器, 扩散变换器

## 3 点简述
- 标准Top-k路由忽略token难度差异，导致稀疏模式不灵活；Top-p路由固定阈值易失控计算成本。
- 采用PI控制器动态调整概率阈值，实现激活专家稀疏度与目标对齐；引入动态路由归一化，适应层间专家选择模式。
- 在LLM和Diffusion Transformer实验中，DTop-p优于Top-k和固定阈值Top-p，展示强扩展性和资源自适应分配。

## 摘要（原文）

> Sparse Mixture-of-Experts (MoE) architectures effectively scale model capacity by activating only a subset of experts for each input token. However, the standard Top-k routing strategy imposes a uniform sparsity pattern that ignores the varying difficulty of tokens. While Top-p routing offers a flexible alternative, existing implementations typically rely on a fixed global probability threshold, which results in uncontrolled computational costs and sensitivity to hyperparameter selection. In this paper, we propose DTop-p MoE, a sparsity-controllable dynamic Top-p routing mechanism. To resolve the challenge of optimizing a non-differentiable threshold, we utilize a Proportional-Integral (PI) Controller that dynamically adjusts the probability threshold to align the running activated-expert sparsity with a specified target. Furthermore, we introduce a dynamic routing normalization mechanism that adapts layer-wise routing logits, allowing different layers to learn distinct expert-selection patterns while utilizing a global probability threshold. Extensive experiments on Large Language Models and Diffusion Transformers demonstrate that DTop-p consistently outperforms both Top-k and fixed-threshold Top-p baselines. Our analysis confirms that DTop-p maintains precise control over the number of activated experts while adaptively allocating resources across different tokens and layers. Furthermore, DTop-p exhibits strong scaling properties with respect to expert granularity, expert capacity, model size, and dataset size, offering a robust framework for large-scale MoE pre-training.

