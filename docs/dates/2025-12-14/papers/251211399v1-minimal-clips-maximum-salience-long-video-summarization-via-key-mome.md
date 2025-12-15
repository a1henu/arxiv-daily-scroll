---
layout: default
title: Minimal Clips, Maximum Salience: Long Video Summarization via Key Moment Extraction
---

# Minimal Clips, Maximum Salience: Long Video Summarization via Key Moment Extraction
**arXiv**：[2512.11399v1](https://arxiv.org/abs/2512.11399) · [PDF](https://arxiv.org/pdf/2512.11399.pdf)  
**作者**：Galann Pennec, Zhengyuan Liu, Nicholas Asher, Philippe Muller, Nancy F. Chen  

**一句话要点**：提出基于关键片段提取的长视频多模态摘要方法，以低成本捕获重要视觉信息。

**关键词**：长视频摘要, 关键片段提取, 视觉语言模型, 多模态摘要, 低成本分析

## 3 点简述
- 问题：长视频中视觉信息易丢失，需低成本分析工具。
- 方法：使用轻量视频描述模型生成片段描述，LLM选择关键片段。
- 效果：在MovieSum数据集上接近参考片段性能，计算成本低。

## 摘要（原文）

> Vision-Language Models (VLMs) are able to process increasingly longer videos. Yet, important visual information is easily lost throughout the entire context and missed by VLMs. Also, it is important to design tools that enable cost-effective analysis of lengthy video content. In this paper, we propose a clip selection method that targets key video moments to be included in a multimodal summary. We divide the video into short clips and generate compact visual descriptions of each using a lightweight video captioning model. These are then passed to a large language model (LLM), which selects the K clips containing the most relevant visual information for a multimodal summary. We evaluate our approach on reference clips for the task, automatically derived from full human-annotated screenplays and summaries in the MovieSum dataset. We further show that these reference clips (less than 6% of the movie) are sufficient to build a complete multimodal summary of the movies in MovieSum. Using our clip selection method, we achieve a summarization performance close to that of these reference clips while capturing substantially more relevant video information than random clip selection. Importantly, we maintain low computational cost by relying on a lightweight captioning model.

