---
layout: default
title: Multimodal Evaluation of Russian-language Architectures
---

# Multimodal Evaluation of Russian-language Architectures
**arXiv**：[2511.15552v1](https://arxiv.org/abs/2511.15552) · [PDF](https://arxiv.org/pdf/2511.15552.pdf)  
**作者**：Artem Chervyakov, Ulyana Isaeva, Anton Emelyanov, Artem Safin, Maria Tikhonova, Alexander Kharitonov, Yulia Lyakh, Petr Surovtsev, Denis Shevelev Vildan Saburov, Vasily Konovalov, Elisei Rykov, Ivan Sviridov, Amina Miftakhova, Ilseyar Alimova, Alexander Panchenko, Alexander Kapitanov, Alena Fenogenova  

**一句话要点**：提出Mera Multi多模态评估框架以解决俄语多模态模型缺乏基准的问题

**关键词**：多模态评估, 俄语基准, 指令基准, 模态特定架构, 基准泄露预防, 斯拉夫语言

## 3 点简述
- 核心问题：俄语多模态大模型智能、局限和风险缺乏评估基准
- 方法要点：构建18个新任务，涵盖文本、图像、音频和视频模态
- 实验或效果：提供闭源和开源模型基线结果，防止基准泄露

## 摘要（原文）

> Multimodal large language models (MLLMs) are currently at the center of research attention, showing rapid progress in scale and capabilities, yet their intelligence, limitations, and risks remain insufficiently understood. To address these issues, particularly in the context of the Russian language, where no multimodal benchmarks currently exist, we introduce Mera Multi, an open multimodal evaluation framework for Russian-spoken architectures. The benchmark is instruction-based and encompasses default text, image, audio, and video modalities, comprising 18 newly constructed evaluation tasks for both general-purpose models and modality-specific architectures (image-to-text, video-to-text, and audio-to-text). Our contributions include: (i) a universal taxonomy of multimodal abilities; (ii) 18 datasets created entirely from scratch with attention to Russian cultural and linguistic specificity, unified prompts, and metrics; (iii) baseline results for both closed-source and open-source models; (iv) a methodology for preventing benchmark leakage, including watermarking and licenses for private sets. While our current focus is on Russian, the proposed benchmark provides a replicable methodology for constructing multimodal benchmarks in typologically diverse languages, particularly within the Slavic language family.

