---
layout: default
title: BoxSplitGen: A Generative Model for 3D Part Bounding Boxes in Varying Granularity
---

# BoxSplitGen: A Generative Model for 3D Part Bounding Boxes in Varying Granularity
**arXiv**：[2602.20666v1](https://arxiv.org/abs/2602.20666) · [PDF](https://arxiv.org/pdf/2602.20666.pdf)  
**作者**：Juil Koo, Wei-Tung Lin, Chanho Park, Chanhyeok Park, Minhyuk Sung  

**一句话要点**：提出BoxSplitGen框架，通过迭代分割边界框实现从粗到细的3D形状生成

**关键词**：3D生成模型, 边界框分割, 交互式生成, 扩散模型, 形状细化

## 3 点简述
- 核心问题：现有3D生成模型缺乏辅助人类从抽象到细节的创作过程
- 方法要点：结合边界框分割生成模型和边界框到形状生成模型，支持交互式细化
- 实验或效果：BoxSplitGen在边界框生成上优于基线，形状生成模型基于扩散模型取得优越结果

## 摘要（原文）

> Human creativity follows a perceptual process, moving from abstract ideas to finer details during creation. While 3D generative models have advanced dramatically, models specifically designed to assist human imagination in 3D creation -- particularly for detailing abstractions from coarse to fine -- have not been explored. We propose a framework that enables intuitive and interactive 3D shape generation by iteratively splitting bounding boxes to refine the set of bounding boxes. The main technical components of our framework are two generative models: the box-splitting generative model and the box-to-shape generative model. The first model, named BoxSplitGen, generates a collection of 3D part bounding boxes with varying granularity by iteratively splitting coarse bounding boxes. It utilizes part bounding boxes created through agglomerative merging and learns the reverse of the merging process -- the splitting sequences. The model consists of two main components: the first learns the categorical distribution of the box to be split, and the second learns the distribution of the two new boxes, given the set of boxes and the indication of which box to split. The second model, the box-to-shape generative model, is trained by leveraging the 3D shape priors learned by an existing 3D diffusion model while adapting the model to incorporate bounding box conditioning. In our experiments, we demonstrate that the box-splitting generative model outperforms token prediction models and the inpainting approach with an unconditional diffusion model. Also, we show that our box-to-shape model, based on a state-of-the-art 3D diffusion model, provides superior results compared to a previous model.

