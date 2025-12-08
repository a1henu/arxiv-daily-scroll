---
layout: default
title: Sparse Attention Post-Training for Mechanistic Interpretability
---

# Sparse Attention Post-Training for Mechanistic Interpretability
**arXiv**：[2512.05865v1](https://arxiv.org/abs/2512.05865) · [PDF](https://arxiv.org/pdf/2512.05865.pdf)  
**作者**：Florent Draye, Anson Lei, Ingmar Posner, Bernhard Schölkopf  

**一句话要点**：提出后训练稀疏注意力方法，以提升Transformer的机制可解释性而不牺牲性能。

**关键词**：稀疏注意力, 机制可解释性, 后训练正则化, Transformer结构简化, 计算冗余分析

## 3 点简述
- 核心问题：Transformer注意力冗余，影响模型可解释性，需在保持性能下简化结构。
- 方法要点：通过约束损失目标下的灵活稀疏正则化，后训练使注意力稀疏化至约0.3%边连接。
- 实验或效果：在高达10亿参数模型上验证，保留预训练损失，实现全局电路简化，任务电路组件减少达100倍。

## 摘要（原文）

> We introduce a simple post-training method that makes transformer attention sparse without sacrificing performance. Applying a flexible sparsity regularisation under a constrained-loss objective, we show on models up to 1B parameters that it is possible to retain the original pretraining loss while reducing attention connectivity to $\approx 0.3 \%$ of its edges. Unlike sparse-attention methods designed for computational efficiency, our approach leverages sparsity as a structural prior: it preserves capability while exposing a more organized and interpretable connectivity pattern. We find that this local sparsity cascades into global circuit simplification: task-specific circuits involve far fewer components (attention heads and MLPs) with up to 100x fewer edges connecting them. These results demonstrate that transformer attention can be made orders of magnitude sparser, suggesting that much of its computation is redundant and that sparsity may serve as a guiding principle for more structured and interpretable models.

