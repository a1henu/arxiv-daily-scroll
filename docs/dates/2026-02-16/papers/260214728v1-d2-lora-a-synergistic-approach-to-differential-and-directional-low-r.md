---
layout: default
title: D2-LoRA: A Synergistic Approach to Differential and Directional Low-Rank Adaptation
---

# D2-LoRA: A Synergistic Approach to Differential and Directional Low-Rank Adaptation
**arXiv**：[2602.14728v1](https://arxiv.org/abs/2602.14728) · [PDF](https://arxiv.org/pdf/2602.14728.pdf)  
**作者**：Nozomu Fujisawa, Masaaki Kondo  

**一句话要点**：提出D2-LoRA，结合符号低秩残差更新与列投影，在数据受限下高效微调并保持推理合并性。

**关键词**：参数高效微调, 低秩适应, 符号残差更新, 列投影, 推理合并, 训练稳定性

## 3 点简述
- 核心问题：在数据与计算受限下，探索参数高效微调设计空间，提升性能与稳定性。
- 方法要点：结合带符号的低秩残差更新和训练时列投影，保持代数可合并性，减少推理延迟。
- 实验或效果：在问答和阅读理解任务上平均准确率达76.4%，训练波动降低36%，推理吞吐提升约1.91倍。

## 摘要（原文）

> We systematically investigate the parameter-efficient fine-tuning design space under practical data and compute constraints, and propose D2-LoRA. D2-LoRA achieves 76.4 percent average accuracy across eight question answering and reading comprehension benchmarks using only 5k training samples per task and two epochs, while preserving algebraic mergeability at inference with near-exact numerical equivalence. The method combines signed low-rank residual updates with additive and subtractive components, together with a train-time column-wise projection that keeps each column close to its original norm. After training, the adapter is merged into a single weight matrix, adding zero inference latency. Compared with LoRA, D2-LoRA improves average accuracy by 2.2 percentage points; at matched parameter counts (LoRA rank 2r versus D2-LoRA rank r), the improvement is 1.6 points, indicating gains from architectural design rather than increased parameterization. Compared with DoRA, it matches or exceeds performance on most tasks. Beyond QA and reading comprehension, D2-LoRA improves generative tasks (plus 1.2 ROUGE-L and plus 1.1 percent win rate) and shows 36 percent lower training volatility. The merge preserves numerical fidelity (mean gap about 0.03 percentage points) and recovers about 1.91x evaluation throughput. Training overhead is 19 percent, comparable to DoRA, and decreases with longer input sequences. We provide a geometric analysis explaining how the projection stabilizes training, together with ablation studies isolating the contribution of each design component.

