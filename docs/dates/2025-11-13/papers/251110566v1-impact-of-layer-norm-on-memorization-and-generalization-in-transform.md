---
layout: default
title: Impact of Layer Norm on Memorization and Generalization in Transformers
---

# Impact of Layer Norm on Memorization and Generalization in Transformers
**arXiv**：[2511.10566v1](https://arxiv.org/abs/2511.10566) · [PDF](https://arxiv.org/pdf/2511.10566.pdf)  
**作者**：Rishi Singhal, Jung-Eun Kim  

**一句话要点**：分析LayerNorm对Transformer记忆与泛化的影响，比较Pre-与Post-LayerNorm架构

**关键词**：LayerNorm, Transformer架构, 记忆机制, 泛化性能, 深度学习优化, 视觉与语言数据集

## 3 点简述
- 核心问题：LayerNorm在Pre-和Post-LayerNorm Transformer中对记忆与学习的影响机制未知
- 方法要点：通过消除LayerNorm参数，分析其在稳定学习和记忆中的作用
- 实验或效果：在13个模型和6个数据集上验证，早期层LayerNorm最关键

## 摘要（原文）

> Layer Normalization (LayerNorm) is one of the fundamental components in transformers that stabilizes training and improves optimization. In recent times, Pre-LayerNorm transformers have become the preferred choice over Post-LayerNorm transformers due to their stable gradient flow. However, the impact of LayerNorm on learning and memorization across these architectures remains unclear. In this work, we investigate how LayerNorm influences memorization and learning for Pre- and Post-LayerNorm transformers. We identify that LayerNorm serves as a key factor for stable learning in Pre-LayerNorm transformers, while in Post-LayerNorm transformers, it impacts memorization. Our analysis reveals that eliminating LayerNorm parameters in Pre-LayerNorm models exacerbates memorization and destabilizes learning, while in Post-LayerNorm models, it effectively mitigates memorization by restoring genuine labels. We further precisely identify that early layers LayerNorm are the most critical over middle/later layers and their influence varies across Pre and Post LayerNorm models. We have validated it through 13 models across 6 Vision and Language datasets. These insights shed new light on the role of LayerNorm in shaping memorization and learning in transformers.

