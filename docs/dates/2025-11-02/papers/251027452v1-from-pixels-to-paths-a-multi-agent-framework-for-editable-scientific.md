---
layout: default
title: From Pixels to Paths: A Multi-Agent Framework for Editable Scientific Illustration
---

# From Pixels to Paths: A Multi-Agent Framework for Editable Scientific Illustration
**arXiv**：[2510.27452v1](https://arxiv.org/abs/2510.27452) · [PDF](https://arxiv.org/pdf/2510.27452.pdf)  
**作者**：Jianwen Sun, Fanrui Zhang, Yukang Feng, Chuanhao Li, Zizhen Li, Jiaxin Ai, Yifan Chang, Yu Dai, Kaipeng Zhang  

**一句话要点**：提出VisPainter多智能体框架以解决科学插图的元素级编辑问题

**关键词**：科学插图生成, 多智能体框架, 矢量图形编辑, 视觉语言模型评估, 元素级控制

## 3 点简述
- 核心问题：现有生成模型缺乏语义结构，代码方法编辑繁琐，无法高效迭代修改科学插图。
- 方法要点：采用多智能体协作，包括Manager、Designer和Toolbox模块，生成可编辑矢量图。
- 实验或效果：引入VisBench基准进行七维评估，验证架构合理性和模型能力。

## 摘要（原文）

> Scientific illustrations demand both high information density and
> post-editability. However, current generative models have two major
> limitations: Frist, image generation models output rasterized images lacking
> semantic structure, making it impossible to access, edit, or rearrange
> independent visual components in the images. Second, code-based generation
> methods (TikZ or SVG), although providing element-level control, force users
> into the cumbersome cycle of "writing-compiling-reviewing" and lack the
> intuitiveness of manipulation. Neither of these two approaches can well meet
> the needs for efficiency, intuitiveness, and iterative modification in
> scientific creation. To bridge this gap, we introduce VisPainter, a multi-agent
> framework for scientific illustration built upon the model context protocol.
> VisPainter orchestrates three specialized modules-a Manager, a Designer, and a
> Toolbox-to collaboratively produce diagrams compatible with standard vector
> graphics software. This modular, role-based design allows each element to be
> explicitly represented and manipulated, enabling true element-level control and
> any element can be added and modified later. To systematically evaluate the
> quality of scientific illustrations, we introduce VisBench, a benchmark with
> seven-dimensional evaluation metrics. It assesses high-information-density
> scientific illustrations from four aspects: content, layout, visual perception,
> and interaction cost. To this end, we conducted extensive ablation experiments
> to verify the rationality of our architecture and the reliability of our
> evaluation methods. Finally, we evaluated various vision-language models,
> presenting fair and credible model rankings along with detailed comparisons of
> their respective capabilities. Additionally, we isolated and quantified the
> impacts of role division, step control,and description on the quality of
> illustrations.

