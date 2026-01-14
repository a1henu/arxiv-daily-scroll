---
layout: default
title: How Do Optical Flow and Textual Prompts Collaborate to Assist in Audio-Visual Semantic Segmentation?
---

# How Do Optical Flow and Textual Prompts Collaborate to Assist in Audio-Visual Semantic Segmentation?
**arXiv**：[2601.08133v1](https://arxiv.org/abs/2601.08133) · [PDF](https://arxiv.org/pdf/2601.08133.pdf)  
**作者**：Peng Gao, Yujian Lee, Yongqi Xu, Wentao Fan  

**一句话要点**：提出SSP框架，集成光流与文本提示以解决音频-视觉语义分割中动态与静态声源挑战。

**关键词**：音频-视觉语义分割, 光流分析, 文本提示, 跨模态对齐, 运动动态建模, 语义场景理解

## 3 点简述
- 核心问题：音频-视觉语义分割需超越像素级声源定位，实现语义理解，面临动态与静态声源共存场景。
- 方法要点：引入SSP框架，利用光流捕捉运动动态，结合类别与场景文本提示，并通过视觉-文本对齐模块增强跨模态整合。
- 实验或效果：SSP在实验中优于现有音频-视觉分割方法，提供高效精确的分割结果，训练中采用后掩码技术学习光流图。

## 摘要（原文）

> Audio-visual semantic segmentation (AVSS) represents an extension of the audio-visual segmentation (AVS) task, necessitating a semantic understanding of audio-visual scenes beyond merely identifying sound-emitting objects at the visual pixel level. Contrary to a previous methodology, by decomposing the AVSS task into two discrete subtasks by initially providing a prompted segmentation mask to facilitate subsequent semantic analysis, our approach innovates on this foundational strategy. We introduce a novel collaborative framework, \textit{S}tepping \textit{S}tone \textit{P}lus (SSP), which integrates optical flow and textual prompts to assist the segmentation process. In scenarios where sound sources frequently coexist with moving objects, our pre-mask technique leverages optical flow to capture motion dynamics, providing essential temporal context for precise segmentation. To address the challenge posed by stationary sound-emitting objects, such as alarm clocks, SSP incorporates two specific textual prompts: one identifies the category of the sound-emitting object, and the other provides a broader description of the scene. Additionally, we implement a visual-textual alignment module (VTA) to facilitate cross-modal integration, delivering more coherent and contextually relevant semantic interpretations. Our training regimen involves a post-mask technique aimed at compelling the model to learn the diagram of the optical flow. Experimental results demonstrate that SSP outperforms existing AVS methods, delivering efficient and precise segmentation results.

