---
layout: default
title: ReaMIL: Reasoning- and Evidence-Aware Multiple Instance Learning for Whole-Slide Histopathology
---

# ReaMIL: Reasoning- and Evidence-Aware Multiple Instance Learning for Whole-Slide Histopathology
**arXiv**：[2601.10073v1](https://arxiv.org/abs/2601.10073) · [PDF](https://arxiv.org/pdf/2601.10073.pdf)  
**作者**：Hyun Do Jung, Jungwon Choi, Hwiyoung Kim  

**一句话要点**：提出ReaMIL方法，通过轻量选择头和预算充分性目标，在组织病理学全切片图像中实现高效证据选择的多实例学习。

**关键词**：多实例学习, 组织病理学全切片分析, 证据选择, 预算充分性目标, 软门控, 定量评估

## 3 点简述
- 核心问题：全切片组织病理学分析中，多实例学习需要从大量图像块中高效选择关键证据，同时保持分类性能。
- 方法要点：在强MIL骨干网络上添加轻量选择头，使用预算充分性目标训练，通过软门控和稀疏预算生成紧凑证据集。
- 实验或效果：在TCGA-NSCLC等数据集上，ReaMIL匹配或略提升基线AUC，提供定量证据效率诊断，如平均最小充分K约8.2个图像块。

## 摘要（原文）

> We introduce ReaMIL (Reasoning- and Evidence-Aware MIL), a multiple instance learning approach for whole-slide histopathology that adds a light selection head to a strong MIL backbone. The head produces soft per-tile gates and is trained with a budgeted-sufficiency objective: a hinge loss that enforces the true-class probability to be $\geq τ$ using only the kept evidence, under a sparsity budget on the number of selected tiles. The budgeted-sufficiency objective yields small, spatially compact evidence sets without sacrificing baseline performance. Across TCGA-NSCLC (LUAD vs. LUSC), TCGA-BRCA (IDC vs. Others), and PANDA, ReaMIL matches or slightly improves baseline AUC and provides quantitative evidence-efficiency diagnostics. On NSCLC, it attains AUC 0.983 with a mean minimal sufficient K (MSK) $\approx 8.2$ tiles at $τ= 0.90$ and AUKC $\approx 0.864$, showing that class confidence rises sharply and stabilizes once a small set of tiles is kept. The method requires no extra supervision, integrates seamlessly with standard MIL training, and naturally yields slide-level overlays. We report accuracy alongside MSK, AUKC, and contiguity for rigorous evaluation of model behavior on WSIs.

