---
layout: default
title: Rethinking Infrared Small Target Detection: A Foundation-Driven Efficient Paradigm
---

# Rethinking Infrared Small Target Detection: A Foundation-Driven Efficient Paradigm
**arXiv**：[2512.05511v1](https://arxiv.org/abs/2512.05511) · [PDF](https://arxiv.org/pdf/2512.05511.pdf)  
**作者**：Chuang Yu, Jinmiao Zhao, Yunpeng Liu, Yaokun Li, Xiujun Shu, Yuanhao Feng, Bo Wang, Yimian Dai, Xiangyu Yue  

**一句话要点**：提出基础驱动高效范式，首次将视觉基础模型冻结表示引入单帧红外小目标检测，提升精度且无额外推理开销。

**关键词**：红外小目标检测, 视觉基础模型, 语义对齐融合, 隐式自蒸馏, 评估指标统一

## 3 点简述
- 核心问题：视觉基础模型在单帧红外小目标检测中的应用潜力未充分探索，现有方法缺乏高效集成。
- 方法要点：设计语义对齐调制融合模块实现全局语义先验与任务特征的动态对齐与深度融合。
- 实验或效果：在多个公开数据集上实现最先进性能，并通过协同优化隐式自蒸馏策略避免推理负担。

## 摘要（原文）

> While large-scale visual foundation models (VFMs) exhibit strong generalization across diverse visual domains, their potential for single-frame infrared small target (SIRST) detection remains largely unexplored. To fill this gap, we systematically introduce the frozen representations from VFMs into the SIRST task for the first time and propose a Foundation-Driven Efficient Paradigm (FDEP), which can seamlessly adapt to existing encoder-decoder-based methods and significantly improve accuracy without additional inference overhead. Specifically, a Semantic Alignment Modulation Fusion (SAMF) module is designed to achieve dynamic alignment and deep fusion of the global semantic priors from VFMs with task-specific features. Meanwhile, to avoid the inference time burden introduced by VFMs, we propose a Collaborative Optimization-based Implicit Self-Distillation (CO-ISD) strategy, which enables implicit semantic transfer between the main and lightweight branches through parameter sharing and synchronized backpropagation. In addition, to unify the fragmented evaluation system, we construct a Holistic SIRST Evaluation (HSE) metric that performs multi-threshold integral evaluation at both pixel-level confidence and target-level robustness, providing a stable and comprehensive basis for fair model comparison. Extensive experiments demonstrate that the SIRST detection networks equipped with our FDEP framework achieve state-of-the-art (SOTA) performance on multiple public datasets. Our code is available at https://github.com/YuChuang1205/FDEP-Framework

