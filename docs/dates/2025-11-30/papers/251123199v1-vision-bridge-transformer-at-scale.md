---
layout: default
title: Vision Bridge Transformer at Scale
---

# Vision Bridge Transformer at Scale
**arXiv**：[2511.23199v1](https://arxiv.org/abs/2511.23199) · [PDF](https://arxiv.org/pdf/2511.23199.pdf)  
**作者**：Zhenxiong Tan, Zeqing Wang, Xingyi Yang, Songhua Liu, Xinchao Wang  

**一句话要点**：提出Vision Bridge Transformer，通过缩放至20B和1.3B参数，实现基于指令的图像编辑和复杂视频翻译。

**关键词**：Bridge Models, 条件生成, 图像编辑, 视频翻译, Transformer架构, 大规模模型

## 3 点简述
- 核心问题：传统扩散模型从噪声生成数据效率低，需高效数据到数据转换方法。
- 方法要点：采用Bridge Models直接建模输入输出轨迹，结合Transformer架构和方差稳定速度匹配目标。
- 实验或效果：在图像和视频翻译任务中验证有效性，支持大规模条件生成应用。

## 摘要（原文）

> We introduce Vision Bridge Transformer (ViBT), a large-scale instantiation of Brownian Bridge Models designed for conditional generation. Unlike traditional diffusion models that transform noise into data, Bridge Models directly model the trajectory between inputs and outputs, creating an efficient data-to-data translation paradigm. By scaling these models to 20B and 1.3B parameters, we demonstrate their effectiveness for image and video translation tasks. To support this scale, we adopt a Transformer architecture and propose a variance-stabilized velocity-matching objective for robust training. Together, these advances highlight the power of scaling Bridge Models for instruction-based image editing and complex video translation.

