---
layout: default
title: EW-DETR: Evolving World Object Detection via Incremental Low-Rank DEtection TRansformer
---

# EW-DETR: Evolving World Object Detection via Incremental Low-Rank DEtection TRansformer
**arXiv**：[2602.20985v1](https://arxiv.org/abs/2602.20985) · [PDF](https://arxiv.org/pdf/2602.20985.pdf)  
**作者**：Munish Monga, Vishal Chudasama, Pankaj Wasnik, C. V. Jawahar  

**一句话要点**：提出EW-DETR框架以解决演化世界中的目标检测问题，结合增量学习、领域适应和未知检测。

**关键词**：演化世界目标检测, 增量学习, 领域适应, 未知检测, DETR框架, FOGS评估

## 3 点简述
- 核心问题：现实世界目标检测需在演化环境中处理新类、领域偏移和未知对象，且无先验数据访问。
- 方法要点：基于DETR，引入增量LoRA适配器、查询范数对象性适配器和熵感知未知混合模块。
- 实验或效果：在Pascal Series和Diverse Weather基准上，EW-DETR优于其他方法，FOGS分数提升57.24%。

## 摘要（原文）

> Real-world object detection must operate in evolving environments where new classes emerge, domains shift, and unseen objects must be identified as "unknown": all without accessing prior data. We introduce Evolving World Object Detection (EWOD), a paradigm coupling incremental learning, domain adaptation, and unknown detection under exemplar-free constraints. To tackle EWOD, we propose EW-DETR framework that augments DETR-based detectors with three synergistic modules: Incremental LoRA Adapters for exemplar-free incremental learning under evolving domains; a Query-Norm Objectness Adapter that decouples objectness-aware features from DETR decoder queries; and Entropy-Aware Unknown Mixing for calibrated unknown detection. This framework generalises across DETR-based detectors, enabling state-of-the-art RF-DETR to operate effectively in evolving-world settings. We also introduce FOGS (Forgetting, Openness, Generalisation Score) to holistically evaluate performance across these dimensions. Extensive experiments on Pascal Series and Diverse Weather benchmarks show EW-DETR outperforms other methods, improving FOGS by 57.24%.

