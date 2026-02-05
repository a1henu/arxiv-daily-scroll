---
layout: default
title: Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement
---

# Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement
**arXiv**：[2602.04304v1](https://arxiv.org/abs/2602.04304) · [PDF](https://arxiv.org/pdf/2602.04304.pdf)  
**作者**：Zipeng Zhu, Zhanghao Hu, Qinglin Zhu, Yuxi Hong, Yijun Liu, Jingyong Su, Yulan He, Lin Gui  

**一句话要点**：提出LASER方法，通过层自适应视觉定位与解码增强解决大视觉语言模型在复杂推理任务中的视觉幻觉问题。

**关键词**：大视觉语言模型, 视觉定位, 注意力机制, 视觉问答, 推理增强, 层自适应

## 3 点简述
- 核心问题：固定视觉令牌预算导致图像细节丢失，静态注意力增强方法在复杂任务中效果有限。
- 方法要点：引入VAQ度量动态识别查询相关视觉层，基于此设计LASER进行自适应视觉定位与解码。
- 实验或效果：在多样化VQA基准测试中，LASER显著提升不同复杂度任务的准确性。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have advanced rapidly by aligning visual patches with the text embedding space, but a fixed visual-token budget forces images to be resized to a uniform pretraining resolution, often erasing fine-grained details and causing hallucinations via over-reliance on language priors. Recent attention-guided enhancement (e.g., cropping or region-focused attention allocation) alleviates this, yet it commonly hinges on a static "magic layer" empirically chosen on simple recognition benchmarks and thus may not transfer to complex reasoning tasks. In contrast to this static assumption, we propose a dynamic perspective on visual grounding. Through a layer-wise sensitivity analysis, we demonstrate that visual grounding is a dynamic process: while simple object recognition tasks rely on middle layers, complex visual search and reasoning tasks require visual information to be reactivated at deeper layers. Based on this observation, we introduce Visual Activation by Query (VAQ), a metric that identifies the layer whose attention map is most relevant to query-specific visual grounding by measuring attention sensitivity to the input query. Building on VAQ, we further propose LASER (Layer-adaptive Attention-guided Selective visual and decoding Enhancement for Reasoning), a training-free inference procedure that adaptively selects task-appropriate layers for visual localization and question answering. Experiments across diverse VQA benchmarks show that LASER significantly improves VQA accuracy across tasks with varying levels of complexity.

