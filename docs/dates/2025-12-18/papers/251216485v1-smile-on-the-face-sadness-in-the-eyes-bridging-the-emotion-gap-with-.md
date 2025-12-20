---
layout: default
title: Smile on the Face, Sadness in the Eyes: Bridging the Emotion Gap with a Multimodal Dataset of Eye and Facial Behaviors
---

# Smile on the Face, Sadness in the Eyes: Bridging the Emotion Gap with a Multimodal Dataset of Eye and Facial Behaviors
**arXiv**：[2512.16485v1](https://arxiv.org/abs/2512.16485) · [PDF](https://arxiv.org/pdf/2512.16485.pdf)  
**作者**：Kejun Liu, Yuanyuan Liu, Lin Wei, Chang Tang, Yibing Zhan, Zijing Chen, Zhe Chen  

**一句话要点**：提出眼行为辅助多模态情感识别数据集与模型，以解决面部表情与真实情感间的差距问题。

**关键词**：情感识别, 多模态数据集, 眼行为建模, 面部表情识别, Transformer模型, 自发情感诱导

## 3 点简述
- 核心问题：面部表情常作为社交工具而非真实情感表现，导致情感识别与面部表情识别间存在差距。
- 方法要点：构建眼行为辅助多模态情感识别数据集，结合自发情感诱导范式收集眼行为与面部视频数据。
- 实验或效果：设计眼行为辅助多模态Transformer模型，在七种基准协议下显著优于现有方法，验证眼行为建模的重要性。

## 摘要（原文）

> Emotion Recognition (ER) is the process of analyzing and identifying human emotions from sensing data. Currently, the field heavily relies on facial expression recognition (FER) because visual channel conveys rich emotional cues. However, facial expressions are often used as social tools rather than manifestations of genuine inner emotions. To understand and bridge this gap between FER and ER, we introduce eye behaviors as an important emotional cue and construct an Eye-behavior-aided Multimodal Emotion Recognition (EMER) dataset. To collect data with genuine emotions, spontaneous emotion induction paradigm is exploited with stimulus material, during which non-invasive eye behavior data, like eye movement sequences and eye fixation maps, is captured together with facial expression videos. To better illustrate the gap between ER and FER, multi-view emotion labels for mutimodal ER and FER are separately annotated. Furthermore, based on the new dataset, we design a simple yet effective Eye-behavior-aided MER Transformer (EMERT) that enhances ER by bridging the emotion gap. EMERT leverages modality-adversarial feature decoupling and a multitask Transformer to model eye behaviors as a strong complement to facial expressions. In the experiment, we introduce seven multimodal benchmark protocols for a variety of comprehensive evaluations of the EMER dataset. The results show that the EMERT outperforms other state-of-the-art multimodal methods by a great margin, revealing the importance of modeling eye behaviors for robust ER. To sum up, we provide a comprehensive analysis of the importance of eye behaviors in ER, advancing the study on addressing the gap between FER and ER for more robust ER performance. Our EMER dataset and the trained EMERT models will be publicly available at https://github.com/kejun1/EMER.

