---
layout: default
title: Context Determines Optimal Architecture in Materials Segmentation
---

# Context Determines Optimal Architecture in Materials Segmentation
**arXiv**：[2602.04154v1](https://arxiv.org/abs/2602.04154) · [PDF](https://arxiv.org/pdf/2602.04154.pdf)  
**作者**：Mingjian Lu, Pawan K. Tripathi, Mark Shteyn, Debargha Ganguly, Roger H. French, Vipin Chaudhary, Yinghui Wu  

**一句话要点**：提出跨模态评估框架以解决材料图像分割中架构选择依赖上下文的问题

**关键词**：材料图像分割, 跨模态评估, 架构选择, 成像模态, 可靠性信号, 可解释性工具

## 3 点简述
- 核心问题：传统分割架构基准测试基于单一成像模态，忽略部署中性能变化，导致最优架构因模态而异
- 方法要点：开发跨模态评估框架，涵盖SEM、AFM、XCT和光学显微镜，评估六种编码器-解码器组合在七个数据集上的表现
- 实验或效果：发现最优架构随上下文系统变化，如UNet在高对比度2D成像中表现最佳，DeepLabv3+在困难案例中更优

## 摘要（原文）

> Segmentation architectures are typically benchmarked on single imaging modalities, obscuring deployment-relevant performance variations: an architecture optimal for one modality may underperform on another. We present a cross-modal evaluation framework for materials image segmentation spanning SEM, AFM, XCT, and optical microscopy. Our evaluation of six encoder-decoder combinations across seven datasets reveals that optimal architectures vary systematically by context: UNet excels for high-contrast 2D imaging while DeepLabv3+ is preferred for the hardest cases. The framework also provides deployment feedback via out-of-distribution detection and counterfactual explanations that reveal which microstructural features drive predictions. Together, the architecture guidance, reliability signals, and interpretability tools address a practical gap in materials characterization, where researchers lack tools to select architectures for their specific imaging setup or assess when models can be trusted on new samples.

