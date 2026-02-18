---
layout: default
title: Automatic Funny Scene Extraction from Long-form Cinematic Videos
---

# Automatic Funny Scene Extraction from Long-form Cinematic Videos
**arXiv**：[2602.15381v1](https://arxiv.org/abs/2602.15381) · [PDF](https://arxiv.org/pdf/2602.15381.pdf)  
**作者**：Sibendu Paul, Haotian Jiang, Caren Chen  

**一句话要点**：提出端到端系统以自动提取长视频中的幽默场景，优化内容创作与用户参与度。

**关键词**：长视频理解, 多模态场景定位, 幽默检测, 端到端系统, 内容生成

## 3 点简述
- 核心问题：长视频叙事复杂，幽默依赖多模态，场景定位与识别困难。
- 方法要点：结合视觉与文本线索进行场景分割，利用音频和文本进行多模态幽默标注。
- 实验或效果：在OVSD数据集上AP提升18.3%，幽默检测F1得分0.834，提取场景准确率达98%。

## 摘要（原文）

> Automatically extracting engaging and high-quality humorous scenes from cinematic titles is pivotal for creating captivating video previews and snackable content, boosting user engagement on streaming platforms. Long-form cinematic titles, with their extended duration and complex narratives, challenge scene localization, while humor's reliance on diverse modalities and its nuanced style add further complexity. This paper introduces an end-to-end system for automatically identifying and ranking humorous scenes from long-form cinematic titles, featuring shot detection, multimodal scene localization, and humor tagging optimized for cinematic content. Key innovations include a novel scene segmentation approach combining visual and textual cues, improved shot representations via guided triplet mining, and a multimodal humor tagging framework leveraging both audio and text. Our system achieves an 18.3% AP improvement over state-of-the-art scene detection on the OVSD dataset and an F1 score of 0.834 for detecting humor in long text. Extensive evaluations across five cinematic titles demonstrate 87% of clips extracted by our pipeline are intended to be funny, while 98% of scenes are accurately localized. With successful generalization to trailers, these results showcase the pipeline's potential to enhance content creation workflows, improve user engagement, and streamline snackable content generation for diverse cinematic media formats.

