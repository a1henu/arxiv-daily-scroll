---
layout: default
title: FlowDet: Unifying Object Detection and Generative Transport Flows
---

# FlowDet: Unifying Object Detection and Generative Transport Flows
**arXiv**：[2512.16771v1](https://arxiv.org/abs/2512.16771) · [PDF](https://arxiv.org/pdf/2512.16771.pdf)  
**作者**：Enis Baty, C. P. Bridges, Simon Hadfield  

**一句话要点**：提出FlowDet，首次将条件流匹配技术应用于目标检测，统一检测与生成式传输流。

**关键词**：目标检测, 条件流匹配, 生成式传输, 推理效率, COCO数据集, LVIS数据集

## 3 点简述
- 核心问题：将目标检测重新表述为生成式传输问题，替代扩散模型的随机路径。
- 方法要点：使用条件流匹配学习更直、更简单的传输路径，支持可变框数和推理步数。
- 实验或效果：在COCO和LVIS数据集上，AP提升达+3.6%，AP$_{rare}$提升达+4.2%。

## 摘要（原文）

> We present FlowDet, the first formulation of object detection using modern Conditional Flow Matching techniques. This work follows from DiffusionDet, which originally framed detection as a generative denoising problem in the bounding box space via diffusion. We revisit and generalise this formulation to a broader class of generative transport problems, while maintaining the ability to vary the number of boxes and inference steps without re-training. In contrast to the curved stochastic transport paths induced by diffusion, FlowDet learns simpler and straighter paths resulting in faster scaling of detection performance as the number of inference steps grows. We find that this reformulation enables us to outperform diffusion based detection systems (as well as non-generative baselines) across a wide range of experiments, including various precision/recall operating points using multiple feature backbones and datasets. In particular, when evaluating under recall-constrained settings, we can highlight the effects of the generative transport without over-compensating with large numbers of proposals. This provides gains of up to +3.6% AP and +4.2% AP$_{rare}$ over DiffusionDet on the COCO and LVIS datasets, respectively.

