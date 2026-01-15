---
layout: default
title: Integrating Diverse Assignment Strategies into DETRs
---

# Integrating Diverse Assignment Strategies into DETRs
**arXiv**：[2601.09247v1](https://arxiv.org/abs/2601.09247) · [PDF](https://arxiv.org/pdf/2601.09247.pdf)  
**作者**：Yiwei Zhang, Jin Gao, Hanshi Wang, Fudong Ge, Guan Luo, Weiming Hu, Zhipeng Zhang  

**一句话要点**：提出LoRA-DETR框架，通过集成多样分配策略解决DETR类检测器收敛慢问题。

**关键词**：目标检测, DETR框架, 标签分配, 低秩适应, 一对多监督, 模型优化

## 3 点简述
- 核心问题：DETR类检测器的一对一匹配策略导致监督稀疏和收敛缓慢。
- 方法要点：在训练时添加多个LoRA分支，每个分支实现不同的一对多分配规则，以注入多样监督梯度。
- 实验或效果：在不同基准上验证有效性，实现先进性能且不增加推理计算成本。

## 摘要（原文）

> Label assignment is a critical component in object detectors, particularly within DETR-style frameworks where the one-to-one matching strategy, despite its end-to-end elegance, suffers from slow convergence due to sparse supervision. While recent works have explored one-to-many assignments to enrich supervisory signals, they often introduce complex, architecture-specific modifications and typically focus on a single auxiliary strategy, lacking a unified and scalable design. In this paper, we first systematically investigate the effects of ``one-to-many'' supervision and reveal a surprising insight that performance gains are driven not by the sheer quantity of supervision, but by the diversity of the assignment strategies employed. This finding suggests that a more elegant, parameter-efficient approach is attainable. Building on this insight, we propose LoRA-DETR, a flexible and lightweight framework that seamlessly integrates diverse assignment strategies into any DETR-style detector. Our method augments the primary network with multiple Low-Rank Adaptation (LoRA) branches during training, each instantiating a different one-to-many assignment rule. These branches act as auxiliary modules that inject rich, varied supervisory gradients into the main model and are discarded during inference, thus incurring no additional computational cost. This design promotes robust joint optimization while maintaining the architectural simplicity of the original detector. Extensive experiments on different baselines validate the effectiveness of our approach. Our work presents a new paradigm for enhancing detectors, demonstrating that diverse ``one-to-many'' supervision can be integrated to achieve state-of-the-art results without compromising model elegance.

