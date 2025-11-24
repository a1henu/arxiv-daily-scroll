---
layout: default
title: FireScope: Wildfire Risk Prediction with a Chain-of-Thought Oracle
---

# FireScope: Wildfire Risk Prediction with a Chain-of-Thought Oracle
**arXiv**：[2511.17171v1](https://arxiv.org/abs/2511.17171) · [PDF](https://arxiv.org/pdf/2511.17171.pdf)  
**作者**：Mario Markov, Stefan Maria Ailuro, Luc Van Gool, Konrad Schindler, Danda Pani Paudel  

**一句话要点**：提出FireScope框架以解决跨大陆野火风险预测问题

**关键词**：野火风险预测, 视觉语言模型, 跨大陆泛化, 推理轨迹, 多模态数据, 栅格生成

## 3 点简述
- 核心问题：现有方法缺乏因果推理和多模态理解，难以可靠泛化野火风险预测。
- 方法要点：基于VLM的推理生成框架，结合强化学习和视觉监督预测风险栅格与推理轨迹。
- 实验或效果：在跨大陆测试中性能显著提升，推理轨迹被验证为忠实且语义有意义。

## 摘要（原文）

> Predicting wildfire risk is a reasoning-intensive spatial problem that requires the integration of visual, climatic, and geographic factors to infer continuous risk maps. Existing methods lack the causal reasoning and multimodal understanding required for reliable generalization. We introduce $\textbf{FireScope-Bench}$, a large-scale dataset and benchmark that couples Sentinel-2 imagery and climate data with expert-defined risk rasters across the USA, and real wildfire events in Europe for cross-continental evaluation. Building on this dataset, we propose $\textbf{FireScope}$, a VLM-based reasoning-to-generation framework that learns from both reinforcement learning and visual supervision to predict risk rasters with complementary reasoning traces. When trained in the USA and tested in Europe, $\textbf{FireScope}$ achieves substantial performance gains, while expert feedback and automated analysis confirm that its reasoning traces are faithful and semantically meaningful. Our findings demonstrate that reasoning can ground raster prediction models, improving both generalization and interpretability. To our knowledge, this is the first framework to (1) demonstrate that language-based reasoning can improve generalization in visual generation, (2) propose a high-resolution wildfire risk model that can be applied across continents, and (3) enable systematic studies of robust cross-continental generalization for multimodal fire risk models. We believe that $\textbf{FireScope-Bench}$ has the potential to serve as a foundation for advancing reasoning-driven, interpretable and generalizable spatial modeling. Data and source code will be made publicly available.

