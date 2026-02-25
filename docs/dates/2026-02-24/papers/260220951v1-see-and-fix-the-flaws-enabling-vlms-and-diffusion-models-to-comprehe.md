---
layout: default
title: See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis
---

# See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis
**arXiv**：[2602.20951v1](https://arxiv.org/abs/2602.20951) · [PDF](https://arxiv.org/pdf/2602.20951.pdf)  
**作者**：Jaehyun Park, Minyoung Ahn, Minkyu Kim, Jonghyun Lee, Jae-Gil Lee, Dongmin Park  

**一句话要点**：提出ArtiAgent以自动合成带视觉伪影标注的图像对，用于提升扩散模型和视觉语言模型的伪影理解能力。

**关键词**：视觉伪影缓解, 扩散模型, 智能体系统, 数据合成, 图像生成, 伪影标注

## 3 点简述
- 核心问题：AI生成图像常含视觉伪影，现有方法依赖昂贵人工标注，难以扩展。
- 方法要点：设计三智能体系统，通过感知、合成和筛选自动生成伪影注入的图像对。
- 实验或效果：合成10万张图像，展示在多种应用中的有效性和通用性。

## 摘要（原文）

> Despite recent advances in diffusion models, AI generated images still often contain visual artifacts that compromise realism. Although more thorough pre-training and bigger models might reduce artifacts, there is no assurance that they can be completely eliminated, which makes artifact mitigation a highly crucial area of study. Previous artifact-aware methodologies depend on human-labeled artifact datasets, which are costly and difficult to scale, underscoring the need for an automated approach to reliably acquire artifact-annotated datasets. In this paper, we propose ArtiAgent, which efficiently creates pairs of real and artifact-injected images. It comprises three agents: a perception agent that recognizes and grounds entities and subentities from real images, a synthesis agent that introduces artifacts via artifact injection tools through novel patch-wise embedding manipulation within a diffusion transformer, and a curation agent that filters the synthesized artifacts and generates both local and global explanations for each instance. Using ArtiAgent, we synthesize 100K images with rich artifact annotations and demonstrate both efficacy and versatility across diverse applications. Code is available at link.

