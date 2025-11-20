---
layout: default
title: BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching
---

# BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching
**arXiv**：[2511.15066v1](https://arxiv.org/abs/2511.15066) · [PDF](https://arxiv.org/pdf/2511.15066.pdf)  
**作者**：Yachuan Huang, Xianrui Luo, Qiwen Wang, Liao Shen, Jiaqi Li, Huiqiang Sun, Zihao Huang, Wei Jiang, Zhiguo Cao  

**一句话要点**：提出BokehFlow框架，基于流匹配实现无需深度的可控散景渲染。

**关键词**：散景渲染, 流匹配, 可控生成, 深度无关, 文本控制, 图像合成

## 3 点简述
- 核心问题：现有可控散景渲染方法依赖深度图，缺乏深度输入时难以实现高效控制。
- 方法要点：使用流匹配和交叉注意力机制，通过文本提示控制焦点区域和模糊强度。
- 实验或效果：在多个数据集上验证，渲染质量和效率优于现有方法，实现逼真散景效果。

## 摘要（原文）

> Bokeh rendering simulates the shallow depth-of-field effect in photography, enhancing visual aesthetics and guiding viewer attention to regions of interest. Although recent approaches perform well, rendering controllable bokeh without additional depth inputs remains a significant challenge. Existing classical and neural controllable methods rely on accurate depth maps, while generative approaches often struggle with limited controllability and efficiency. In this paper, we propose BokehFlow, a depth-free framework for controllable bokeh rendering based on flow matching. BokehFlow directly synthesizes photorealistic bokeh effects from all-in-focus images, eliminating the need for depth inputs. It employs a cross-attention mechanism to enable semantic control over both focus regions and blur intensity via text prompts. To support training and evaluation, we collect and synthesize four datasets. Extensive experiments demonstrate that BokehFlow achieves visually compelling bokeh effects and offers precise control, outperforming existing depth-dependent and generative methods in both rendering quality and efficiency.

