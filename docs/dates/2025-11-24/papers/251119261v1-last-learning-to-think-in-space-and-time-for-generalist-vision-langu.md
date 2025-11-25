---
layout: default
title: LAST: LeArning to Think in Space and Time for Generalist Vision-Language Models
---

# LAST: LeArning to Think in Space and Time for Generalist Vision-Language Models
**arXiv**：[2511.19261v1](https://arxiv.org/abs/2511.19261) · [PDF](https://arxiv.org/pdf/2511.19261.pdf)  
**作者**：Shuai Wang, Daoan Zhang, Tianyi Bai, Shitong Shao, Jiebo Luo, Jiaheng Wei  

**一句话要点**：提出LAST方法，通过空间与时间思维轨迹提升通用视觉语言模型在3D空间和长视频理解能力

**关键词**：视觉语言模型, 3D空间理解, 长视频理解, 思维轨迹, 零样本学习, 微调优化

## 3 点简述
- 核心问题：当前视觉语言模型难以理解3D空间和长视频，依赖专用架构
- 方法要点：使用2D图像输入，构建视觉思维轨迹，联合优化空间与时间理解
- 实验或效果：在零样本和微调场景下，多任务基准显著提升，如EgoSchema增益15.8%

## 摘要（原文）

> Humans can perceive and understand 3D space and long videos from sequential visual observations. But do vision-language models (VLMs) can? Recent work demonstrates that even state-of-the-art VLMs still struggle to understand 3D space and long videos, although they are powerful in typical vision-language tasks. Current methods often rely on specialized architectural designs to improve performance for 3D tasks and video understanding tasks separately. In contrast, we propose LAST, short for LeArn to Think in Space and Time, to jointly improve 3D spatial and long video understanding for general VLMs with only a set of 2D images as inputs. LAST makes VLMs think in space and time rather than only with text before giving the final answer, building visual thinking trajectories in 3D space and temporal dimension. We demonstrate the effectiveness of LAST in two scenarios: 1) zero-shot, where we directly prompt proprietary models; and 2) fine-tuning general VLMs with data that include thinking trajectories in 3D space and time. We show that LAST brings substantial gains in various benchmarks, including 3 spatial understanding, 4 video understanding, and 3 image understanding tasks. Notably, 15.8% gains on EgoSchema with GPT-4o in a zero-shot manner and 8.3 gains on VSI-Bench compared with Qwen2.5-VL-7B.

