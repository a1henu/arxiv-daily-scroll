---
layout: default
title: Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion
---

# Trifuse: Enhancing Attention-Based GUI Grounding via Multimodal Fusion
**arXiv**：[2602.06351v1](https://arxiv.org/abs/2602.06351) · [PDF](https://arxiv.org/pdf/2602.06351.pdf)  
**作者**：Longhui Ma, Di Zhao, Siwei Wang, Zhao Lv, Miao Wang  

**一句话要点**：提出Trifuse框架，通过多模态融合增强基于注意力的GUI定位，减少对标注数据的依赖。

**关键词**：GUI定位, 多模态融合, 注意力机制, 空间锚点, 无监督学习

## 3 点简述
- 核心问题：现有基于注意力的GUI定位方法因缺乏显式空间锚点而可靠性低。
- 方法要点：Trifuse融合注意力、OCR文本和图标语义，采用共识-单峰策略提升定位精度。
- 实验或效果：在四个基准测试中表现优异，无需任务特定微调，降低数据需求。

## 摘要（原文）

> GUI grounding maps natural language instructions to the correct interface elements, serving as the perception foundation for GUI agents. Existing approaches predominantly rely on fine-tuning multimodal large language models (MLLMs) using large-scale GUI datasets to predict target element coordinates, which is data-intensive and generalizes poorly to unseen interfaces. Recent attention-based alternatives exploit localization signals in MLLMs attention mechanisms without task-specific fine-tuning, but suffer from low reliability due to the lack of explicit and complementary spatial anchors in GUI images. To address this limitation, we propose Trifuse, an attention-based grounding framework that explicitly integrates complementary spatial anchors. Trifuse integrates attention, OCR-derived textual cues, and icon-level caption semantics via a Consensus-SinglePeak (CS) fusion strategy that enforces cross-modal agreement while retaining sharp localization peaks. Extensive evaluations on four grounding benchmarks demonstrate that Trifuse achieves strong performance without task-specific fine-tuning, substantially reducing the reliance on expensive annotated data. Moreover, ablation studies reveal that incorporating OCR and caption cues consistently improves attention-based grounding performance across different backbones, highlighting its effectiveness as a general framework for GUI grounding.

