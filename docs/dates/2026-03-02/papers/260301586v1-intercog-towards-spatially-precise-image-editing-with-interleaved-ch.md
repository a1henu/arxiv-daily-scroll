---
layout: default
title: InterCoG: Towards Spatially Precise Image Editing with Interleaved Chain-of-Grounding Reasoning
---

# InterCoG: Towards Spatially Precise Image Editing with Interleaved Chain-of-Grounding Reasoning
**arXiv**：[2603.01586v1](https://arxiv.org/abs/2603.01586) · [PDF](https://arxiv.org/pdf/2603.01586.pdf)  
**作者**：Yecong Wan, Fan Li, Chunwei Wang, Hao Wu, Mingwen Shao, Wangmeng Zuo  

**一句话要点**：提出InterCoG框架，通过文本-视觉交错链式推理实现复杂多实体场景下的精细图像编辑

**关键词**：图像编辑, 空间推理, 视觉定位, 多模态学习, 链式推理, 数据集构建

## 3 点简述
- 核心问题：复杂多实体场景中非显著目标的精细编辑需空间推理，现有统一编辑模型面临挑战。
- 方法要点：采用文本位置推理、视觉定位和描述重写三步链式推理，辅以多模态定位监督和对齐训练模块。
- 实验或效果：构建GroundEdit-45K数据集和GroundEdit-Bench评估基准，实验验证在空间复杂场景中实现高精度编辑。

## 摘要（原文）

> Emerging unified editing models have demonstrated strong capabilities in general object editing tasks. However, it remains a significant challenge to perform fine-grained editing in complex multi-entity scenes, particularly those where targets are not visually salient and require spatial reasoning. To this end, we propose InterCoG, a novel text-vision Interleaved Chain-of-Grounding reasoning framework for fine-grained image editing in complex real-world scenes. The key insight of InterCoG is to first perform object position reasoning solely within text that includes spatial relation details to explicitly deduce the location and identity of the edited target. It then conducts visual grounding via highlighting the editing targets with generated bounding boxes and masks in pixel space, and finally rewrites the editing description to specify the intended outcomes. To further facilitate this paradigm, we propose two auxiliary training modules: multimodal grounding reconstruction supervision and multimodal grounding reasoning alignment to enforce spatial localization accuracy and reasoning interpretability, respectively. We also construct GroundEdit-45K, a dataset comprising 45K grounding-oriented editing samples with detailed reasoning annotations, and GroundEdit-Bench for grounding-aware editing evaluation. Extensive experiments substantiate the superiority of our approach in highly precise edits under spatially intricate and multi-entity scenes.

