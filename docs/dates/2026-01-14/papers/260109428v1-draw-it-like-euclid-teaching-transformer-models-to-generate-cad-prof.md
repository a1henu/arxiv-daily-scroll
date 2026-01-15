---
layout: default
title: Draw it like Euclid: Teaching transformer models to generate CAD profiles using ruler and compass construction steps
---

# Draw it like Euclid: Teaching transformer models to generate CAD profiles using ruler and compass construction steps
**arXiv**：[2601.09428v1](https://arxiv.org/abs/2601.09428) · [PDF](https://arxiv.org/pdf/2601.09428.pdf)  
**作者**：Siyi Li, Joseph G. Lambourne, Longfei Zhang, Pradeep Kumar Jayaraman, Karl. D. D. Willis  

**一句话要点**：提出基于尺规构造步骤的CAD轮廓生成方法，通过序列化几何操作提升生成质量与参数化编辑能力。

**关键词**：CAD轮廓生成, 几何构造序列, 参数化编辑, 强化学习优化, Transformer模型

## 3 点简述
- 核心问题：如何生成高质量且可参数化编辑的CAD轮廓，减少自由度并保持精度。
- 方法要点：使用序列化几何构造步骤（如偏移、旋转、交点）连接输入几何与最终轮廓，类似思维链机制。
- 实验或效果：引入强化学习优化构造序列，在多项指标上提升生成质量，支持浮点精度参数调整。

## 摘要（原文）

> We introduce a new method of generating Computer Aided Design (CAD) profiles via a sequence of simple geometric constructions including curve offsetting, rotations and intersections. These sequences start with geometry provided by a designer and build up the points and curves of the final profile step by step. We demonstrate that adding construction steps between the designer's input geometry and the final profile improves generation quality in a similar way to the introduction of a chain of thought in language models. Similar to the constraints in a parametric CAD model, the construction sequences reduce the degrees of freedom in the modeled shape to a small set of parameter values which can be adjusted by the designer, allowing parametric editing with the constructed geometry evaluated to floating point precision. In addition we show that applying reinforcement learning to the construction sequences gives further improvements over a wide range of metrics, including some which were not explicitly optimized.

