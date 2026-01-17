---
layout: default
title: ReaMIL: Reasoning- and Evidence-Aware Multiple Instance Learning for Whole-Slide Histopathology
---

# ReaMIL: Reasoning- and Evidence-Aware Multiple Instance Learning for Whole-Slide Histopathology
**arXiv**：[2601.10073v1](https://arxiv.org/abs/2601.10073) · [PDF](https://arxiv.org/pdf/2601.10073.pdf)  
**作者**：Hyun Do Jung, Jungwon Choi, Hwiyoung Kim  

**一句话要点**：提出ReaMIL方法，通过轻量选择头和预算充足目标优化全切片病理学中的多实例学习。

**关键词**：全切片病理学, 多实例学习, 证据选择, 预算充足目标, 软门控, AUC评估

## 3 点简述
- 核心问题：全切片病理学中多实例学习需高效选择关键图块作为证据，避免冗余计算。
- 方法要点：在强MIL骨干上添加选择头，使用预算充足目标训练，生成软门控和紧凑证据集。
- 实验或效果：在多个数据集上匹配或提升基线AUC，提供证据效率诊断，如NSCLC中AUC达0.983，平均最小足够图块数约8.2。

## 摘要（原文）

> We introduce ReaMIL (Reasoning- and Evidence-Aware MIL), a multiple instance learning approach for whole-slide histopathology that adds a light selection head to a strong MIL backbone. The head produces soft per-tile gates and is trained with a budgeted-sufficiency objective: a hinge loss that enforces the true-class probability to be $\geq τ$ using only the kept evidence, under a sparsity budget on the number of selected tiles. The budgeted-sufficiency objective yields small, spatially compact evidence sets without sacrificing baseline performance. Across TCGA-NSCLC (LUAD vs. LUSC), TCGA-BRCA (IDC vs. Others), and PANDA, ReaMIL matches or slightly improves baseline AUC and provides quantitative evidence-efficiency diagnostics. On NSCLC, it attains AUC 0.983 with a mean minimal sufficient K (MSK) $\approx 8.2$ tiles at $τ= 0.90$ and AUKC $\approx 0.864$, showing that class confidence rises sharply and stabilizes once a small set of tiles is kept. The method requires no extra supervision, integrates seamlessly with standard MIL training, and naturally yields slide-level overlays. We report accuracy alongside MSK, AUKC, and contiguity for rigorous evaluation of model behavior on WSIs.

