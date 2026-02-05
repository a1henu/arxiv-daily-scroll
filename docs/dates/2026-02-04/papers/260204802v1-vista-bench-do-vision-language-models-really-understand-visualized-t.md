---
layout: default
title: VISTA-Bench: Do Vision-Language Models Really Understand Visualized Text as Well as Pure Text?
---

# VISTA-Bench: Do Vision-Language Models Really Understand Visualized Text as Well as Pure Text?
**arXiv**：[2602.04802v1](https://arxiv.org/abs/2602.04802) · [PDF](https://arxiv.org/pdf/2602.04802.pdf)  
**作者**：Qing'an Liu, Juntong Feng, Yuhao Wang, Xinzhe Han, Yujie Cheng, Yue Zhu, Haiwen Diao, Yunzhi Zhuge, Huchuan Lu  

**一句话要点**：提出VISTA-Bench以评估视觉语言模型在可视化文本理解中的模态差距

**关键词**：视觉语言模型, 可视化文本理解, 模态差距, 基准测试, 多模态感知

## 3 点简述
- 核心问题：现有视觉语言模型在处理图像中可视化文本时，性能是否与纯文本相当？
- 方法要点：通过对比纯文本和可视化文本问题，在受控渲染条件下系统评估多模态感知、推理和单模态理解。
- 实验或效果：评估20多个代表性模型，发现显著模态差距，性能随渲染难度增加而下降。

## 摘要（原文）

> Vision-Language Models (VLMs) have achieved impressive performance in cross-modal understanding across textual and visual inputs, yet existing benchmarks predominantly focus on pure-text queries. In real-world scenarios, language also frequently appears as visualized text embedded in images, raising the question of whether current VLMs handle such input requests comparably. We introduce VISTA-Bench, a systematic benchmark from multimodal perception, reasoning, to unimodal understanding domains. It evaluates visualized text understanding by contrasting pure-text and visualized-text questions under controlled rendering conditions. Extensive evaluation of over 20 representative VLMs reveals a pronounced modality gap: models that perform well on pure-text queries often degrade substantially when equivalent semantic content is presented as visualized text. This gap is further amplified by increased perceptual difficulty, highlighting sensitivity to rendering variations despite unchanged semantics. Overall, VISTA-Bench provides a principled evaluation framework to diagnose this limitation and to guide progress toward more unified language representations across tokenized text and pixels. The source dataset is available at https://github.com/QingAnLiu/VISTA-Bench.

