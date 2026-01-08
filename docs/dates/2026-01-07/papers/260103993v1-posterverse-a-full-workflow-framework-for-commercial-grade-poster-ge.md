---
layout: default
title: PosterVerse: A Full-Workflow Framework for Commercial-Grade Poster Generation with HTML-Based Scalable Typography
---

# PosterVerse: A Full-Workflow Framework for Commercial-Grade Poster Generation with HTML-Based Scalable Typography
**arXiv**：[2601.03993v1](https://arxiv.org/abs/2601.03993) · [PDF](https://arxiv.org/pdf/2601.03993.pdf)  
**作者**：Junle Liu, Peirong Zhang, Yuyi Zhang, Pengyu Yan, Hui Zhou, Xinyue Zhou, Fengjun Guo, Lianwen Jin  

**一句话要点**：提出PosterVerse框架，通过全流程自动化解决商业海报生成中的设计不完整与文本渲染不精确问题。

**关键词**：海报生成, HTML排版, 扩散模型, 多模态大语言模型, 商业设计自动化

## 3 点简述
- 核心问题：现有自动化海报生成系统存在设计流程不完整、文本渲染准确性差和商业应用灵活性不足的局限。
- 方法要点：采用三阶段流程，包括LLM蓝图创建、扩散模型背景生成和MLLM驱动的HTML引擎统一布局文本渲染。
- 实验或效果：实验表明PosterVerse能生成视觉吸引、文本对齐准确且可定制的商业级海报，并引入HTML数据集PosterDNA提升训练效果。

## 摘要（原文）

> Commercial-grade poster design demands the seamless integration of aesthetic appeal with precise, informative content delivery. Current automated poster generation systems face significant limitations, including incomplete design workflows, poor text rendering accuracy, and insufficient flexibility for commercial applications. To address these challenges, we propose PosterVerse, a full-workflow, commercial-grade poster generation method that seamlessly automates the entire design process while delivering high-density and scalable text rendering. PosterVerse replicates professional design through three key stages: (1) blueprint creation using fine-tuned LLMs to extract key design elements from user requirements, (2) graphical background generation via customized diffusion models to create visually appealing imagery, and (3) unified layout-text rendering with an MLLM-powered HTML engine to guarantee high text accuracy and flexible customization. In addition, we introduce PosterDNA, a commercial-grade, HTML-based dataset tailored for training and validating poster design models. To the best of our knowledge, PosterDNA is the first Chinese poster generation dataset to introduce HTML typography files, enabling scalable text rendering and fundamentally solving the challenges of rendering small and high-density text. Experimental results demonstrate that PosterVerse consistently produces commercial-grade posters with appealing visuals, accurate text alignment, and customizable layouts, making it a promising solution for automating commercial poster design. The code and model are available at https://github.com/wuhaer/PosterVerse.

