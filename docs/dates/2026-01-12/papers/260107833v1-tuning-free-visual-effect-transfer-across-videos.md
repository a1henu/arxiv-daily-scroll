---
layout: default
title: Tuning-free Visual Effect Transfer across Videos
---

# Tuning-free Visual Effect Transfer across Videos
**arXiv**：[2601.07833v1](https://arxiv.org/abs/2601.07833) · [PDF](https://arxiv.org/pdf/2601.07833.pdf)  
**作者**：Maxwell Jones, Rameen Abdal, Or Patashnik, Ruslan Salakhutdinov, Sergey Tulyakov, Jun-Yan Zhu, Kuan-Chieh Jackson Wang  

**一句话要点**：提出RefVFX框架，以前馈方式将参考视频的复杂时序效果转移到目标视频或图像。

**关键词**：视觉效果转移, 时序一致性, 参考条件编辑, 视频到视频合成, 自动化数据生成, 前馈模型

## 3 点简述
- 核心问题：现有方法难以处理动态时序效果，如动态光照变化或角色变换，这些效果难以通过文本或静态条件描述。
- 方法要点：构建大规模三元组数据集，包括参考效果视频、输入图像或视频及输出视频，使用自动化管道生成高质量配对视频，并基于文本到视频骨干训练参考条件模型。
- 实验或效果：RefVFX产生视觉一致和时序连贯的编辑，泛化到未见效果类别，在定量指标和人类偏好上优于仅提示的基线。

## 摘要（原文）

> We present RefVFX, a new framework that transfers complex temporal effects from a reference video onto a target video or image in a feed-forward manner. While existing methods excel at prompt-based or keyframe-conditioned editing, they struggle with dynamic temporal effects such as dynamic lighting changes or character transformations, which are difficult to describe via text or static conditions. Transferring a video effect is challenging, as the model must integrate the new temporal dynamics with the input video's existing motion and appearance. % To address this, we introduce a large-scale dataset of triplets, where each triplet consists of a reference effect video, an input image or video, and a corresponding output video depicting the transferred effect. Creating this data is non-trivial, especially the video-to-video effect triplets, which do not exist naturally. To generate these, we propose a scalable automated pipeline that creates high-quality paired videos designed to preserve the input's motion and structure while transforming it based on some fixed, repeatable effect. We then augment this data with image-to-video effects derived from LoRA adapters and code-based temporal effects generated through programmatic composition. Building on our new dataset, we train our reference-conditioned model using recent text-to-video backbones. Experimental results demonstrate that RefVFX produces visually consistent and temporally coherent edits, generalizes across unseen effect categories, and outperforms prompt-only baselines in both quantitative metrics and human preference. See our website $\href{https://tuningfreevisualeffects-maker.github.io/Tuning-free-Visual-Effect-Transfer-across-Videos-Project-Page/}{at\ this\ URL}$.

