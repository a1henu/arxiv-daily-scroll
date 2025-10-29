---
layout: default
title: Listening without Looking: Modality Bias in Audio-Visual Captioning
---

# Listening without Looking: Modality Bias in Audio-Visual Captioning
**arXiv**：[2510.24024v1](https://arxiv.org/abs/2510.24024) · [PDF](https://arxiv.org/pdf/2510.24024.pdf)  
**作者**：Yuchi Ishikawa, Toranosuke Manabe, Tatsuya Komatsu, Yoshimitsu Aoki  

**一句话要点**：揭示音频-视觉字幕模型中的模态偏差，并提出平衡训练方法以减少偏差

**关键词**：音频-视觉字幕, 模态偏差, 鲁棒性测试, 数据集增强, 模态融合, 模型评估

## 3 点简述
- 核心问题：音频-视觉字幕模型存在模态偏差，音频流主导，影响互补性和鲁棒性
- 方法要点：通过选择性抑制或破坏模态流，系统测试模型对音频和视觉的敏感度
- 实验或效果：在AudioVisualCaps数据集上训练，模型模态偏差减少，鲁棒性提升

## 摘要（原文）

> Audio-visual captioning aims to generate holistic scene descriptions by
> jointly modeling sound and vision. While recent methods have improved
> performance through sophisticated modality fusion, it remains unclear to what
> extent the two modalities are complementary in current audio-visual captioning
> models and how robust these models are when one modality is degraded. We
> address these questions by conducting systematic modality robustness tests on
> LAVCap, a state-of-the-art audio-visual captioning model, in which we
> selectively suppress or corrupt the audio or visual streams to quantify
> sensitivity and complementarity. The analysis reveals a pronounced bias toward
> the audio stream in LAVCap. To evaluate how balanced audio-visual captioning
> models are in their use of both modalities, we augment AudioCaps with textual
> annotations that jointly describe the audio and visual streams, yielding the
> AudioVisualCaps dataset. In our experiments, we report LAVCap baseline results
> on AudioVisualCaps. We also evaluate the model under modality robustness tests
> on AudioVisualCaps and the results indicate that LAVCap trained on
> AudioVisualCaps exhibits less modality bias than when trained on AudioCaps.

