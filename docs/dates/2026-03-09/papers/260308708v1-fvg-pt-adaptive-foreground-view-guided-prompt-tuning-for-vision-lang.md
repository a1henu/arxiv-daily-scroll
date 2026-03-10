---
layout: default
title: FVG-PT: Adaptive Foreground View-Guided Prompt Tuning for Vision-Language Models
---

# FVG-PT: Adaptive Foreground View-Guided Prompt Tuning for Vision-Language Models
**arXiv**：[2603.08708v1](https://arxiv.org/abs/2603.08708) · [PDF](https://arxiv.org/pdf/2603.08708.pdf)  
**作者**：Haoyang Li, Liang Wang, Siyu Zhou, Jiacheng Sun, Jing Jiang, Chao Wang, Guodong Long, Yan Peng  

**一句话要点**：提出自适应前景视图引导提示调优方法，以缓解视觉语言模型在调优过程中的前景注意力偏移问题。

**关键词**：视觉语言模型, 提示调优, 注意力机制, 前景引导, 自适应模块, 蒸馏补偿

## 3 点简述
- 核心问题：现有提示调优方法忽视视觉编码器内部注意力表示变化，导致预测失败。
- 方法要点：引入可学习前景可靠性门、前景蒸馏补偿模块和先验校准模块，自适应引导视觉注意力。
- 实验或效果：在多个骨干模型和数据集上验证了方法的有效性和兼容性，代码已开源。

## 摘要（原文）

> CLIP-based prompt tuning enables pretrained Vision-Language Models (VLMs) to efficiently adapt to downstream tasks. Although existing studies have made significant progress, they pay limited attention to changes in the internal attention representations of VLMs during the tuning process. In this paper, we attribute the failure modes of prompt tuning predictions to shifts in foreground attention of the visual encoder, and propose Foreground View-Guided Prompt Tuning (FVG-PT), an adaptive plug-and-play foreground attention guidance module, to alleviate the shifts. Concretely, FVG-PT introduces a learnable Foreground Reliability Gate to automatically enhance the foreground view quality, applies a Foreground Distillation Compensation module to guide visual attention toward the foreground, and further introduces a Prior Calibration module to mitigate generalization degradation caused by excessive focus on the foreground. Experiments on multiple backbone models and datasets show the effectiveness and compatibility of FVG-PT. Codes are available at: https://github.com/JREion/FVG-PT

