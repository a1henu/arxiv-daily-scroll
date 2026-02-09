---
layout: default
title: AI-Generated Music Detection in Broadcast Monitoring
---

# AI-Generated Music Detection in Broadcast Monitoring
**arXiv**：[2602.06823v1](https://arxiv.org/abs/2602.06823) · [PDF](https://arxiv.org/pdf/2602.06823.pdf)  
**作者**：David Lopez-Ayala, Asier Cabello, Pablo Zinemanas, Emilio Molina, Martin Rocamora  

**一句话要点**：提出AI-OpenBMAT数据集以解决广播场景中AI生成音乐检测的挑战

**关键词**：AI音乐检测, 广播音频, 数据集构建, 语音掩蔽, 短音乐片段, 模型评估

## 3 点简述
- 核心问题：现有AI音乐检测方法在广播音频中因短片段和语音掩蔽而失效
- 方法要点：构建首个广播风格数据集，结合人类制作音乐与AI生成音乐，模拟真实电视音频模式
- 实验或效果：基准测试显示，流媒体场景模型性能大幅下降，F1分数低于60%，突显关键挑战

## 摘要（原文）

> AI music generators have advanced to the point where their outputs are often indistinguishable from human compositions. While detection methods have emerged, they are typically designed and validated in music streaming contexts with clean, full-length tracks. Broadcast audio, however, poses a different challenge: music appears as short excerpts, often masked by dominant speech, conditions under which existing detectors fail. In this work, we introduce AI-OpenBMAT, the first dataset tailored to broadcast-style AI-music detection. It contains 3,294 one-minute audio excerpts (54.9 hours) that follow the duration patterns and loudness relations of real television audio, combining human-made production music with stylistically matched continuations generated with Suno v3.5. We benchmark a CNN baseline and state-of-the-art SpectTTTra models to assess SNR and duration robustness, and evaluate on a full broadcast scenario. Across all settings, models that excel in streaming scenarios suffer substantial degradation, with F1-scores dropping below 60% when music is in the background or has a short duration. These results highlight speech masking and short music length as critical open challenges for AI music detection, and position AI-OpenBMAT as a benchmark for developing detectors capable of meeting industrial broadcast requirements.

