---
layout: default
title: NeuralCrop: Combining physics and machine learning for improved crop yield predictions
---

# NeuralCrop: Combining physics and machine learning for improved crop yield predictions
**arXiv**：[2512.20177v1](https://arxiv.org/abs/2512.20177) · [PDF](https://arxiv.org/pdf/2512.20177.pdf)  
**作者**：Yunan Lin, Sebastian Bathiany, Maha Badri, Maximilian Gelbrecht, Philipp Hess, Brian Groenke, Jens Heinke, Christoph Müller, Niklas Boers  

**一句话要点**：提出NeuralCrop混合模型，结合物理模型与机器学习以提升气候变化下作物产量预测的准确性和鲁棒性。

**关键词**：作物产量预测, 混合模型, 气候变化适应, 机器学习应用, 生物物理过程模拟

## 3 点简述
- 全球网格作物模型在模拟复杂生物物理过程时存在不确定性，机器学习模型泛化能力不足。
- NeuralCrop融合过程模型与数据驱动组件，先模拟再微调，优化预测性能。
- 实验显示模型在站点和大尺度区域优于现有方法，尤其在干旱极端条件下表现更佳，泛化能力更强。

## 摘要（原文）

> Global gridded crop models (GGCMs) simulate daily crop growth by explicitly representing key biophysical processes and project end-of-season yield time series. They are a primary tool to quantify the impacts of climate change on agricultural productivity and assess associated risks for food security. Despite decades of development, state-of-the-art GGCMs still have substantial uncertainties in simulating complex biophysical processes due to limited process understanding. Recently, machine learning approaches trained on observational data have shown great potential in crop yield predictions. However, these models have not demonstrated improved performance over classical GGCMs and are not suitable for simulating crop yields under changing climate conditions due to problems in generalizing outside their training distributions. Here we introduce NeuralCrop, a hybrid GGCM that combines the strengths of an advanced process-based GGCM, resolving important processes explicitly, with data-driven machine learning components. The model is first trained to emulate a competitive GGCM before it is fine-tuned on observational data. We show that NeuralCrop outperforms state-of-the-art GGCMs across site-level and large-scale cropping regions. Across moisture conditions, NeuralCrop reproduces the interannual yield anomalies in European wheat regions and the US Corn Belt more accurately during the period from 2000 to 2019 with particularly strong improvements under drought extremes. When generalizing to conditions unseen during training, NeuralCrop continues to make robust projections, while pure machine learning models exhibit substantial performance degradation. Our results show that our hybrid crop modelling approach offers overall improved crop modeling and more reliable yield projections under climate change and intensifying extreme weather conditions.

