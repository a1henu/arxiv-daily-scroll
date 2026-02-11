---
layout: default
title: Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing
---

# Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing
**arXiv**：[2602.09609v1](https://arxiv.org/abs/2602.09609) · [PDF](https://arxiv.org/pdf/2602.09609.pdf)  
**作者**：Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  

**一句话要点**：提出Tele-Omni统一多模态框架，以支持基于多模态指令的视频生成与编辑

**关键词**：视频生成, 视频编辑, 多模态框架, 扩散模型, 指令解析

## 3 点简述
- 现有视频生成方法多依赖文本指令，难以统一处理多模态输入和多样化任务
- Tele-Omni利用预训练多模态大语言模型解析指令，结合扩散模型进行视频合成
- 实验显示该框架在多种视频任务中表现竞争性，保持时间连贯性和视觉一致性

## 摘要（原文）

> Recent advances in diffusion-based video generation have substantially improved visual fidelity and temporal coherence. However, most existing approaches remain task-specific and rely primarily on textual instructions, limiting their ability to handle multimodal inputs, contextual references, and diverse video generation and editing scenarios within a unified framework. Moreover, many video editing methods depend on carefully engineered pipelines tailored to individual operations, which hinders scalability and composability. In this paper, we propose Tele-Omni, a unified multimodal framework for video generation and editing that follows multimodal instructions, including text, images, and reference videos, within a single model. Tele-Omni leverages pretrained multimodal large language models to parse heterogeneous instructions and infer structured generation or editing intents, while diffusion-based generators perform high-quality video synthesis conditioned on these structured signals. To enable joint training across heterogeneous video tasks, we introduce a task-aware data processing pipeline that unifies multimodal inputs into a structured instruction format while preserving task-specific constraints. Tele-Omni supports a wide range of video-centric tasks, including text-to-video generation, image-to-video generation, first-last-frame video generation, in-context video generation, and in-context video editing. By decoupling instruction parsing from video synthesis and combining it with task-aware data design, Tele-Omni achieves flexible multimodal control while maintaining strong temporal coherence and visual consistency. Experimental results demonstrate that Tele-Omni achieves competitive performance across multiple tasks.

