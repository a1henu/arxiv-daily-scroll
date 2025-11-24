---
layout: default
title: Vision Language Models are Confused Tourists
---

# Vision Language Models are Confused Tourists
**arXiv**：[2511.17004v1](https://arxiv.org/abs/2511.17004) · [PDF](https://arxiv.org/pdf/2511.17004.pdf)  
**作者**：Patrick Amadeus Irawan, Ikhlasul Akmal Hanif, Muhammad Dehan Al Kautsar, Genta Indra Winata, Fajri Koto, Alham Fikri Aji  

**一句话要点**：提出ConfusedTourist套件以评估视觉语言模型在混合文化线索下的稳定性

**关键词**：视觉语言模型, 文化对抗鲁棒性, 多文化线索, 注意力机制, 模型稳定性

## 3 点简述
- 现有评估忽视多文化线索共存场景，模型文化稳定性未充分测试
- 引入文化对抗鲁棒性套件，通过图像堆叠和生成扰动评估模型
- 实验显示模型准确率大幅下降，注意力被干扰线索分散

## 摘要（原文）

> Although the cultural dimension has been one of the key aspects in evaluating Vision-Language Models (VLMs), their ability to remain stable across diverse cultural inputs remains largely untested, despite being crucial to support diversity and multicultural societies. Existing evaluations often rely on benchmarks featuring only a singular cultural concept per image, overlooking scenarios where multiple, potentially unrelated cultural cues coexist. To address this gap, we introduce ConfusedTourist, a novel cultural adversarial robustness suite designed to assess VLMs' stability against perturbed geographical cues. Our experiments reveal a critical vulnerability, where accuracy drops heavily under simple image-stacking perturbations and even worsens with its image-generation-based variant. Interpretability analyses further show that these failures stem from systematic attention shifts toward distracting cues, diverting the model from its intended focus. These findings highlight a critical challenge: visual cultural concept mixing can substantially impair even state-of-the-art VLMs, underscoring the urgent need for more culturally robust multimodal understanding.

