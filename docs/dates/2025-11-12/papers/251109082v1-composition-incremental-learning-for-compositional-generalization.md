---
layout: default
title: Composition-Incremental Learning for Compositional Generalization
---

# Composition-Incremental Learning for Compositional Generalization
**arXiv**：[2511.09082v1](https://arxiv.org/abs/2511.09082) · [PDF](https://arxiv.org/pdf/2511.09082.pdf)  
**作者**：Zhen Li, Yuwei Wu, Chenchen Jing, Che Sun, Chuanhao Li, Yunde Jia  

**一句话要点**：提出伪重放框架以解决组合零样本学习中的增量学习问题

**关键词**：组合增量学习, 组合零样本学习, 视觉合成器, 语言基元蒸馏, 组合泛化, 伪重放框架

## 3 点简述
- 核心问题：现实数据不断涌现，组合无限且长尾，需模型持续提升组合泛化能力
- 方法要点：使用视觉合成器合成已学组合表示，结合语言基元蒸馏保持表示对齐
- 实验或效果：在MIT-States-CompIL和C-GQA-CompIL基准上验证框架有效性

## 摘要（原文）

> Compositional generalization has achieved substantial progress in computer vision on pre-collected training data. Nonetheless, real-world data continually emerges, with possible compositions being nearly infinite, long-tailed, and not entirely visible. Thus, an ideal model is supposed to gradually improve the capability of compositional generalization in an incremental manner. In this paper, we explore Composition-Incremental Learning for Compositional Generalization (CompIL) in the context of the compositional zero-shot learning (CZSL) task, where models need to continually learn new compositions, intending to improve their compositional generalization capability progressively. To quantitatively evaluate CompIL, we develop a benchmark construction pipeline leveraging existing datasets, yielding MIT-States-CompIL and C-GQA-CompIL. Furthermore, we propose a pseudo-replay framework utilizing a visual synthesizer to synthesize visual representations of learned compositions and a linguistic primitive distillation mechanism to maintain aligned primitive representations across the learning process. Extensive experiments demonstrate the effectiveness of the proposed framework.

