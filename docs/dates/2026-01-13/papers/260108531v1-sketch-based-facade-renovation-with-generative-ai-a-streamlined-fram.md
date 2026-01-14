---
layout: default
title: Sketch-Based Facade Renovation With Generative AI: A Streamlined Framework for Bypassing As-Built Modelling in Industrial Adaptive Reuse
---

# Sketch-Based Facade Renovation With Generative AI: A Streamlined Framework for Bypassing As-Built Modelling in Industrial Adaptive Reuse
**arXiv**：[2601.08531v1](https://arxiv.org/abs/2601.08531) · [PDF](https://arxiv.org/pdf/2601.08531.pdf)  
**作者**：Warissara Booranamaitree, Xusheng Du, Yushu Cai, Zhengyang Wang, Ye Zhang, Haoran Xie  

**一句话要点**：提出基于生成AI的三阶段框架，以草图与文本直接生成立面改造方案，绕过精细建模。

**关键词**：立面改造, 生成式人工智能, 视觉语言模型, 草图生成, 稳定扩散, ControlNet

## 3 点简述
- 核心问题：立面改造需先精细建模，耗时费力且反复修改。
- 方法要点：结合VLM预测修改区域，稳定扩散生成新元素，ControlNet优化为逼真图像。
- 实验或效果：在数据集和真实工业建筑上验证，能保留原结构并提升细节质量。

## 摘要（原文）

> Facade renovation offers a more sustainable alternative to full demolition, yet producing design proposals that preserve existing structures while expressing new intent remains challenging. Current workflows typically require detailed as-built modelling before design, which is time-consuming, labour-intensive, and often involves repeated revisions. To solve this issue, we propose a three-stage framework combining generative artificial intelligence (AI) and vision-language models (VLM) that directly processes rough structural sketch and textual descriptions to produce consistent renovation proposals. First, the input sketch is used by a fine-tuned VLM model to predict bounding boxes specifying where modifications are needed and which components should be added. Next, a stable diffusion model generates detailed sketches of new elements, which are merged with the original outline through a generative inpainting pipeline. Finally, ControlNet is employed to refine the result into a photorealistic image. Experiments on datasets and real industrial buildings indicate that the proposed framework can generate renovation proposals that preserve the original structure while improving facade detail quality. This approach effectively bypasses the need for detailed as-built modelling, enabling architects to rapidly explore design alternatives, iterate on early-stage concepts, and communicate renovation intentions with greater clarity.

