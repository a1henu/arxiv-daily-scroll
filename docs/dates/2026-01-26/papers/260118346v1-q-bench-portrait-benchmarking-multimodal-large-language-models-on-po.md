---
layout: default
title: Q-Bench-Portrait: Benchmarking Multimodal Large Language Models on Portrait Image Quality Perception
---

# Q-Bench-Portrait: Benchmarking Multimodal Large Language Models on Portrait Image Quality Perception
**arXiv**：[2601.18346v1](https://arxiv.org/abs/2601.18346) · [PDF](https://arxiv.org/pdf/2601.18346.pdf)  
**作者**：Sijing Wu, Yunhao Li, Zicheng Zhang, Qi Jia, Xinyue Li, Huiyu Duan, Xiongkuo Min, Guangtao Zhai  

**一句话要点**：提出Q-Bench-Portrait基准以评估多模态大语言模型在肖像图像质量感知上的能力

**关键词**：肖像图像质量感知, 多模态大语言模型, 基准测试, 图像质量评估, AIGC失真

## 3 点简述
- 核心问题：现有低层视觉基准主要关注通用图像，缺乏针对肖像图像质量感知的评估。
- 方法要点：构建包含2,765个图像-问题-答案三元组的基准，涵盖多样图像源、质量维度和问题格式。
- 实验或效果：评估25个开源和闭源模型，发现其性能有限且不精确，与人类判断存在差距。

## 摘要（原文）

> Recent advances in multimodal large language models (MLLMs) have demonstrated impressive performance on existing low-level vision benchmarks, which primarily focus on generic images. However, their capabilities to perceive and assess portrait images, a domain characterized by distinct structural and perceptual properties, remain largely underexplored. To this end, we introduce Q-Bench-Portrait, the first holistic benchmark specifically designed for portrait image quality perception, comprising 2,765 image-question-answer triplets and featuring (1) diverse portrait image sources, including natural, synthetic distortion, AI-generated, artistic, and computer graphics images; (2) comprehensive quality dimensions, covering technical distortions, AIGC-specific distortions, and aesthetics; and (3) a range of question formats, including single-choice, multiple-choice, true/false, and open-ended questions, at both global and local levels. Based on Q-Bench-Portrait, we evaluate 20 open-source and 5 closed-source MLLMs, revealing that although current models demonstrate some competence in portrait image perception, their performance remains limited and imprecise, with a clear gap relative to human judgments. We hope that the proposed benchmark will foster further research into enhancing the portrait image perception capabilities of both general-purpose and domain-specific MLLMs.

