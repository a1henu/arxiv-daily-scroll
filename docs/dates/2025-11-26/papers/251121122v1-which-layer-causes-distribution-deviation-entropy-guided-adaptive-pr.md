---
layout: default
title: Which Layer Causes Distribution Deviation? Entropy-Guided Adaptive Pruning for Diffusion and Flow Models
---

# Which Layer Causes Distribution Deviation? Entropy-Guided Adaptive Pruning for Diffusion and Flow Models
**arXiv**：[2511.21122v1](https://arxiv.org/abs/2511.21122) · [PDF](https://arxiv.org/pdf/2511.21122.pdf)  
**作者**：Changlin Li, Jiawei Zhang, Zeyi Shi, Zongxin Yang, Zhihui Li, Xiaojun Chang  

**一句话要点**：提出EntPruner框架以解决扩散和流模型在下游任务中的参数冗余问题

**关键词**：扩散模型, 流模型, 模型剪枝, 条件熵偏差, 自适应剪枝, 推理加速

## 3 点简述
- 核心问题：预训练扩散和流模型迁移到下游任务时存在显著参数冗余
- 方法要点：使用条件熵偏差指导块级重要性评估，实现零-shot自适应剪枝
- 实验或效果：在DiT和SiT模型上实现最高2.22倍推理加速，保持生成质量

## 摘要（原文）

> Large-scale vision generative models, including diffusion and flow models, have demonstrated remarkable performance in visual generation tasks. However, transferring these pre-trained models to downstream tasks often results in significant parameter redundancy. In this paper, we propose EntPruner, an entropy-guided automatic progressive pruning framework for diffusion and flow models. First, we introduce entropy-guided pruning, a block-level importance assessment strategy specifically designed for generative models. Unlike discriminative models, generative models require preserving the diversity and condition-fidelity of the output distribution. As the importance of each module can vary significantly across downstream tasks, EntPruner prioritizes pruning of less important blocks using data-dependent Conditional Entropy Deviation (CED) as a guiding metric. CED quantifies how much the distribution diverges from the learned conditional data distribution after removing a block. Second, we propose a zero-shot adaptive pruning framework to automatically determine when and how much to prune during training. This dynamic strategy avoids the pitfalls of one-shot pruning, mitigating mode collapse, and preserving model performance. Extensive experiments on DiT and SiT models demonstrate the effectiveness of EntPruner, achieving up to 2.22$\times$ inference speedup while maintaining competitive generation quality on ImageNet and three downstream datasets.

