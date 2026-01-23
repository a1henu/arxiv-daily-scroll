---
layout: default
title: Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot Compositional Action Recognition
---

# Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot Compositional Action Recognition
**arXiv**：[2601.16211v1](https://arxiv.org/abs/2601.16211) · [PDF](https://arxiv.org/pdf/2601.16211.pdf)  
**作者**：Geo Ahn, Inwoong Lee, Taeoh Kim, Minho Shim, Dongyoon Wee, Jinwoo Choi  

**一句话要点**：提出RCORE框架以缓解零样本组合动作识别中的对象驱动动词捷径问题

**关键词**：零样本组合动作识别, 对象驱动捷径, 组合视频理解, 时间顺序正则化, 组合感知增强

## 3 点简述
- 核心问题：现有ZS-CAR模型因组合监督稀疏性和动词-对象学习难度不对称，过度依赖共现统计，忽略视觉证据。
- 方法要点：RCORE通过组合感知增强和时间顺序正则化损失，强制基于时间的动词学习，减少捷径行为。
- 实验或效果：在Sth-com和EK100-com基准上，RCORE显著提升未见组合准确率，降低共现偏差依赖，实现稳定正组合差距。

## 摘要（原文）

> We study Compositional Video Understanding (CVU), where models must recognize verbs and objects and compose them to generalize to unseen combinations. We find that existing Zero-Shot Compositional Action Recognition (ZS-CAR) models fail primarily due to an overlooked failure mode: object-driven verb shortcuts. Through systematic analysis, we show that this behavior arises from two intertwined factors: severe sparsity and skewness of compositional supervision, and the asymmetric learning difficulty between verbs and objects. As training progresses, the existing ZS-CAR model increasingly ignores visual evidence and overfits to co-occurrence statistics. Consequently, the existing model does not gain the benefit of compositional recognition in unseen verb-object compositions. To address this, we propose RCORE, a simple and effective framework that enforces temporally grounded verb learning. RCORE introduces (i) a composition-aware augmentation that diversifies verb-object combinations without corrupting motion cues, and (ii) a temporal order regularization loss that penalizes shortcut behaviors by explicitly modeling temporal structure. Across two benchmarks, Sth-com and our newly constructed EK100-com, RCORE significantly improves unseen composition accuracy, reduces reliance on co-occurrence bias, and achieves consistently positive compositional gaps. Our findings reveal object-driven shortcuts as a critical limiting factor in ZS-CAR and demonstrate that addressing them is essential for robust compositional video understanding.

