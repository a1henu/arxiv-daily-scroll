---
layout: default
title: VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation
---

# VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation
**arXiv**：[2602.15819v1](https://arxiv.org/abs/2602.15819) · [PDF](https://arxiv.org/pdf/2602.15819.pdf)  
**作者**：Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  

**一句话要点**：提出VideoSketcher，利用预训练视频模型实现可控顺序草图生成

**关键词**：顺序草图生成, 视频扩散模型, 两阶段微调, 数据高效学习, 可控生成

## 3 点简述
- 核心问题：现有生成模型忽略草图绘制的时间顺序，难以模拟创造性过程
- 方法要点：结合LLM规划语义顺序与视频扩散模型渲染，通过两阶段微调学习顺序与外观
- 实验或效果：仅用少量人工数据生成高质量顺序草图，支持笔刷风格控制和自回归生成

## 摘要（原文）

> Sketching is inherently a sequential process, in which strokes are drawn in a meaningful order to explore and refine ideas. However, most generative models treat sketches as static images, overlooking the temporal structure that underlies creative drawing. We present a data-efficient approach for sequential sketch generation that adapts pretrained text-to-video diffusion models to generate sketching processes. Our key insight is that large language models and video diffusion models offer complementary strengths for this task: LLMs provide semantic planning and stroke ordering, while video diffusion models serve as strong renderers that produce high-quality, temporally coherent visuals. We leverage this by representing sketches as short videos in which strokes are progressively drawn on a blank canvas, guided by text-specified ordering instructions. We introduce a two-stage fine-tuning strategy that decouples the learning of stroke ordering from the learning of sketch appearance. Stroke ordering is learned using synthetic shape compositions with controlled temporal structure, while visual appearance is distilled from as few as seven manually authored sketching processes that capture both global drawing order and the continuous formation of individual strokes. Despite the extremely limited amount of human-drawn sketch data, our method generates high-quality sequential sketches that closely follow text-specified orderings while exhibiting rich visual detail. We further demonstrate the flexibility of our approach through extensions such as brush style conditioning and autoregressive sketch generation, enabling additional controllability and interactive, collaborative drawing.

