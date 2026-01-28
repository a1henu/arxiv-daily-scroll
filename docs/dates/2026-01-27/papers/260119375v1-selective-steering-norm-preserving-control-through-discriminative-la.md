---
layout: default
title: Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection
---

# Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection
**arXiv**：[2601.19375v1](https://arxiv.org/abs/2601.19375) · [PDF](https://arxiv.org/pdf/2601.19375.pdf)  
**作者**：Quy-Anh Dang, Chris Ngo  

**一句话要点**：提出选择性转向方法，通过判别层选择和规范保持旋转解决大语言模型推理时控制问题。

**关键词**：大语言模型对齐, 激活转向, 推理时干预, 规范保持控制, 判别层选择, 行为修改

## 3 点简述
- 核心问题：现有激活转向方法存在规范变化或控制不连续，导致模型行为不稳定或生成崩溃。
- 方法要点：引入规范保持旋转公式和判别层选择，仅在特征表示对齐相反的层应用转向，确保激活分布完整性。
- 实验或效果：在九个模型上实现攻击成功率提升5.5倍，保持零困惑度违规和约100%能力保留。

## 摘要（原文）

> Despite significant progress in alignment, large language models (LLMs) remain vulnerable to adversarial attacks that elicit harmful behaviors. Activation steering techniques offer a promising inference-time intervention approach, but existing methods suffer from critical limitations: activation addition requires careful coefficient tuning and is sensitive to layer-specific norm variations, while directional ablation provides only binary control. Recent work on Angular Steering introduces continuous control via rotation in a 2D subspace, but its practical implementation violates norm preservation, causing distribution shift and generation collapse, particularly in models below 7B parameters. We propose Selective Steering, which addresses these limitations through two key innovations: (1) a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity, and (2) discriminative layer selection that applies steering only where feature representations exhibit opposite-signed class alignment. Experiments across nine models demonstrate that Selective Steering achieves 5.5x higher attack success rates than prior methods while maintaining zero perplexity violations and approximately 100\% capability retention on standard benchmarks. Our approach provides a principled, efficient framework for controllable and stable LLM behavior modification. Code: https://github.com/knoveleng/steering

